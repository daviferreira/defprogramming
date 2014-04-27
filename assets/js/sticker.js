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
            this.isStuck = false;
            this.bind();
        },

        bind: function bind() {
            var timer,
                lastScrollTop = 0,
                self = this;

            this.scrollHandler = function () {
                clearTimeout(timer);
                timer = setTimeout(function () {
                    self.check(lastScrollTop);
                    lastScrollTop = window.pageYOffset;
                }, 20);
            };

            window.addEventListener('scroll', this.scrollHandler);
        },

        check: function check(lastScrollTop) {
            var scrollDirection = this.getScrollDirection(lastScrollTop);
            if (this.isStuck) {
                this.checkStuck(scrollDirection);
            } else  if (window.pageYOffset >= this.container.offsetTop
                    && scrollDirection === 'down') {
                this.glue();
            }
        },

        checkStuck: function checkStuck(scrollDirection) {
            if (window.pageYOffset + window.outerHeight > this.container.offsetTop + this.container.offsetHeight) {
                this.sticky.style.top = ((this.container.offsetTop + this.container.offsetHeight) - (window.pageYOffset + window.outerHeight)) + 'px';
            } else if (window.pageYOffset < this.container.offsetTop) {
                this.unglue();
            } else if (scrollDirection === 'up' && this.sticky.style.top !== '2em') {
                this.sticky.style.top = '2em';
            }
        },

        getScrollDirection: function getScrollDirection(lastScrollTop) {
            if (window.pageYOffset >= lastScrollTop) {
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
