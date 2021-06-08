L=100;
N=2000;
h=L/N;
tau=h^2/4;
tMax=8000;
x1=-20;
v1=-5;
x2=20;
v2=5;
A1=0.5;
A2=0.5;
S=0.5;
s=tau/h^2;
clf

x=(-L/2:h:L/2-h);
y=(1:tMax);
psi0=((A1*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1)))+(A2*sech(A2.*(x-x2)).*exp(1i*v2.*(x-x2))))';
psi=zeros(size(psi0));

conserved1=trapz(abs(psi0).^2);
% con=[conserved1];
figure(1)
plot(x,abs(psi0),'r')
hold on
% z=[abs(psi0)];

A=diag((1+1i*s)*ones(N-2,1),0)+diag(-1i*s/2*ones(N-3,1),1)+diag(-1i*s/2*ones(N-3,1),-1);
tic
for tt=1:tMax-1
    psi(1)=0;
    psi(2:N-1)=A\(psi0(2:N-1)+1i*tau/(2*h^2).*(psi0(1:N-2)-2.*psi0(2:N-1)+psi0(3:N))+...
        (2*1i*tau*abs(psi0(2:N-1)).^2.*psi0(2:N-1))./(1+S.*sin(abs(psi0(2:N-1)).^2)));
    psi(N)=0;
    psi0=psi;
    
    conserved=trapz(abs(psi0).^2);
%     con=[con conserved];
    plot(x,abs(psi0)),drawnow
    
%     z=[z abs(psi0)];
end
toc
disp( conserved1-conserved )

% figure(2)
% plot(y,con),drawnow
% title('The Conserved Quantity over time')
% xlabel('Time')
% ylabel('N')
% 
% figure(3)
% sur=surf(y, x, z);
% set(sur,'LineStyle','none')
% title('Time evolution of the NLS using Implicit FD')
% xlabel('Time')
% ylabel('x')
% zlabel(texlabel('|psi|'))