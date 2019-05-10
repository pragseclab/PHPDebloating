// ==UserScript==
// @name     pma_470_GremlinsJS
// @version  1
// @grant    none
// @include  http://localhost:8085/phpMyAdmin-4.7.0-all-languages/*
// @require  https://raw.githubusercontent.com/marmelab/gremlins.js/master/gremlins.min.js
// ==/UserScript==

var horde;

$(document).ready(function(){
    $( 'a' ).each(function() {
        if( location.hostname === this.hostname || !this.hostname.length ) {
            //$(this).addClass('local');
        } else {
            $(this).removeAttr("href");;
        }
        if(this.href.indexOf('logout.php') != -1){ // Remove logout link
            $(this).empty();
        }
    });
    setCookie('test_group','pma470_monkey_test', 1, 'phpMyAdmin-4.7.0-all-languages');
    setCookie('test_name','pma470_gremlinsjs_loggedin', 1, 'phpMyAdmin-4.7.0-all-languages');
    setCookie('software_id','1', 1, 'phpMyAdmin-4.7.0-all-languages');
    setCookie('software_version_id','4', 1, 'phpMyAdmin-4.7.0-all-languages');
    console.log('UNLEASH THEM MONKEEEYS!');
    // You can also run this in any file now!
    horde = gremlins.createHorde()
    .gremlin(gremlins.species.clicker().clickTypes(['click']))
    .gremlin(gremlins.species.formFiller())
    .gremlin(gremlins.species.scroller());
    horde.strategy(gremlins.strategies.distribution().delay(25).distribution([0.48, 0.47, 0.05]).randomizer(new Chance(1234)));
    horde.mogwai(gremlins.mogwais.gizmo().maxErrors(-1)); // Prevent Gizmo from stopping the test after 10 js errors
    horde.mogwai(gremlins.mogwais.alert()); // overrides alerts
    horde.seed(1234);
    horde.unleash();
});

setTimeout(function(){
  if (horde != null) {
      horde.stop();
  }
  window.location = "http://localhost:8085/phpMyAdmin-4.7.0-all-languages/";
}, 120000);

$(window).on("beforeunload", function() {
    if (horde != null) {
        horde.stop();
        horde = null;
    }
});

$(document).bind("ajaxSend", function(){
    if (horde != null) {
        horde.stop();
        horde = null;
    }
});

$(document).bind("ajaxComplete", function(){
    $( 'a' ).each(function() {
        if( location.hostname === this.hostname || !this.hostname.length ) {
            //$(this).addClass('local');
        } else {
            $(this).removeAttr("href");;
        }
        if(this.href.indexOf('logout.php') != -1){ // Remove logout link
            $(this).empty();
        }
    });
    if (horde == null) {
        horde = gremlins.createHorde()
        .gremlin(gremlins.species.clicker().clickTypes(['click']))
        .gremlin(gremlins.species.formFiller())
        .gremlin(gremlins.species.scroller());
        horde.strategy(gremlins.strategies.distribution().delay(25).distribution([0.48, 0.47, 0.05]).randomizer(new Chance(1234)));
        horde.mogwai(gremlins.mogwais.gizmo().maxErrors(-1)); // Prevent Gizmo from stopping the test after 10 js errors
        horde.mogwai(gremlins.mogwais.alert()); // overrides alerts
        horde.seed(1234);
        horde.unleash();
    }
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
