clear all
close all
clc
A=xlsread('fake_rat_full.csv');
A=A*10;
A=round(A);
%A(2)
b=tabulate(A);
hold on
b(:,3)=b(:,3)/sum(b(:,3));
plot(b(:,3))

B=xlsread('real_rat_full.csv');
B=B*10;
B=round(B);
%A(2)
a=tabulate(B);
a(:,3)=a(:,3)/sum(a(:,3));
hold on
plot(a(:,3),'r')

meanA=mean(A);
meanB=mean(B);
hold on
stem(meanA,40,'b')
stem(meanB,20,'r')
