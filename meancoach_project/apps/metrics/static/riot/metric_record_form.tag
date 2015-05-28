<metric-record-form-container>
    <span class="day_link previous" onclick="{ this.previous_day }">
        <small>previous day</small>
    </span> -
    <span class="day_link next" onclick="{ this.next_day }">
        <small>next day</small>
    </span>

    <metric-record-form title="Daily Metrics"
                        metrics="{ opts.daily_entries }"
                        checklist="{ opts.daily_checklist }">
    </metric-record-form>

    <metric-record-form title="Monthly Metrics"
                        metrics="{ opts.monthly_entries }"
                        only_show_first_of_month="1">
    </metric-record-form>

    /*
       Component methods
     */
    var self = this;

    self.change_day = function(new_date) {
        $.get("?date=" + new_date.format())
            .success(function(data) {
                self.trigger('day_changed', $.parseJSON(data));
            })
            .error(function() {
                alert('Could not change page, is your Internet connection working?');
            });
    }
    self.previous_day = function() {
        self.change_day(moment(opts.date).add(-1, 'days'));
    }
    self.next_day = function() {
        self.change_day(moment(opts.date).add(1, 'days'));
    }

    /*
       Event handlers
     */
    // Called when the day is moved forwards or backwards
    self.on('day_changed', function(new_data) {
        riot.route('date/' + moment(new_data.date).format());
        opts = _.extend(opts, new_data);
        self.update();
    });

    // Called when a form value has changed
    self.on('form_changed', function() {
        var raw_measurements = [].concat(
            opts.daily_checklist,
            opts.daily_entries,
            opts.monthly_entries
        )
        var save_date = moment(opts.date).format();
        var prepared_measurements = {};

        for (i in raw_measurements) {
            var metric_id = raw_measurements[i].metric_id;
            prepared_measurements[metric_id] = {
                notes: raw_measurements[i].notes,
                measurement: raw_measurements[i].measurement
            }
        }

        delay(function() {
            $.post("?date=" + save_date,
                   JSON.stringify(prepared_measurements))
                .success(function() {
                    self.trigger('form_save_success');
                })
                .error(function() {
                    self.trigger('form_save_failure');
                });

        }, 2000);
    });

    // Called when form is saved successfully
    self.on('form_save_success', function() {
        set_status_bar('Saved!', 'alert-success', 3000);
    });

    // Called when form is not saved successfully
    self.on('form_save_failure', function() {
        set_status_bar('Failed to save, do you have an Internet connection?', 'alert-danger', 3000);
    });
</metric-record-form-container>


<metric-record-form>
    <div class="panel panel-default"
         hide="{ opts.only_show_first_of_month && this.parent.opts.day_of_month != 1 }">
        <div class="panel-heading">
            <h1>
                { opts.title }
                <small>for <span class="metric_date">{ moment(this.parent.opts.date).format("MMM Do") }</span></small>
            </h1>
        </div>

        <div class="panel-body">
            <h3 show="{ opts.checklist && opts.checklist.length > 0 }">Checklist</h3>

            <div class="control-group">
                <div class="controls">
                    <checklist each="{ opts.checklist }"></checklist>
                </div>
            </div>

            <measurement each="{ opts.metrics }">
            </measurement>
        </div>
    </div>

    /*
       Component methods
     */
    var self = this;

    self.load_data = function(new_data) {
        opts = _.extend(opts, new_data);
        self.update();
    }

    /*
       Event handlers
     */
    // Container events
    self.parent.on('day_changed', self.load_data);

    // This form events
    self.on('form_input_changed', function(input) {
        var all_metrics = self.opts.metrics;
        if(self.opts.checklist) {
            all_metrics = self.opts.metrics.concat(self.opts.checklist);
        }

        for (metric in all_metrics) {
            // find the right metric to update
            if (all_metrics[metric].metric_id == input.metric_id) {
                all_metrics[metric].measurement = input.measurement;
                all_metrics[metric].notes = input.notes;
            }
        }
        self.update();

        self.parent.trigger('form_changed');
    });
</metric-record-form>


<checklist>
    <label class="checkbox-inline">
        <input type="checkbox"
               id="id_measurement"
               checked="{ this.measurement > 0 }"
               onchange="{ this.checkbox_changed }">
        { this.name }
    </label>

    /*
       Component methods
     */
    var self = this;

    self.checkbox_changed = function() {
        this.measurement = this.id_measurement.checked ? 1 : 0;
        self.update();

        self.parent.trigger('form_input_changed', self);
    };

</checklist>


<measurement>
    <div class="col-lg-6">
        <h3 class="title">
            <span class="label"
                  style="background-color: { this.convert_to_hsl(this.measurement) };">
                { this.measurement }
            </span>
            { this.name }
        </h3>
        <small class="description_worst">1 being { this.description_worst }</small>
        <small class="description_best">10 being { this.description_best }</small>

        <input type="range"
               id="id_measurement"
               name="measurement"
               min="1"
               max="10"
               value="{ this.measurement }"
               onchange="{ this.on_form_value_changed('measurement') }">
        <textarea id="id_notes"
                  name="notes"
                  oninput="{ this.on_form_value_changed('notes') }"
                  placeholder="notes"
        >{ this.notes }</textarea>
    </div>

    /*
       Component methods
     */
    var self = this;

    // No data binding in riotjs, manually change the value
    self.on_form_value_changed = function(field_name) {
        return function() {
            // In django forms typically the form's id == "id_the_name_of_field"
            // and the "name" property of the field is "name_of_field"
            self[field_name] = self["id_" + field_name].value;
            self.update();

            // Note this triggers the parent form not the CONTAINER event
            self.parent.trigger('form_input_changed', self);
        }
    }

    self.convert_to_hsl = function(value){
        var hue = ((value * 12) - 12);
        var sat = '50%';
        var l = '65%';
        // Skip gold color, make it gray
        if(value == 5) {
            sat = '0%';
        } else if (value > 5) {
            hue += 24;
        }
        return 'hsl(' + hue + ', ' + sat + ', ' + l + ')';
    };
</measurement>
