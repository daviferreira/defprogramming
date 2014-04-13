/*global require*/
var gulp = require('gulp'),
    gutil = require('gulp-util'),
    iconfont = require('gulp-iconfont'),
    iconfontCss = require('gulp-iconfont-css'),
    sass = require('gulp-sass'),
    prefix = require('gulp-autoprefixer'),
    minifyCss = require('gulp-minify-css'),
    concat = require('gulp-concat'),
    livereload = require('gulp-livereload'),
    fontName = 'defprogramming';

gulp.task('iconfont', function(){
    gulp.src(['svgs/*.svg'], {base: ''})
        .pipe(iconfontCss({
            fontName: fontName,
            targetPath: '../../../assets/scss/_icons.scss',
            fontPath: '../fonts/'
        }))
        .pipe(iconfont({
            fontName: fontName, // required
            appendCodepoints: true // recommended option
        }))
        .on('codepoints', function(codepoints, options) {
            // CSS templating, e.g.
            console.log(codepoints, options);
        })
        .pipe(gulp.dest('../defprogramming/static/fonts/'));
});

gulp.task('sass', function () {
    return gulp.src('scss/*.scss')
               .pipe(sass())
               .pipe(gulp.dest('css'));
});

gulp.task('css', ['sass'], function () {
    gulp.src(['css/bootstrap.css', 'css/base.css'])
        .pipe(prefix({cascade: true}))
        .pipe(concat('defprogramming.min.css'))
        .pipe(minifyCss())
        .pipe(gulp.dest('../defprogramming/static/css/'))
        .pipe(livereload());
});

gulp.task('watch', function() {
    var watcher = gulp.watch('scss/**/*.scss', ['css']);
    watcher.on('changed', function(event){
        console.log('File '+event.path+' was '+event.type+', running tasks...');
    });
});

gulp.task('default', ['css', 'watch']);
