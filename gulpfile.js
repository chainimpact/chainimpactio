var gulp = require('gulp');
var bs = require('browser-sync').create(); // create a browser sync instance.

var changed = require('gulp-changed');
var imagemin = require('gulp-imagemin');

// var imagemin = require('gulp-imagemin');
// var imageminJpegtran = require('imagemin-jpegtran');
// var imageminPngquant = require('imagemin-pngquant');

gulp.task('browser-sync', function() {
    bs.init({
        server: {
            baseDir: "./"
        }
    });
});

gulp.task('imagemin', function() {
    var imgSrc = 'assets/img/*.+(png|jpg|jpeg|gif)'
    var imgDist = 'build/images';

    gulp.src(imgSrc)
    .pipe(changed(imgDist))
    .pipe(imagemin())
    .pipe(gulp.dest(imgDist));

});

gulp.task('default', ['imagemin'],function(){
});
