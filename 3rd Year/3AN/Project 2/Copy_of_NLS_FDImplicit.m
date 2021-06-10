L=100;
N=2000;
h=L/N;
tau=h^2/3;
tMax=100;
x1=-10;
v1=5;
x2=10;
v2=-5;
A1=1;
A2=1;
S=0.2;
s=tau/h^2;

x=(-L/2:h:L/2-h)';
y=linspace(0,tMax*tau,tMax);
% psi0=((A1*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1)))+(A2*sech(A2.*(x-x2)).*exp(1i*v2.*(x-x2))));
psi=(A1*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1)));

conserved1=trapz(x,abs(psi).^2);
con=zeros(size(y));
con(1)=conserved1;
figure(1)
z=zeros(tMax, N);
z(1,:)=abs(psi);

A = diag(s/2*ones(N-1, 1), 1) + diag((1i-s)*ones(N, 1), 0) + diag(s/2*ones(N-1, 1), -1);

A(1,N)=s/2;
A(N,1)=s/2;

rhs=zeros(size(x));

tic
for tt=1:tMax-1
    rhs(2:N-1) = -s/2*psi(1:N-2) + (1i + s)*psi(2:N-1) - (2*tau*abs(psi(2:N-1)).^2)./(1+S*sin(abs(psi(2:N-1)).^2)).*psi(2:N-1) - s/2*psi(3:N);
    rhs(1) = -s/2*psi(N) + (1i + s)*psi(1) - (2*tau*abs(psi(1)).^2)/(1+S*sin(abs(psi(1)).^2)).*psi(1) - s/2*psi(2);
    rhs(N) = -s/2*psi(N-1) + (1i + s)*psi(N) - (2*tau*abs(psi(N)).^2)/(1+S*sin(abs(psi(N)).^2)).*psi(N) - s/2*psi(1);

    
    psi=A\rhs;
    plot(x,abs(psi)),drawnow

    conserved=trapz(x,abs(psi).^2);
    con(tt+1)=conserved;
    
    z(tt+1,:)=abs(psi);
%     disp( tt )
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
xlabel('x')
ylabel('Time')
zlabel(texlabel('|psi|'))
view(-5.475000000000006,73.666079097422624)