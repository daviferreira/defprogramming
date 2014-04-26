function Sandwich(el) {
    'use strict';
    this.init(el);
}

(function () {
    'use strict';

    Sandwich.prototype = {

        init: function init(el) {
            this.root = el;
            this.setup()
                .bind();
        },

        setup: function setup() {
            this.currentPage = 1;
            this.content = this.root.querySelector('.widget-sandwich-content');
            this.btnUp = this.root.querySelector('.widget-sandwich-up');
            this.btnDown = this.root.querySelector('.widget-sandwich-down');
            this.setupItems();
            return this;
        },

        setupItems: function setupItems() {
            var maxHeight = this.root.querySelector('.widget-sandwich-wrapper').offsetHeight,
                height = 0,
                items = this.content.querySelectorAll('.widget-sandwich-item'),
                i = 0;
            this.totalItems = items.length;
            for (i = 0; i < this.totalItems; i += 1) {
                height += items[i].offsetHeight;
                if (height > maxHeight) {
                    this.itemHeight = items[i].offsetHeight;
                    this.itemsPerPage = i;
                    this.pageHeight = this.itemHeight * this.itemsPerPage;
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
            this.content.style.marginTop = this.getMargin(page) + 'px';
            this.currentPage = page;
            this.setButtonStates();
        },

        getMargin: function getMargin(page) {
            var margin = this.calculateMargin(page),
                pageTotalItems = this.itemsPerPage * page;
            this.isLastPage = false;
            if (pageTotalItems > this.totalItems) {
                this.isLastPage = true;
                return margin + ((pageTotalItems - this.totalItems) * this.itemHeight);
            }
            return margin;
        },

        calculateMargin: function calculateMargin(page) {
            if (page === 1) {
                return 0;
            }
            if (page < this.currentPage) {
                return parseInt(this.content.style.marginTop, 10) + this.pageHeight;
            }
            return -(this.pageHeight * (page - 1));
        },

        setButtonStates: function setButtonStates() {
            this.setButtonState(this.btnUp, this.currentPage === 1);
            this.setButtonState(this.btnDown, this.isLastPage);
        },

        setButtonState: function setButtonState(btn, condition) {
            if (condition) {
                btn.disabled = true;
            } else if (btn.disabled) {
                btn.disabled = false;
            }
        }

    };

}());