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
            this.styleTop = '2em';
            this.diffLeft = 15;
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
            var scrollDistance = window.pageYOffset + window.outerHeight,
                containerDistance = this.container.offsetTop +
                                    this.container.offsetHeight;
            if (scrollDistance > containerDistance) {
                this.sticky.style.top = (containerDistance - scrollDistance) +
                                        'px';
            } else if (window.pageYOffset < this.container.offsetTop) {
                this.unglue();
            } else if (scrollDirection === 'up'
                    && this.sticky.style.top !== this.styleTop) {
                this.sticky.style.top = this.styleTop;
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
            this.sticky.style.left = this.container.offsetLeft +
                                     this.diffLeft +
                                     this.container.offsetWidth + 'px';
            this.sticky.style.top = this.styleTop;
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
