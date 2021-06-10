L = 100;
N = 2000;
tMax = 4000;
S = 0.5;
A1 = 1;
A2 = 1;
x1 = -20;
x2 = 20;
v1 = 5;
v2 = -5;

epsilon = 0.01;

h = L/N;
tau = h^2/3;
s = tau/h^2;
x = (-L/2:h:L/2-h)';
t = linspace(0,tMax*tau,tMax+1);

psi0 = A1.*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1)) + A2.*sech(A2.*(x-x2)).*exp(1i*v2.*(x-x2));
psi = psi0;

A = diag(s/2*ones(N-1, 1), 1) + diag((1i-s)*ones(N, 1), 0) + diag(s/2*ones(N-1, 1), -1);
A(1, N) = s/2;
A(N, 1) = s/2;

B=inv(A);

figure(1)

rhs = zeros(size(x));
initConst = trapz(x, abs(psi).^2);

Z = zeros(tMax+1, N);
format longg
tic
i = 0;
for tt = 1:tMax
    rhs(2:N-1) = -s/2*psi(1:N-2) + (1i + s)*psi(2:N-1) - (2*tau*abs(psi(2:N-1)).^2)./(1+S*sin(abs(psi(2:N-1)).^2)).*psi(2:N-1) - s/2*psi(3:N);
    rhs(1) = -s/2*psi(N) + (1i + s)*psi(1) - (2*tau*abs(psi(1)).^2)/(1+S*sin(abs(psi(1)).^2)).*psi(1) - s/2*psi(2);
    rhs(N) = -s/2*psi(N-1) + (1i + s)*psi(N) - (2*tau*abs(psi(N)).^2)/(1+S*sin(abs(psi(N)).^2)).*psi(N) - s/2*psi(1);
    
%     psi = A\rhs;
    psi=B*rhs;
%     Z(tt, 1:end) = abs(psi);
% 
%     plot(x,abs(psi))
%     ylim([0, 1.5])
%     drawnow
%     const = trapz(x,abs(psi).^2);
end
toc

% disp(initConst-const)
% 
% 
% figure(3)
% h = surf(x,t,Z);
% set(h,'LineStyle','none')
% title('Time evolution of the NLS using Implicit FD')
% xlabel('x')
% ylabel('Time')
% zlabel(texlabel('|psi|'))
% view(-5.475000000000006,73.666079097422624)