load all_data
f = find(all_data(:,2)>-1);
data = all_data(f,:);
thresh = [0.5:0.01:1];
for n=1:51, f=find(data(:,1)>thresh(n)); frc(n)=length(f)/length(data); prf(n) = mean(data(f,2)); end;
plot(thresh , prf)
plot(frc, prf)


f0 = find(data(:,2)==0);
f1 = find(data(:,2)==1);
[p0,a0] = pdf(data(f0,1),50);
[p1,a1] = pdf(data(f1,1),50);
plot(a0,p0,'r'); hold on; plot(a1,p1,'b');