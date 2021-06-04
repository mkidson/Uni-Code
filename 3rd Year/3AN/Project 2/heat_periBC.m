L=10;
N=1000;
h=L/N;
j=1:N+1;
x=h*(j-1);
u0=sin(x)';
u=zeros(size(u0));
clf
plot(x,u0,'r')
hold on
ta=0.2;
s=ta/h^2;
A=diag((1+2*s)*ones(N,1),0)+diag(-s*ones(N-1,1),1)...
    +diag(-s*ones(N-1,1),-1);
A(1,N)=-s;
A(N,1)=-s;
B=inv(A);
Tmax=1000;
tic
for k=1:Tmax
   % u(1)=0;
    u(1:N)=A\u0(1:N);
    %u(2:N)=B*u0(2:N);
    %u(N+1)=0;
    u0=u;
    plot(x(1:N),u(1:N),'b'),set(gca,'FontSize',14),drawnow
end
toc
plot(x(1:N),u(1:N),'m','LineWidth',2),set(gca,'FontSize',14)
grid