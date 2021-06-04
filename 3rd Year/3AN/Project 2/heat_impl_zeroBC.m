L=10;
N=100;
h=L/N;
j=1:N+1;
x=h*(j-1);
u0=sin(x)';
u=zeros(size(u0));
clf
plot(x,u0,'r')
hold on
ta=2*h^2;
s=ta/h^2;
A=diag((1+2*s)*ones(N-1,1),0)+diag(-s*ones(N-2,1),1)...
    +diag(-s*ones(N-2,1),-1);
B=inv(A);
Tmax=1000;
tic
for k=1:Tmax
    u(1)=0;
    %u(2:N)=A\u0(2:N);
    u(2:N)=B*u0(2:N);
    u(N+1)=0;
    u0=u;
    plot(x,u,'b'),set(gca,'FontSize',14),drawnow
end
toc
plot(x,u,'m','LineWidth',2),set(gca,'FontSize',14)
grid