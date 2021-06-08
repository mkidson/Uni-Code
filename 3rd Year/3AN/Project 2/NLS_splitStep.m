L=100;
N=5000;
h=L/N;
tau=0.0025;
tMax=8000;
x1=-10;
v1=1;
x2=10;
v2=-1;
A1=1;
A2=1;
S=0;

x=(-L/2:h:L/2-h);
y=linspace(0,tMax*tau,tMax);
psi=(A1*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1)))+(A2*sech(A2.*(x-x2)).*exp(1i*v2.*(x-x2)));

conserved1=trapz(x,abs(psi).^2);
con=zeros(size(y));
con(1)=conserved1;
figure(1)
plot(x,abs(psi))
z=zeros(tMax, N);
z(1,:)=abs(psi);

n=[0:N/2-1 -N/2:-1].^2;

n=exp(-1i*tau*4*pi^2/L^2*n);
tic
for tt=1:tMax-1
    psi=psi.*exp((1i*tau*2*abs(psi).^2)./(1+S.*sin(abs(psi).^2)));
    
    psi=ifft(n.*fft(psi));
    
    conserved=trapz(x,abs(psi).^2);
    con(tt+1)=conserved;
    plot(x,abs(psi)),drawnow

    z(tt+1,:)=abs(psi);
end
toc

figure(1)
plot(x,abs(psi)),drawnow
title('Final State of the waves')
xlabel('x')
ylabel(texlabel('|psi|'))

disp( conserved1-conserved )

figure(2)
plot(y,con),drawnow
title('Conserved Quantity over time')
xlabel('Time')
ylabel('N')

figure(3)
sur=surf(x, y, z);
set(sur,'LineStyle','none')
title('Time evolution of the NLS using Split Step')
xlabel('x')
ylabel('Time')
zlabel(texlabel('|psi|'))
view(-5.475000000000006,73.666079097422624)