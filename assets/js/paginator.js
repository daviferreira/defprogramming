var paginator;

(function (window, document, undefined) {
    'use strict';
    function elementInViewport(el) {
        var top = el.offsetTop,
            left = el.offsetLeft,
            width = el.offsetWidth,
            height = el.offsetHeight;

        while (el.offsetParent) {
            el = el.offsetParent;
            top += el.offsetTop;
            left += el.offsetLeft;
        }

        return (
            top < (window.pageYOffset + window.innerHeight) &&
            left < (window.pageXOffset + window.innerWidth) &&
            (top + height) > window.pageYOffset &&
            (left + width) > window.pageXOffset
        );
    }

    paginator = {
        init: function init() {
            this.currentPage = 1;
            this.isPaginating = false;
            this.maxAutoLoad = 3;
            this.root = document.getElementById('quotes');
            this.loader = document.getElementById('pagination-loader');
            this.bind();
        },

        tplQuote: function tplQuote(data) {
            return '<div class="quote-card">' +
                   '    <q><p>' + data.body + '</p></q>' +
                        this.tplActions(data) +
                        this.tplAuthors(data.authors) +
                        this.tplTags(data.tags) +
                   '</div>';
        },

        tplActions: function tplActions(data) {
            return '<div class="quote-card-actions">' +
                   '    <a href="https://www.facebook.com/sharer/sharer.php?u=http://defprogramming.com' + data.url + '" target="_blank" class="facebook">' +
                   '        <i class="icon icon-facebook"></i>' +
                   '    </a>' +
                   '    <a href="https://twitter.com/home?status=%22' + encodeURI(data.body) + '%22 http://defprogramming.com' + data.url + '" target="_blank" class="twitter">' +
                   '        <i class="icon icon-twitter"></i>' +
                   '    </a>' +
                   '    <a href="https://plus.google.com/share?url=http://defprogramming.com' + data.url + '" target="_blank" class="google-plus">' +
                   '        <i class="icon icon-google-plus"></i>' +
                   '    </a>' +
                   '    <a href="' + data.url + '#comments"><i class="icon icon-comments"></i></a>' +
                   '</div>';
        },

        tplAuthors: function tplAuthors(authors) {
            var html = '<div class="quote-card-author">',
                author;
            if (authors.length > 1) {
                authors.forEach(function (author) {
                    html += '<a href="' + author.url + '">' + author.name + '</a> & ';
                });
                html = html.replace('/& $/', '');
            } else {
                author = authors[0];
                html += '<a href="' + author.url + '">';
                if (author.avatar) {
                    html += '<img src="' + author.avatar + '" class="author-avatar" width="60" height="60">';
                }
                html += '<p>' + author.name + '</p>';
                html += '</a>';
            }
            html += '</div>';
            return html;
        },

        tplTags: function tplTags(tags) {
            var html = '<div class="quote-card-tags">on ';
            tags.forEach(function (tag) {
                html += '<a href="' + tag.url + '">' + tag.name + '</a>, ';
            });
            html = html.replace(/, $/, '');
            html += '</div>';
            return html;
        },

        bind: function bind() {
            var footer = document.getElementsByTagName('footer')[0],
                timer,
                self = this;
            this.scrollHandler = function () {
                clearTimeout(timer);
                timer = setTimeout(function () {
                    if (elementInViewport(footer)) {
                        self.paginate();
                    }
                }, 50);
            };
            window.addEventListener('scroll', this.scrollHandler);
        },

        paginate: function paginate() {
            if (this.isPaginating) {
                return;
            }
            this.lock();
            this.currentPage += 1;
            if (!this.httpRequest) {
                this.createHttpRequest();
            }
            this.httpRequest.open('GET',
                                  '/page/' + this.currentPage + '/format/json/',
                                  true);
            this.httpRequest.send(null);
        },

        lock: function lock() {
            this.isPaginating = true;
            this.loader.style.display = 'block';
            if (this.btn) {
                this.btn.style.display = 'none';
            }
        },

        unlock: function unlock() {
            this.isPaginating = false;
            this.loader.style.display = 'none';
            if (this.btn) {
                this.btn.style.display = 'block';
            }
        },

        createHttpRequest: function createHttpRequest() {
            var self = this,
                data;
            this.httpRequest = new window.XMLHttpRequest();
            this.httpRequest.onreadystatechange = function () {
                if (self.httpRequest.readyState === 4) {
                    if (self.httpRequest.status === 200) {
                        data = JSON.parse(self.httpRequest.responseText);
                        self.root.innerHTML += self.parseQuotes(data.quotes);
                        self.setupNextPage(data.hasNext);
                        setTimeout(function () {
                            self.resetNewCards();
                        }, 300);
                    }
                    self.unlock();
                }
            };
        },

        parseQuotes: function parseQuotes(quotes) {
            var html = '';
            html += '<h3>Page ' + this.currentPage + '</h3>';
            html += '<div class="quote-cards-container single container ' +
                    'quote-cards-container-new">';
            quotes.forEach(function (quote) {
                html += this.tplQuote(quote);
            }.bind(this));
            html += '</div>';
            return html;
        },

        setupNextPage: function setupNextPage(hasNext) {
            if (hasNext && this.currentPage < this.maxAutoLoad) {
                return;
            }
            window.removeEventListener('scroll',
                                       this.scrollHandler);
            if (hasNext) {
                this.createButton();
            } else if (this.btn) {
                this.root.parentNode.removeChild(this.btn);
            }
        },

        createButton: function createButton() {
            if (this.btn) {
                return;
            }
            this.btn = document.createElement('button');
            this.btn.className = 'btn btn-load-more';
            this.btn.innerText = 'load more';
            this.root.parentNode.appendChild(this.btn);
            this.btn.addEventListener('click', function (e) {
                e.preventDefault();
                this.paginate();
            }.bind(this));
        },

        resetNewCards: function resetNewCards() {
            document.querySelector('.quote-cards-container-new')
                        .classList.remove('quote-cards-container-new');
        }
    };
}(window, document));