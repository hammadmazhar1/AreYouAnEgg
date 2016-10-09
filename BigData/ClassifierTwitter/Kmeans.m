clear all
close all
clc
A=xlsread('labelled_instances.csv');
Plus=A(1:305,:);
Minus=A(306:end,:);
PlusB=round(Plus(:,2)*10);
%A(2)
b=tabulate(PlusB);
b(:,3)=b(:,3)/sum(b(:,3));
plot(b(:,3),'b')
hold on

MinusB=round(Minus(:,3)*10);
%A(2)
a=tabulate(MinusB);
a(:,3)=a(:,3)/sum(a(:,3));
plot(a(:,3),'r')
%% Real

plot(Plus(:,1),Plus(:,2),'x')
hold on
plot(Minus(:,1),Minus(:,3),'o')

x=0.1:0.1:1;


y=-0.673077+1.92308*x;
hold on 
plot(x,y)


