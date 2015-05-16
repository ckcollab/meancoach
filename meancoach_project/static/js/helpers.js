// Buffers tasks to only execute ONCE after delay has ended
var delay = (function() {
    var timer = 0;
    return function(callback, ms) {
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
    };
})();


var set_status_bar = function(message, css_class, fade_out_time) {
    fade_out_time = fade_out_time || 3000;
    var result = $('#bottom_status_bar').html(message).addClass(css_class).fadeIn().fadeOut(fade_out_time);
};
//$('#bottom_status_bar').html("Saved!").addClass('alert-success').fadeIn().fadeOut(3000);
//
//
//$('#bottom_status_bar').html("Error saving! Do you have a connection to the Internet?").addClass('alert-danger').fadeIn();
