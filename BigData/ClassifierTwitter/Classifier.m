clear all
close all
clc
A=xlsread('FuckedupTables');
B=xlsread('Test.csv');

Output=zeros(length(B),1);
for i = 1:length(B)
test =B(i,:);
RT=round(test(1)*10);
Fr=round(test(2)*10);
Fl=round(test(3)*10);

ProbRR=A(RT+1,2)*A(Fr+1,3);
ProbFF=A(RT+1,2)*A(Fl+1,4);

if ProbRR > ProbFF
    Output(i) = 0;
else
    Output(i) =1;
end
end

sum(Output)