'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var del = require('del');  // Add to package.json
var templateCache = require('gulp-angular-templatecache');
var cleanCSS = require('gulp-clean-css');
// browser-sync
var bs, browserSync;
try {
  bs = require('browser-sync');
}
catch (e) {
  console.log('browser-sync not installed');
}
if (bs) {
  browserSync = bs.create();
}

var app = {
  src: require('./bower.json').appPath || 'static',
  build: 'build',
  moduleName: require('./bower.json').moduleName
};

var paths = {
  scripts: [app.src + '/scripts/**/*.js'],
  styles: [app.src + '/styles/**/*.scss'],
  images: [app.src + '/images/**/*'],
  fonts: [app.src + '/fonts/**/*'],
  views: [app.src + '/views/**/*.html'],
  djangoTemplates: ['./templates/**/*.html'],
  components: [
    'bower_components/jquery/dist/jquery.js',
    'bower_components/fastclick/lib/fastclick.js',
    'bower_components/angular/angular.js',
    'bower_components/angular-animate/angular-animate.js',
    'bower_components/angular-route/angular-route.js',
    'bower_components/lodash/lodash.js',
    'bower_components/js-data/dist/js-data.js',
    'bower_components/js-data-angular/dist/js-data-angular.js',
    'bower_components/js-cookie/src/js.cookie.js'
    //'static/scripts/vendor/**/*.js'
  ]
};

////////////////////////
// Tasks //
////////////////////////

// Clean the build directory
gulp.task('clean', function () {
  return del([app.build]);
});

// SASS
var styles = function () {
  return gulp.src(paths.styles)
    .pipe($.plumber())
    .pipe($.sass({
      outputStyle: 'expanded',
      precision: 10
    }))
    .on('error', $.sass.logError)
    .pipe($.autoprefixer('last 2 versions'))
    .pipe(gulp.dest(app.build + '/styles'));
};

gulp.task('styles', ['clean'], styles);
gulp.task('styles:watch', styles);
gulp.task('styles:watch:reload', ['styles:watch'], function (done) {
  browserSync.reload();
  done();
});

// Vendor scripts
var scriptsVendor = function () {
  return gulp.src(paths.components)
    .pipe($.plumber())
    .pipe($.concat('vendor.js'))
    .pipe(gulp.dest(app.build + '/scripts'));
};

gulp.task('scripts:vendor', ['clean'], scriptsVendor);
gulp.task('scripts:vendor:watch', scriptsVendor);
gulp.task('scripts:vendor:watch:reload', ['scripts:vendor:watch'], function (done) {
  browserSync.reload();
  done();
});

// Angular views
var ngViews = function () {
  return gulp.src(paths.views)
    .pipe(templateCache({
      filename: 'views.js',
      module: app.moduleName,
      root: 'views'}))
    .pipe(gulp.dest(app.build + '/scripts'));
};

gulp.task('ngViews', ['clean'], ngViews);
gulp.task('ngViews:watch', ngViews);

// App scripts
var scriptsApp = function () {
  return gulp.src(paths.scripts.concat([app.build + '/scripts/views.js']))
    .pipe($.plumber())
    .pipe($.ngAnnotate())
    .pipe($.concat('app.js'))
    .pipe(gulp.dest(app.build + '/scripts'));
};

gulp.task('scripts:app', ['clean', 'ngViews'], scriptsApp);
gulp.task('scripts:app:watch', ['ngViews:watch'], scriptsApp);
gulp.task('scripts:app:watch:reload', ['scripts:app:watch'], function (done) {
  browserSync.reload();
  done();
});

// Lint scripts
gulp.task('lint:scripts', function () {
  return gulp.src(paths.scripts)
    .pipe($.jshint('.jshintrc'))
    .pipe($.jshint.reporter('jshint-stylish'));
});

// Copy images
var images = function () {
  return gulp.src(paths.images)
    .pipe(gulp.dest(app.build + '/images'));
};

gulp.task('images', ['clean'], images);
gulp.task('images:watch', images);
gulp.task('images:watch:reload', ['images:watch'], function (done) {
  browserSync.reload();
  done();
});

// Copy fonts
var fonts = function () {
  return gulp.src(paths.fonts)
    .pipe(gulp.dest(app.build + '/fonts'));
};

gulp.task('fonts', ['clean'], fonts);
gulp.task('fonts:watch', fonts);
gulp.task('fonts:watch:reload', ['fonts:watch'], function (done) {
  browserSync.reload();
  done();
});

// Django templates
var templates = function () {
  return gulp.src(paths.djangoTemplates)
    .pipe(gulp.dest(app.build + '/templates'));
};

gulp.task('templates', ['clean'], templates);
gulp.task('templates:watch', templates);
gulp.task('templates:watch:reload', ['templates:watch'], function (done) {
  browserSync.reload();
  done();
});

////////////////////////
// Watch Tasks //
////////////////////////

gulp.task('browser-sync', function () {
  browserSync.init({
    proxy: 'localhost:8000'
  });
});

gulp.task('watch', ['images:watch', 'fonts:watch', 'styles:watch', 'scripts:app:watch', 'scripts:vendor:watch', 'templates:watch', 'browser-sync'], function () {
  gulp.watch(paths.styles, ['styles:watch:reload']);
  gulp.watch(paths.scripts, ['scripts:app:watch:reload']);
  gulp.watch(paths.views, ['scripts:app:watch:reload']);
  gulp.watch(paths.images, ['images:watch:reload']);
  gulp.watch(paths.fonts, ['fonts:watch:reload']);
  gulp.watch(paths.djangoTemplates, ['templates:watch:reload']);
  gulp.watch('gulpfile.js', ['scripts:vendor:watch:reload']);
});

////////////////////////
// Build Tasks //
////////////////////////

gulp.task('scripts:optimize', ['scripts:vendor', 'scripts:app'], function () {
  return gulp.src(app.build + '/scripts/**/*.js')
    .pipe($.uglify())
    .pipe(gulp.dest(function (file) {  // Replace files in place
      return file.base;
    }));
});

gulp.task('styles:optimize', ['styles'], function () {
  return gulp.src(app.build + '/styles/**/*.css')
    .pipe(cleanCSS())
    .pipe(gulp.dest(function (file) {  // Replace files in place
      return file.base;
    }));
});

gulp.task('images:optimize', ['images'], function () {
  return gulp.src(app.build + '/images/**/*')
    .pipe($.imagemin({
        optimizationLevel: 5,  // 0-7.  3 is default.
        progressive: true  // Lossless conversion to progressive
    }))
    .pipe(gulp.dest(function (file) {  // Replace files in place
      return file.base;
    }));
    //.pipe(gulp.dest(app.build + '/images'));
});

gulp.task('templates:optimize', ['templates'], function () {
  return gulp.src(app.build + '/templates/**/*.html')
    .pipe($.htmlmin({collapseWhitespace: true}))
    .pipe(gulp.dest(function (file) {  // Replace files in place
      return file.base;
    }));
});

gulp.task('build', ['fonts', 'images:optimize', 'styles:optimize', 'scripts:optimize', 'templates:optimize']);

gulp.task('default', ['watch']);
