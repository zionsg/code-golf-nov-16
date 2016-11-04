function f(x) {
  var r = [], l = x.length;
  x.forEach(function (v,k,a) {
    if (v == 0) {
      if (k > 0) r.push(a[k-1]);
      if (k < l - 1) r.push(a[k+1]);
    }
  });
  return Math.max(...r);
}
