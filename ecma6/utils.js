/**
 * Created by gcharles on 3/23/16.
 */
function output(message) {
   $(document.body).append('<div>' + message + '</div>');
}

function outputResult(problem, result) {
   output(`Result for problem ${problem} is <b>${result}</b>`);
}

// Range generator
function* Range(begin, end, interval = 1) {
   for (let i = begin; i <= end; i += interval) {
      yield i;
   }
}

Object.prototype.isIterable = function() {
   return typeof this[Symbol.iterator] === 'function';
};