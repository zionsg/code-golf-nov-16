let f = Math.floor
let p = Math.pow
let x = k => k != 1 ? k + ' ' + (k % 2 == 0 ? x(f(p(k, 0.5))) : x(f(p(k, 1.5)))) : 1