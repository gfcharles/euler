// Karma configuration
// Generated on Sun Sep 25 2016 12:25:20 GMT-0700 (PDT)

module.exports = function(config) {
  config.set({

    // base path that will be used to resolve all patterns (eg. files, exclude)
    basePath: '',


    // frameworks to use
    // available frameworks: https://npmjs.org/browse/keyword/karma-adapter
    frameworks: ['jasmine'],


    // list of files / patterns to load in the browser
    files: [
      'src/secret.js',
      'src/utils.js',
      'src/euler_framework.js',
      'src/gwu.js',
      'src/primes.js',
      'src/my_math.js',
      'src/roman_numeral.js',
      'src/FileUtils.js',
      'node_modules/big-integer/BigInteger.js',
      'euler065.js',
      // 'euler079.js',
      //'euler144.js',
      'test/TestEulers.js',
      'test/TestMyMath.js',
      'test/TestTea.js',
      'test/TestGwu.js',
      // 'test/TestRomanNumeral.js'
    ],


    // list of files to exclude
    exclude: [
      '**/*-compiled.js'
    ],


    // preprocess matching files before serving them to the browser
    // available preprocessors: https://npmjs.org/browse/keyword/karma-preprocessor
    preprocessors: {
    },


    // test results reporter to use
    // possible values: 'dots', 'progress'
    // available reporters: https://npmjs.org/browse/keyword/karma-reporter
    reporters: ['progress'],


    // web server port
    port: 9876,


    // enable / disable colors in the output (reporters and logs)
    colors: true,


    // level of logging
    // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
    logLevel: config.LOG_INFO,


    // enable / disable watching file and executing tests whenever any file changes
    autoWatch: false,


    // start these browsers
    // available browser launchers: https://npmjs.org/browse/keyword/karma-launcher
    browsers: ['Chrome'],


    // Continuous Integration mode
    // if true, Karma captures browsers, runs the tests and exits
    singleRun: false,

    // Concurrency level
    // how many browser should be started simultaneous
    concurrency: Infinity,

    browserNoActivityTimeout: 10000
  })
}
