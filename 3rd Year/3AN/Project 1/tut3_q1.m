a=1;
b=4;
N=10;
h=(b-a)/N;
x=(a:h:b)';
h2=h^2;

y=1-1/4*x.^2;
plot(x,y,'r'), hold on

uPrime=[(guess(2)-guess(1))/h;(guess(2:end)-guess(1:end-1))/(2*h);(guess(end)-guess(end-1))/h];
uPrimePrime
g=[-uPrimePrime-1/r];

rhs=[-3*y(1)+4*y(2)-y(3)+h/2;y(1:N-1)-2*y(2:N)+y(3:N+1)-2*h2*y(2:N).^3;...
    2*h*y(N+1)+3*y(N+1)-4*y(N)+y(N-1)-h*8/25];
    
tole=1;
count=1;

d_1=ones(N,1);

while (tole>1.e-7) && (count<20)    
    dd=[0;-2-6*h2*y(2:N).^2;0];
    J=diag(dd,0)+diag(d_1,1)+diag(d_1,-1);
    J(1,1)=-3; J(1,2)=4; J(1,3)=-1;
    J(N+1,N+1)=2*h+3; J(N+1,N)=-4; J(N+1,N-1)=1;
    z=-J\rhs;
    y=y+z;
    rhs=[-3*y(1)+4*y(2)-y(3)+h/2;y(1:N-1)-2*y(2:N)+y(3:N+1)-2*h2*y(2:N).^3;...
    2*h*y(N+1)+3*y(N+1)-4*y(N)+y(N-1)-h*8/25];
    tole=norm(rhs);
    disp([count tole norm(z)])
    plot(x,y),drawnow
    pause(1)
    count=count+1;
end
