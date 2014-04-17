var mobileMenu;

(function (window, document, undefined) {
    'use strict';

    mobileMenu = {
        init: function init() {
            this.root = document.getElementById('masthead');
            this.toggler = document.getElementById('menu-toggler');
            this.isActive = false;
            this.bind();
        },

        bind: function bind() {
            var self = this;
            this.toggler.addEventListener('click', function (e) {
                e.preventDefault();
                self.root.classList.toggle('menu-active');
                self.isActive = !self.isActive;
            });
        }
    };

}(window, document));
