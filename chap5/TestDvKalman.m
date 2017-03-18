clear all

dt = 0.1;
t = 0:dt:10;

Nsamples = length(t);

Xsaved = zeros(Nsamples, 2);
Zsaved = zeros(Nsamples, 1);
Vsaved = zeros(Nsamples, 1);
for k=1:Nsamples
    [z,V] = GetPos();
    [pos, vel] = DvKalman(z);
    
    Xsaved(k,:) = [pos, vel];
    Vsaved(k) = V;
    Zsaved(k) = z;
end


figure
hold on
plot(t, Zsaved(:),'r.')
plot(t, Xsaved(:,1))

figure
hold on
plot(t, Xsaved(:,2), 'b-')
plot(t, Vsaved(:), 'r-')