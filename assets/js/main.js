/*global Modernizr, mobileMenu, smartBar*/

(function (window, document, undefined) {
    'use strict';

    if (!Modernizr.touch) {
        smartBar.init(document.getElementById('masthead'), 200);
    } else if (document.documentElement.offsetWidth < 768) {
        mobileMenu.init();
    }

    var credits = document.getElementById('credits'),
        overlay = document.getElementById('overlay');
    document.getElementById('lnk-love').addEventListener('click', function (e) {
        e.preventDefault();
        overlay.style.display = credits.style.display = 'block';
    });

    overlay.addEventListener('click', function (e) {
        if (e.target.id === 'overlay') {
            overlay.style.display = credits.style.display = 'none';
        }
    });
}(window, document));
