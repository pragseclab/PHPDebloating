// ==UserScript==
// @name     pma_440_FormFuzzer
// @version  1
// @grant    none
// @include  http://localhost:8085/phpMyAdmin-4.4.0-all-languages/*
// @require  https://raw.githubusercontent.com/marmelab/gremlins.js/master/gremlins.min.js
// ==/UserScript==


var checkForAjax = false;

function setCookies() {
    setCookie('test_group','pma440_form_fuzzer', 1, '/phpMyAdmin-4.4.0-all-languages');
    setCookie('test_name','pma440_form_fuzzer', 1, '/phpMyAdmin-4.4.0-all-languages');
    setCookie('software_id','1', 1, '/phpMyAdmin-4.4.0-all-languages');
    setCookie('software_version_id','2', 1, '/phpMyAdmin-4.4.0-all-languages');
}

$( document ).ajaxSuccess(function() {
    if (horde && checkForAjax) {
        console.log('Ajax call reloaded the page, restarting Gremlins');
        horde.stop();
        var selected_form_info = selectForm();
        if (selected_form_info) {
            var selected_form = selected_form_info[0];
            var selected_form_id = selected_form_info[1];
            fuzzForm(selected_form, selected_form_id);
        }
        else {
          console.log('No forms to fuzz');
          // Run clicker gremlins
          runClicker();
        }
    }
});
$(document).ready(function(){
    $( 'a' ).each(function() {
        if( location.hostname === this.hostname || !this.hostname.length ) {
            // Link to localhost
            //$(this).addClass('local');
        } else { // Link to outside websites
            try {
                $(this).removeAttr("href");
            }
            catch(err) {
                console.log('External link already removed');
            }
        }
        if(this.href.indexOf('logout') !== -1){ // Remove logout link
          try {
              $(this).empty();
          }
          catch(err) {
              console.log('Logout button already removed');
          }
        }
    });

    setCookies();

    var selected_form_info = selectForm();
    if (selected_form_info) {
        var selected_form = selected_form_info[0];
        var selected_form_id = selected_form_info[1];
        fuzzForm(selected_form, selected_form_id);
    }
    else {
      console.log('No forms to fuzz');
      // Run clicker gremlins
      runClicker();
    }
});

function selectForm() {
    let forms = $('form:visible');
    let key = window.location.href;
    let form_ids = localStorageReadArray(localStorage.getItem(key));
    if (!form_ids) {
        form_ids = [];
    }
    //console.log(form_ids);
    if (forms.length - form_ids.length > 0) {
        let rand = selectRandomForm(forms.length);
        do {
            rand = selectRandomForm(forms.length);
        }
        while (form_ids.includes(rand));

        let selected_form = forms[rand];
        //console.log(selected_form);
        return [selected_form, rand];
    }
    else {
        console.log('All forms are already covered');
        return null;
    }
}

function selectRandomForm(forms_length) {
    return chance.integer({ min: 0, max: forms_length - 1 });
}

function fuzzForm(form, form_id) {
    horde = gremlins.createHorde()
    .gremlin(gremlins.species.formFiller().canFillElement(function(element) { return $(form).has($(element)); }).maxNbTries(1000));
    horde.strategy(gremlins.strategies.distribution().delay(25));
    horde.mogwai(gremlins.mogwais.gizmo().maxErrors(-1)); // Prevent Gizmo from stopping the test after 10 js errors
    horde.mogwai(gremlins.mogwais.alert()); // overrides alerts
    horde.seed(1234);
    console.log('UNLEASH THEM MONKEEEYS!');
    checkForAjax = false;
    var count = 0;
    horde.gremlin(function() {
        count++;
        if (form.length > 0) {
            if(count >= 100) {
                horde.stop();
                let key = window.location.href;
                let form_ids;
                if(!localStorage.getItem(key)){
                    form_ids = [form_id];
                }
                else {
                    form_ids = localStorageReadArray(localStorage.getItem(key));
                    if (form_ids.includes(form_id)) {
                        console.log('Form already submitted');
                        horde.stop();
                        runClicker();
                    }
                    else {
                        form_ids.push(form_id);
                    }
                }
                localStorage.setItem(key, form_ids);
                try {
                    $(document.body).append(form);
                    form.submit();
                    checkForAjax = true;
                }
                catch(err) {
                    console.log(err);
                    horde.stop();
                    runClicker();
                }
            }
        }
        else {
            horde.stop();
        }
    });
    horde.unleash({nb: 180000}); // Run for 0.5 hour
}

function runClicker() {
    horde = gremlins.createHorde()
    .gremlin(gremlins.species.clicker().clickTypes(['click']))
    .gremlin(gremlins.species.scroller());
    horde.strategy(gremlins.strategies.distribution().delay(100).distribution([0.90, 0.1]));
    horde.mogwai(gremlins.mogwais.gizmo().maxErrors(-1)); // Prevent Gizmo from stopping the test after 10 js errors
    horde.mogwai(gremlins.mogwais.alert()); // overrides alerts
    horde.seed(1234);
    horde.unleash({nb: 180000}); // Run for 0.5 hour
    checkForAjax = true;
}

function localStorageReadArray(value) {
    // Convert string to array of ints "1,2,3" -> [1,2,3]
    if (value) {
        return value.split(',').map(function(item) {
            return parseInt(item, 10);
        });
    }
    else {
        return null;
    }
}

function setCookie(name,value,days, path) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=" + path;
}
