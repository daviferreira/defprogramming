var smartBar;!function(i){"use strict";smartBar={init:function(i,t){this.root=i,this.limit=t,this.isVisible=!0,this.isLocked=!1,this.bindEvents()},bindEvents:function(){this.bindOver().bindScroll()},bindOver:function(){var i=this;return this.root.addEventListener("mouseover",function(){i.isLocked=!0}),this.root.addEventListener("mouseout",function(){i.isLocked=!1}),this},bindScroll:function(){var t,e,s=0,n=this;i.addEventListener("scroll",function(){clearTimeout(t),t=setTimeout(function(){e=n.getScrollDirection(s),i.pageYOffset>n.limit&&!n.isLocked?"up"!==e||n.isVisible?"down"===e&&n.isVisible&&n.hide():n.show():i.pageYOffset<n.root.offsetHeight&&n.unglue(),s=i.pageYOffset},100)})},getScrollDirection:function(t){return i.pageYOffset>t?"down":"up"},show:function(){this.isVisible=!0,this.root.setAttribute("data-visible",!0)},hide:function(){this.isVisible=!1,this.root.setAttribute("data-visible",!1)},unglue:function(){this.isVisible=!0,this.root.setAttribute("data-visible","")}}}(window,document);