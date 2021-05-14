L=12;
p=0.58318946;
%p=2.1e-10;
y0=[0;p];

t=0:0.1:L;
[t,y]=ode45(@t1q2,t,y0);
plot(t,y(:,1),'r')

function dy=t1q2(t,y)
    n=1;
    phi=y(1);
    dphi=y(2);
    r=t;
    if r>1.1e-4
        dy(1,1)=dphi;
        dy(2,1)=-dphi/r+n^2/r^2*phi-(1-phi^2)*phi;
    else
        dy(1,1)=dphi;
        dy(2,1)=-(1-phi^2)*phi;
        
    end
end