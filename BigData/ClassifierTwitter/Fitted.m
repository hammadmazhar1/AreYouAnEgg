%Fitted
x=0.1:0.1:10;
%yFake=0.014*x.^5-0.29*x.^4 + 2.3*x.^3 - 8.5*x.^2 + 14*x -1.7;
yFake = 0.0021*x.^6 - 0.057*x.^5 + 0.62*x.^4 - 3.3*x.^3 + 9.4*x.^2 -13*x +5.9;
for i=1:100
    if yFake(i) < 0 || i < 20
    yFake(i) =0;
    end
end

yFake=yFake/sum(yFake);


yReal=0.0013*x.^5 - 0.053*x.^4 + 0.86*x.^3 -6.3*x.^2 +17*x +6.9;
for i=1:100
    if i > 80
    yReal(i) =yReal(i-1)-0.05;
    end
end
yReal=yReal/sum(yReal);
x=1:100;
plot(x,yFake,'r')
hold on
plot(x,yReal,'b')
xlim([1 100])
ylim([0 max(yFake)])
sum(yReal)
sum(yFake)

%In calculations consider any Fake > max(Real) to be Max(real)
learningRate = 0.01;
w25=1;
w15=1;
w46=1;
w36=1;

net6=w36*o3+w46o4;
o6=1/(1+exp(-net6));

net5=w15*o1+w25o5;
o5=1/(1+exp(-net5));

net7=w57*o5+w67o6;
o7=1/(1+exp(-net7));

w36=(t-o7)+learningRate+(t-o7)*w36;
w46=(t-o7)+learningRate+(t-o7)*w46;
w15=(t-o7)+learningRate+(t-o7)*w15;
w25=(t-o7)+learningRate+(t-o7)*w25;

w57 =(t-o7)+learningRate+(t-o7)*w57;
w67 = (t-o7)+learningRate+(t-o7)*w67;
