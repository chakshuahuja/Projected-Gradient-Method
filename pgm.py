import functions
import inputf2 as inputfunc
alpha = 0.1

k = 1
x_k = [3,-3]

while (k<100):
    gk = inputfunc.gradf(x_k)
    alpha_times_gk = functions.multiply_sm(gk, alpha)
    x_kplus1 = functions.vector_diff(x_k, alpha_times_gk)
    x_k = functions.rectProj(x_kplus1, inputfunc.rect())
    print x_k
    k += 1

print x_k, inputfunc.f(x_k)

