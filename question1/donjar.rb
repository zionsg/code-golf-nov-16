x=$_.split('');x.length.times{j=1;p x.inject(){|a,e|j+=1;a+e*j};x.shift}
