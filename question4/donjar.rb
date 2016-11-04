def a t, n
  l=-(-t.length / n * n)
  t+=' '*l
  b=0
  y=''
  l.times {
    b = (b % n + 1) if b >= l
    y+=t[b]
    b+=n
  }
  y
end
