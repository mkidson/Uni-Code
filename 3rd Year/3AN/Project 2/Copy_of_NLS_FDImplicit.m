L=100;
N=5000;
h=L/N;
tau=0.0025;
tMax=2000;
x1=-20;
v1=5;
x2=20;
v2=-5;
A1=1;
A2=1;
S=0.5;
s=tau/h^2;

x=(-L/2:h:L/2-h)';
y=(1:tMax);
psi0=((A1*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1)))+(A2*sech(A2.*(x-x2)).*exp(1i*v2.*(x-x2))));
psi=zeros(size(psi0));

conserved1=trapz(x,abs(psi0).^2);
con=zeros(size(y));
con(1)=conserved1;
figure(1)
z=zeros(tMax, N);
z(1,:)=abs(psi0);

A=diag((1+1i*s)*ones(N,1),0)+diag(-1i*s/2*ones(N-1,1),1)+diag(-1i*s/2*ones(N-1,1),-1);

rhs=zeros(size(x));

tic
for tt=1:tMax-1
    rhs(2:N-1)=(psi0(2:N-1)+1i*tau/(2*h^2).*(psi0(1:N-2)-2.*psi0(2:N-1)+psi0(3:N))+...
        (2*1i*tau*abs(psi0(2:N-1)).^2.*psi0(2:N-1))./(1+S.*sin(abs(psi0(2:N-1)).^2)));
    rhs(1)=(psi0(1)+1i*tau/(2*h^2).*(psi0(N)-2.*psi0(1)+psi0(2))+...
        (2*1i*tau*abs(psi0(1)).^2.*psi0(1))./(1+S.*sin(abs(psi0(1)).^2)));
    rhs(N)=(psi0(N)+1i*tau/(2*h^2).*(psi0(N-1)-2.*psi0(N)+psi0(1))+...
        (2*1i*tau*abs(psi0(N)).^2.*psi0(N))./(1+S.*sin(abs(psi0(N)).^2)));
    
    psi=A\rhs;
    psi0=psi;
    plot(x,abs(psi0)),drawnow

    conserved=trapz(x,abs(psi0).^2);
    con(tt+1)=conserved;
    
    z(tt+1,:)=abs(psi);
end
toc

disp( conserved1-conserved )

figure(2)
plot(y,con),drawnow
title('Conserved Quantity over time')
xlabel('Time')
ylabel('N')

figure(3)
sur=surf(x, y, z);
set(sur,'LineStyle','none')
title('Time evolution of the NLS using Implicit FD')
xlabel('Time')
ylabel('x')
zlabel(texlabel('|psi|'))