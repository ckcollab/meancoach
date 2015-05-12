<metric-record-form>
    <div class="panel panel-default" hide="{ opts.only_show_first_of_month && opts.day_of_month != 1 }">
        <div class="panel-heading">
            <h1>{ opts.title } <small>for { moment(opts.date).format("MMM Do") }</small></h1>

            <div hide="{ opts.only_show_first_of_month }">
                <a href="input?date={ moment(opts.date).subtract(1, 'days').format() }">
                    <small>previous day</small>
                </a> -
                <a href="input?date={ moment(opts.date).add(1, 'days').format() }">
                    <small>next day</small>
                </a>
            </div>
        </div>

        <div class="panel-body">
            <metric-record-form-input each="{ opts.metrics }"></metric-record-form-input>
        </div>
    </div>


</metric-record-form>

<metric-record-form-input>
    <p>{ this.name } -> { this.measurement }</p>




</metric-record-form-input>
