/*global window*/

var smartBar;

(function () {
    'use strict';

    smartBar = {
        init: function (el, limit) {
            this.root = el;
            this.limit = limit;
            this.bindScroll();
        },

        bindScroll: function bindScroll() {
            var timer,
                lastScrollTop = 0,
                scrollDirection,
                self = this;
            window.addEventListener('scroll', function () {
                clearTimeout(timer);
                timer = setTimeout(function () {
                    scrollDirection = self.getScrollDirection(lastScrollTop);
                    console.log(scrollDirection);
                    lastScrollTop = window.pageYOffset;
                }, 100);
            });
        },

        getScrollDirection: function getScrollDirection(lastScrollTop) {
            if (window.pageYOffset > lastScrollTop) {
                return 'down';
            }
            return 'up';
        },

        show: function show() {
            this.root.setAttribute('data-visible', true);
        },

        hide: function hide() {
            this.root.setAttribute('data-visible', false);
        }
    };
}());
