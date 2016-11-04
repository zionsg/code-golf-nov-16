def a n
  if n!=1
    p n
    n=(n%2==0?n**0.5:n**1.5).to_i
    a n
  else p n end
end
