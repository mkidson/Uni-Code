a=1;
b=4;
p=0.4;
y0=[p;-1/4;1;0];
tar=1;
counter=1;
while abs(tar)>1.e-10 && counter<=55
    [t,y]=ode45(@newtonshoot,[a:0.1:b],y0);
    figure(1),plot(t,y(:,1))
    tar=abs(y(end,1)+y(end,2)-4/25);
    disp([counter p tar])
    figure(1),plot(t,y(:,1))
    pause
    p=p-(y(end,1)+y(end,2)-4/25)/(y(end,3)+y(end,4));
    y0=[p;-1/4;1;0];
    counter=counter+1;
end
figure(2),plot(t,abs(y(:,1)-1./(t+1)))
function [dy]=newtonshoot(t,y)
    v=y(2);
    z=y(3);
    w=y(4);
    
    dy(1,1)=v;
    dy(2,1)=2*y(1)^3;
    dy(3,1)=w;
    dy(4,1)=6*y(1)^2*z;
end