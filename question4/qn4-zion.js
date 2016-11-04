function f(s, i) {
  var r = [], m = 0, z = '';

  s.split('').forEach(function (v,k) {
     x = k % i
     r[x] = (r[x] || '') + v
     l = r[x].length
     m = l > m ? l : m
  })

  for (a = 0; a < i; a++) z += r[a] + ' '.repeat(m - r[a].length)

  return z;
}
