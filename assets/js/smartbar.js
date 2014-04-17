var smartBar;

(function (window, document, undefined) {
    'use strict';

    smartBar = {
        init: function (el, limit) {
            this.root = el;
            this.limit = limit;
            this.isVisible = true;
            this.isLocked = false;
            this.bindEvents();
        },

        bindEvents: function bindEvents() {
            this.bindOver()
                .bindScroll();
        },

        bindOver: function bindOver() {
            var self = this;
            this.root.addEventListener('mouseover', function () {
                self.isLocked = true;
            });
            this.root.addEventListener('mouseout', function () {
                self.isLocked = false;
            });
            return this;
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
                    if (window.pageYOffset > self.limit && !self.isLocked) {
                        if (scrollDirection === 'up' && !self.isVisible) {
                            self.show();
                        } else if (scrollDirection === 'down' && self.isVisible) {
                            self.hide();
                        }
                    }
                    lastScrollTop = window.pageYOffset;
                }, 50);
            });
        },

        getScrollDirection: function getScrollDirection(lastScrollTop) {
            if (window.pageYOffset > lastScrollTop) {
                return 'down';
            }
            return 'up';
        },

        show: function show() {
            this.isVisible = true;
            setTimeout(function () {
                this.root.setAttribute('data-visible', true);
            }.bind(this), 200);
        },

        hide: function hide() {
            this.isVisible = false;
            this.root.setAttribute('data-visible', false);
        }
    };

}(window, document));
