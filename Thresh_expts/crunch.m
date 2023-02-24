%load data

f0=find(data(:,2)==0);
f1=find(data(:,2)==1);
fq=find(data(:,2)==-1);

subplot(121),boxplot(data(f0,1),'notch','on'); grid on; axis([.5 1.5 .5 1]); xlabel('FPs');
subplot(122),boxplot(data(f1,1),'notch','on'); grid on; axis([.5 1.5 .5 1]); xlabel('TPs');

