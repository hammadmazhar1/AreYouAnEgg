clear all
close all
clc
x=0.1:8;
y=-0.0071*x.^7 + 0.28*x.^6 -4.4*x.^5 + 38*x.^4 -190*x.^3 +530*x.^2 - 790*x+480;
plot(x,y)