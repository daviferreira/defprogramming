/*global elementInViewport*/

function Sticker(container, sticky) {
    'use strict';
    this.init(container, sticky);
}

(function () {
    'use strict';

    Sticker.prototype = {

        init: function init(container, sticky) {
            if (!container || !sticky
                    || (container.offsetHeight < sticky.offsetHeight)) {
                return false;
            }
            this.container = container;
            this.sticky = sticky;
            this.bind();
        },

        bind: function bind() {
            var timer,
                lastScrollTop = 0,
                scrollDirection,
                self = this;

            this.scrollHandler = function () {
                clearTimeout(timer);
                timer = setTimeout(function () {
                    scrollDirection = self.getScrollDirection(lastScrollTop);
                    // TODO: scroll + height > footer
                    if (window.pageYOffset >= self.container.offsetTop
                            && !self.isStuck
                            && scrollDirection === 'down') {
                        self.glue();
                    } else if (window.pageYOffset < self.container.offsetTop
                                && self.isStuck) {
                        self.unglue();
                    }
                    lastScrollTop = window.pageYOffset;
                }, 30);
            };

            window.addEventListener('scroll', this.scrollHandler);
        },

        getScrollDirection: function getScrollDirection(lastScrollTop) {
            if (window.pageYOffset > lastScrollTop) {
                return 'down';
            }
            return 'up';
        },

        glue: function glue() {
            this.sticky.style.width = this.sticky.offsetWidth + 'px';
            // TODO: dynamically get the left diff, calculate it right
            this.sticky.style.left = this.container.offsetLeft +
                                     15 +
                                     this.container.offsetWidth + 'px';
            // TODO: dynamically calulate margin top
            this.sticky.style.top = '2em';
            this.sticky.style.position = 'fixed';
            this.isStuck = true;
        },

        unglue: function unglue() {
            this.sticky.style.position = '';
            this.sticky.style.top = '';
            this.sticky.style.left = '';
            this.sticky.style.width = '';
            this.isStuck = false;
        }

    };

}());
