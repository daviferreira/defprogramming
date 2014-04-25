function Sandwich(el, list) {
    'use strict';
    this.init(el, list);
}

(function () {
    'use strict';

    Sandwich.prototype = {

        init: function init(el, list) {
            this.root = el;
            this.setup()
                .bind();
        },

        setup: function setup() {
            this.currentPage = 1;
            this.content = this.root.querySelector('.widget-sandwich-content');
            this.btnUp = this.root.querySelector('.widget-sandwich-up');
            this.btnDown = this.root.querySelector('.widget-sandwich-down');
            this.calculatePageHeight();
            return this;
        },

        calculatePageHeight: function calculatePageHeight() {
            var maxHeight = this.root.querySelector('.widget-sandwich-wrapper').offsetHeight,
                height = 0,
                items = this.content.querySelectorAll('.widget-sandwich-item'),
                i = 0;
            for (i = 0; i < items.length; i += 1) {
                height += items[i].offsetHeight;
                if (height > maxHeight) {
                    this.pageHeight = height - items[i].offsetHeight;
                    return;
                }
            }
        },

        bind: function bind() {
            this.btnDown.addEventListener('click', function (e) {
                e.preventDefault();
                this.paginate(this.currentPage + 1);
            }.bind(this));

            this.btnUp.addEventListener('click', function (e) {
                e.preventDefault();
                this.paginate(this.currentPage - 1);
            }.bind(this));
            return;
        },

        paginate: function paginate(page) {
            this.content.style.marginTop = -(this.getPageHeight(page)) + 'px';
            this.currentPage = page;
            this.setButtonStates();
        },

        getPageHeight: function getPageHeight(page) {
            var height = (this.pageHeight * page) - this.pageHeight;
            this.isLastPage = false;
            if (height > this.content.offsetHeight) {
                this.isLastPage = true;
                return height - this.root.offsetHeight - 20;
            }
            return height;
        },

        setButtonStates: function setButtonStates() {
            if (this.currentPage === 1) {
                this.btnUp.disabled = true;
            } else if (this.btnUp.disabled) {
                this.btnUp.disabled = false;
            }
            if (this.isLastPage) {
                this.btnDown.disabled = true;
            } else if (this.btnDown.disabled) {
                this.btnDown.disabled = false;
            }
        }

    };

}());