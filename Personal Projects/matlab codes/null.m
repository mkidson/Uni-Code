a=0.001;
b=10;
N=5000;
h=(b-a)/N;
n=3;
t=(a:h:b)';

%approximate function u
u=-exp(-t)+1;
du=[1;(u(3:N+1)-u(1:N-1))./(2*h);1];
ddu=[1;(u(3:N+1)-2.*u(2:N)+u(1:N-1))./(h^2);1];

%Boundary conditions
u(1)=0;
u(N+1)=1;

%figure(1),plot(t,u)
tol=1;
iter=1;
while iter<100 && tol>1e-5
    %update du, ddu
    du=[1;(u(3:N+1)-u(1:N-1))./(2*h);1];
    ddu=[1;(u(3:N+1)-2.*u(2:N)+u(1:N-1))./(h^2);1];
    %defining p,q and R
    R=-(ddu+(1./t).*du+(u./(1-u.^2)).*(du.^2-(n^2)./(t.^2))+u.*(1-u.^2));
    p=-((1./t)+2*(u.*du)./(1-u.^2));
    q=-((((1-u.^2)+2*(u.^2))./(1-u.^2).^2).*(du.^2-(n^2)./(t.^2))+1-3.*u.^2);
    rhs = (h^2).*R(2:N);
    
    d_p1=1-(h.*p(2:N-1))./2;
    d_m1=1+(h.*p(3:N))./2;
    dd=-2-(h^2).*q(2:N);
    J=diag(dd,0)+diag(d_p1,1)+diag(d_m1,-1);
    z_r=J\rhs;
    %figure(1),plot(r,u),plot(r,z)
    figure(1),plot(t,u);
    
    % Updating values
    u(2:N)=u(2:N)+z_r;
    tol=norm(rhs);
    %accur=norm(z_r);
    disp([iter tol])
    pause(0.1)
    iter=iter+1;
end
