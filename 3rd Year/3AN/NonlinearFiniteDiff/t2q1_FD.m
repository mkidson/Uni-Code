L=10;
N=100;
h=L/N;
n=1;
x=(0:h:L)';
%phi=0.5*x;
phi=1-exp(-x);
figure(1),plot(x,phi)
phi(1)=0;
phi(N+1)=1;

j=(2:N)'-1;

rhs=(phi(1:N-1)-2*phi(2:N)+phi(3:N+1))...
    +(phi(3:N+1)-phi(1:N-1))./(2*j)-n^2./j.^2.*phi(2:N)...
    +h^2*(1-phi(2:N).^2).*phi(2:N);

accur=1;
iter=1;
while accur>1.e-5 && iter<200
    d_p1=1+2./j(1:N-2);
    d_m1=1-2./j(2:N-1);
    dd=-2-n^2./j.^2+h^2*(1-3*phi(2:N).^2);
    J=diag(dd,0)+diag(d_p1,1)+diag(d_m1,-1);
    epsi=-J\rhs;
    phi(2:N)=phi(2:N)+epsi;
    plot(x,phi)
    rhs=(phi(1:N-1)-2*phi(2:N)+phi(3:N+1))...
    +(phi(3:N+1)-phi(1:N-1))./(2*j)-n^2./j.^2.*phi(2:N)...
    +h^2*(1-phi(2:N).^2).*phi(2:N);
    accur=norm(rhs);
    disp([iter accur])
    pause(0.1)
    iter=iter+1;
end
