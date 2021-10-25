L = 30;
N = 5000;
h = L/N;
tau = 0.0025;
tMax = 500;
gamma = 0.25;
h1 = 0.25;
A = 1;
theta = 1;

x = (-L:h:L-h);
y = linspace(0,tMax*tau,tMax);
psi = A.*exp(-1i*theta).*sech(A.*x);

figure(1)
plot(x,abs(psi))
% z = zeros(tMax, N);
% z(1,:) = abs(psi);

n = [0:N/2-1 -N/2:-1].^2;

n = exp(-1i*tau*4*pi^2/L^2*n);
tic
for tt = 1:tMax-1
    psi = psi.*exp(2*abs(psi).^2-1+1i*gamma-h.*conj(psi));
    
    psi = ifft(n.*fft(psi));
    
%     conserved = trapz(x,abs(psi).^2);
%     con(tt+1) = conserved;
    plot(x,abs(psi)),drawnow

%     z(tt+1,:) = abs(psi);
end
toc

figure(1)
plot(x,abs(psi)),drawnow
title('Final State of the waves')
xlabel('x')
ylabel(texlabel('|psi|'))


% 
% figure(2)
% sur = surf(x, y, z);
% set(sur,'LineStyle','none')
% title('Time evolution of the NLS using Split Step')
% xlabel('x')
% ylabel('Time')
% zlabel(texlabel('|psi|'))
% view(-5.475000000000006,73.666079097422624)