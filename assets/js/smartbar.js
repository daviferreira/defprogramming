var smartBar;

(function (window, document, undefined) {
    'use strict';

    smartBar = {
        init: function (el, limit) {
            this.root = el;
            this.limit = limit;
            this.isVisible = false;
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
                    // refactor plz
                    if (window.pageYOffset > self.limit) {
                        self.stick();
                        if (scrollDirection === 'up' && !self.isVisible) {
                            self.show();
                        } else if (scrollDirection === 'down' && self.isVisible) {
                            self.hide();
                        }
                    } else if (window.pageYOffset > self.root.offsetHeight) {
                        self.stick();
                    } else {
                        self.unstick();
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
        },

        stick: function stick() {
            if (!this.isSticky) {
                this.root.setAttribute('data-visible', false);
                this.root.setAttribute('data-sticky', true);
                document.body.style.paddingTop = this.root.offsetHeight + 'px';
                this.isSticky = true;
            }
        },

        unstick: function unstick() {
            document.body.style.paddingTop = '';
            this.isSticky = false;
            this.root.setAttribute('data-sticky', false);
            this.root.setAttribute('data-visible', false);
        }
    };
}(window, document));
