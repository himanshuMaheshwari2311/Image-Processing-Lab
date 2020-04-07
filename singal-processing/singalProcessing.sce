//utility function
function [x] = multiply(a, b)
    for i = 1:201    
        x(i) = a(i) * b(i);
    end
endfunction

t =0:0.1:20;
unit_step = ones(1, 201)
ramp = 0.1 * t;                      //k = 0.1 
expo1 = exp(0.2 * t)                //a = 0.2
expo2 = exp(-0.2 * t)               //a = -0.2
sint = sin(t);
cost = cos(t);

/*
subplot(3, 1, 1);
plot(t, unit_step);
xlabel("t", "fontsize", 2);
ylabel("u(t)", "fontsize", 2);
legend("unit step function");
subplot(3, 1, 2);
plot(t, sint, t, cost);
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("sin(t)", "cos(t)");
subplot(3, 1, 3);
plot(t, expo2, t, expo1);
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("e^(at)", "e^(-at)");
*/
/*
plot(t, multiply(ramp, sint)', t, multiply(ramp, cost)', t, multiply(sint, cost)');
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("r(t) * sin(t)", "r(t) * cos(t)", "sin(t) * cos(t)");
*/
/*
plot(t, multiply(expo1, sint)', t, multiply(expo1, cost)', t, multiply(sint, cost)');
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("e^(at) * sin(t)", "e^(at) * cos(t)", "sin(t) * cos(t)");
*/
/*
plot(t, ramp+sint, t, ramp+cost, t, sint+cost);
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("r(t) + sin(t)", "r(t) + cos(t)", "sin(t) + cos(t)");
*/
/*
plot(t, expo2+sint, t, expo2+cost, t, sint+cost);
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("e^(-at) + sin(t)", "e^(-at) + cos(t), sin(t) + cos(t)");
*/
/*
plot(t, multiply(expo1, ramp), t, expo1-ramp, t, expo1+ramp);
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("e^(at) * r(t)", "e^(at) - r(t)", "e^(at) + r(t)");
*/
/*
plot(t, sint+cost+ramp, t, sint-cost+ramp, t, multiply(sint, cost));
xlabel("t", "fontsize", 2);
ylabel("x(t)", "fontsize", 2);
legend("r(t) + sin(t) + cos(t)", "sin(t) - cos(t) + r(t)", "sin(t) * cos(t)");
*/
