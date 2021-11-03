L = 60;
N = 5000;
h = L/N;
tau = (h^2)/(2*pi);
tMax = 1000;
gamma = 0.25;
h1 = 0.25;
theta = asin(gamma/h1)/2;
A = sqrt(h1*cos(2*theta)+1);
% x1=-20;
% v1=5;
% x2=20;
% v2=-5;
% A1=1;
% A2=1;

x=(-L/2:h:L/2-h);
y = linspace(0,tMax*tau,tMax);
psi = A*exp(-1i*theta).*sech(A.*x);
% psi = ((A1*sech(A1.*(x-x1)).*exp(1i*v1.*(x-x1)))+(A2*sech(A2.*(x-x2)).*exp(1i*v2.*(x-x2))));

figure(1)
plot(x,abs(psi))
xlabel('x')
ylabel(texlabel('|psi|'))

figure(2)
plot(x,abs(psi))

z = zeros(tMax, N);
z(1,:) = abs(psi);
conserved = zeros(tMax);
conserved(1) = trapz(x,abs(psi));

n = [0:N/2-1 -N/2:-1].^2;

n = exp(-1i*tau*4*pi^2/L^2*n);
tic
for tt = 1:tMax-1
    psi = psi.*exp(1i*tau*2*abs(psi).^2);
    y_n = n.*fft(real(psi));
    z_n = n.*fft(imag(psi));
    k_n = 2*pi*N/L;
    omega_n = sqrt((1+k_n.^2).^2 - h1^2);
    alpha_n = sqrt((1+k_n.^2-h)/(1+k_n.^2+h));
    % h^2>(1+k^2)^2
%     A_n = ((y_n-alpha_n.*z_n)/2).*exp(tau.*omega_n) + ((y_n+alpha_n.*z_n)/2).*exp(-tau.*omega_n);
%     B_n = ((z_n-(1/alpha_n).*y_n)/2).*exp(tau.*omega_n) + ((z_n+(1/alpha_n).*y_n)/2).*exp(-tau.*omega_n);
    % h^2<(1+k^2)^2
    A_n = y_n.*cos(tau.*omega_n)+alpha_n.*z_n.*sin(tau.*omega_n);
    B_n = z_n.*cos(tau.*omega_n)-(1/alpha_n).*y_n.*sin(tau.*omega_n);
    
    psi = ifft(exp(-gamma*tau).*(A_n+1i.*B_n));
    
    plot(x,abs(psi)),drawnow

    z(tt+1,:) = abs(psi);
    conserved(tt+1) = trapz(x,abs(psi));
end
toc

figure(2)
plot(x,abs(psi)),drawnow
title('Final State of the waves')
xlabel('x')
ylabel(texlabel('|psi|'))



figure(3)
sur = surf(x, y, z);
set(sur,'LineStyle','none')
title('Time evolution of the PDE')
xlabel('x')
ylabel('Time')
zlabel(texlabel('|psi|'))

figure(4)
plot(y,conserved)
title('The integral over the entire solution')
xlabel('Time')
ylabel('trapz(psi)')