def a x
  i=0
  y=nil
  x.each do
    a=x[i-1]||y
    b=x[i+1]||y
    (y||y=a)&&y=[y,a,b].max if x[i]==0
    i+=1
  end
  p y
end
