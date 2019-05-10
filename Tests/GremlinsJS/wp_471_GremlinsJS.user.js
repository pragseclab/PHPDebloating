// ==UserScript==
// @name     wp_471_GremlinsJS
// @version  1
// @grant    none
// @include  http://localhost:8085/WordPress-4.7.1/*
// @require  https://raw.githubusercontent.com/marmelab/gremlins.js/master/gremlins.min.js
// @require  https://code.jquery.com/jquery-3.3.1.min.js
// ==/UserScript==
$(document).ready(function(){
    $( 'a' ).each(function() {
        if( location.hostname === this.hostname || !this.hostname.length) {
            //$(this).removeAttr("href");;
        } else {
            $(this).removeAttr("href");;
        }
        if(this.href.indexOf('logout') != -1 || this.href.indexOf('rss') != -1){ // Remove logout link
            $(this).empty();
        }
    });
    setCookie('test_group','wp471_monkey_test', 1, 'WordPress-4.7.1');
    setCookie('test_name','wp471_gremlinsjs', 1, 'WordPress-4.7.1');
    setCookie('software_id','4', 1, 'WordPress-4.7.1');
    setCookie('software_version_id','20', 1, 'WordPress-4.7.1');
    console.log('UNLEASH THEM MONKEEEYS!');
    // You can also run this in any file now!
    var horde = gremlins.createHorde()
    .gremlin(gremlins.species.clicker().clickTypes(['click']))
    .gremlin(gremlins.species.formFiller())
    .gremlin(gremlins.species.scroller());
    horde.strategy(gremlins.strategies.distribution().delay(25).distribution([0.48, 0.47, 0.05]));
    horde.mogwai(gremlins.mogwais.gizmo().maxErrors(-1)); // Prevent Gizmo from stopping the test after 10 js errors
    horde.mogwai(gremlins.mogwais.alert()); // overrides alerts
    horde.seed(1234);
    horde.unleash();
});

function setCookie(name,value,days, path) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=" + path;
}
