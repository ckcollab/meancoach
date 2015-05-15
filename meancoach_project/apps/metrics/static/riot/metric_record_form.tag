<metric-record-form>
    <div class="panel panel-default" hide="{ opts.only_show_first_of_month && opts.day_of_month != 1 }">
        <div class="panel-heading">
            <h1>{ opts.title } <small>for { moment(opts.date).format("MMM Do") }</small></h1>

            <div hide="{ opts.only_show_first_of_month }">
                <button onclick="{ this.previous_day }">
                    <small>previous day</small>
                </button> -
                <button onclick="{ this.next_day }">
                    <small>next day</small>
                </button>
            </div>
        </div>

        <div class="panel-body">
            <metric-record-form-input each="{ opts.metrics }"></metric-record-form-input>
        </div>
    </div>

    var self = this;

    self.change_day = function(day_difference) {
        var new_date = moment(opts.date).add(day_difference, 'days');
        $.get("?date=" + new_date.format())
            .success(function(data) {
                riot.route('date/' + new_date.format());

                // If I manually change the date here and then do update, it works
                //opts.date = new_date;
                //self.update();

                // However, I should be able to more cleanly update everything
                // by passing the whole object... but it doesn't owrk!
                var obj = $.parseJSON(data);
                self.update(obj);
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
</metric-record-form>

<metric-record-form-input>
    <p>{ this.name } -> { this.measurement }</p>




</metric-record-form-input>
