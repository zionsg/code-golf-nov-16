def a x;y=-100;i=0;x.each_with_index do |n,i|;a=x[i-1]||y;b=x[i+1]||y;y=[y,a,b].max if n==0;end;p y;end
