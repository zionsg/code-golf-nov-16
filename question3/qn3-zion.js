function f(x) {
  var r = x+''
  if (x == 1) return x
  if (0 == x % 2) {
    r+=','+f(Math.floor(Math.sqrt(x)))
  } else {
    r+=','+f(Math.floor(Math.sqrt(x*x*x)))
  }
  return r;
}
