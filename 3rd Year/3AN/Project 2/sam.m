clear
L = 100;
N = 2000;
h = L/N;
tau = h^2/3;
s = tau/h^2;
x = (-L/2:h:L/2-h);
%x = (0:h:L-h)';
tMax = 500;

S = 0.5;
A1 = 1;
A2 = 1;
x1 = 45;
x2 = -45;
v1 = 5;
v2 = -5;

psi0 = A1.*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1))...
    + A2.*sech(A2.*(x-x2)).*exp(1i*v2.*(x-x2));
psi = psi0;

A = diag(s/2*ones(N-1, 1), 1) + diag((1i-s)*ones(N, 1), 0) + diag(s/2*ones(N-1, 1), -1);
A(1, N) = s/2;
A(N, 1) = s/2;

i = 0;
for tt = 1:tMax
    rhs(2:N-1) = -s/2*psi(1:N-2) + (1i + s)*psi(2:N-1) - (2*tau*abs(psi(2:N-1)).^2)./(1+S*sin(abs(psi(2:N-1)).^2)).*psi(2:N-1) - s/2*psi(3:N);
    rhs(1) = -s/2*psi(N) + (1i + s)*psi(1) - (2*tau*abs(psi(1)).^2)./(1+S*sin(abs(psi(1)).^2)).*psi(1) - s/2*psi(2);
    rhs(N) = -s/2*psi(N-1) + (1i + s)*psi(N) - (2*tau*abs(psi(N)).^2)./(1+S*sin(abs(psi(N)).^2)).*psi(N) - s/2*psi(1);
    
    psi = A\rhs;
    disp( [abs(psi(150))] )
    plot(x,abs(psi))
    ylim([0, 1.5])
    %xlim([-15, 15])
    drawnow
    %i = i + 1
    %Const = trapz(x,abs(psi).^2)
end