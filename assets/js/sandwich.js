function Sandwich(el, list) {
    'use strict';
    this.init(el, list);
}

(function () {
    'use strict';

    Sandwich.prototype = {

        init: function init(el, list) {
            this.root = el;
            this.list = list;
            this.btnUp = this.root.querySelector('.widget-sandwich-up');
            this.btnDown = this.root.querySelector('.widget-sandwich-down');
            this.setup()
                .bind();
        },

        setup: function setup() {
            return this;
        },

        bind: function bind() {
            return;
        }

    };

}());