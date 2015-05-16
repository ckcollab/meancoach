<metric-record-form>
    <div class="panel panel-default"
         hide="{ opts.only_show_first_of_month && opts.day_of_month != 1 }">
        <div class="panel-heading">
            <h1>{ opts.title } <small>for { moment(opts.date).format("MMM Do") }</small></h1>

            <div hide="{ opts.only_show_first_of_month }">
                <span class="day_link" onclick="{ this.previous_day }">
                    <small>previous day</small>
                </span> -
                <span class="day_link" onclick="{ this.next_day }">
                    <small>next day</small>
                </span>
            </div>
        </div>

        <div class="panel-body">
            <metric-record-form-input each="{ opts.metrics }"></metric-record-form-input>
        </div>
    </div>

    // Component methods
    var self = this;

    self.load_data = function(new_data) {
        opts.metrics = new_data[opts.metric_context_name];
        opts = _.extend(opts, new_data);
        self.update();

        riot.route('date/' + moment(opts.date).format());
    }
    self.change_day = function(day_difference) {
        var new_date = moment(opts.date).add(day_difference, 'days');
        $.get("?date=" + new_date.format())
            .success(function(data) {
                opts.input_context.trigger('day_changed', $.parseJSON(data));
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

    // Event handlers
    opts.input_context.on('day_changed', self.load_data);

    // Initializer/constructor
    self.load_data(opts);
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
               onchange="{ this.on_measurement_change }">

        <textarea name="notes">{ this.notes }</textarea>
    </div>

    // Component methods
    var self = this;

    self.on_measurement_change = function() {
        // No data binding in riotjs, manually change the value
        self.measurement = self.id_measurement.value;
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
