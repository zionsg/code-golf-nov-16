function f(s) {
  var r = '';
  if (s == '') { return r; }
  s.split('').forEach(function (v,k) {
    r += v.repeat(k + 1);
  });
  return r + "\n" + f(s.substring(1));
}
