<metric-record-form-container>
    <span class="day_link" onclick="{ this.previous_day }">
        <small>previous day</small>
    </span> -
    <span class="day_link" onclick="{ this.next_day }">
        <small>next day</small>
    </span>

    <metric-record-form title="Daily Metrics"
                        metrics="{ opts.daily_entries }">
    </metric-record-form>

    <metric-record-form title="Monthly Metrics"
                        metrics="{ opts.monthly_entries }"
                        only_show_first_of_month="1">
    </metric-record-form>

    /*
       Component methods
     */
    var self = this;

    self.change_day = function(day_difference) {
        var new_date = moment(opts.date).add(day_difference, 'days');
        $.get("?date=" + new_date.format())
            .success(function(data) {
                self.trigger('day_changed', $.parseJSON(data));
            })
            .error(function() {
                console.log("error changin page");
            });
    }
    self.previous_day = function() {
        self.change_day(-1);
    }
    self.next_day = function() {
        self.change_day(1);
    }

    //self.load_data = function(new_data) {
    //   //opts.metrics = new_data[opts.metric_context_name];
    //    opts = _.extend(opts, new_data);
    //    self.update();
    //    console.log(opts);
    //}

    /*
       Event handlers
     */
    // Called when the day is moved forwards or backwards
    self.on('day_changed', function(new_data) {
        riot.route('date/' + moment(opts.date).format());
        opts = _.extend(opts, new_data);
        self.update();
    });

    // Called when a form value has changed
    self.on('form_changed', function() {
        delay(function() {


            // SEND SAVE STUFF HERE!!!





            set_status_bar('Pretend saved!', 'alert-success', 3000)
        }, 1500);
    });

    // Called when form is saved successfully
    self.on('form_save_success', function() {});

    // Called when form is not saved successfully
    self.on('form_save_failure', function() {});
</metric-record-form-container>


<metric-record-form>
    <div class="panel panel-default"
         hide="{ opts.only_show_first_of_month && opts.day_of_month != 1 }">
        <div class="panel-heading">
            <h1>{ opts.title } <small>for { moment(opts.date).format("MMM Do") }</small></h1>
        </div>

        <div class="panel-body">
            <metric-record-form-input each="{ opts.metrics }">
            </metric-record-form-input>
        </div>
    </div>

    /*
       Component methods
     */
    var self = this;

    self.load_data = function(new_data) {
        //opts.metrics = new_data[opts.metric_context_name];
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
        for (metric in self.opts.metrics) {
            // find the right metric to update
            if (self.opts.metrics[metric].metric_id == input.metric_id) {
                self.opts.metrics[metric].measurement = input.measurement;
                self.opts.metrics[metric].notes = input.notes;
            }
        }
        self.update();

        self.parent.trigger('form_changed');
    });

    /*
       Constructor/initializer
     */
    // Have to initialize with data from parent first, then day_changed
    // event is fired to update later
    self.load_data(self.parent.opts);
</metric-record-form>


<metric-record-form-input>
    <div class="col-lg-6">
        <h3 class="title">
            <span class="label"
                  style="background-color: { this.convert_to_hsl(this.measurement) };">
                { this.measurement }
            </span>
            { this.name }
        </h3>
        <small class="description_worst">{ this.description_worst }</small>
        <small class="description_best">{ this.description_best }</small>

        <input type="range"
               id="id_measurement"
               name="measurement"
               min="1"
               max="10"
               value="{ this.measurement }"
               onchange="{ this.on_form_value_changed('measurement') }">
        <textarea id="id_notes"
                  name="notes"
                  oninput="{ this.on_form_value_changed('notes') }">
            { this.notes }
        </textarea>
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
</metric-record-form-input>
