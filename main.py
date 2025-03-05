import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Modelo SIR
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Parâmetros iniciais
N = 1000       # População total
I0 = 1         # Infectados iniciais
R0 = 0         # Recuperados iniciais
S0 = N - I0    # Suscetíveis iniciais

beta = 0.3     # Taxa de transmissão (probabilidade de infecção por contato)
gamma = 0.1    # Taxa de recuperação (1/duração da infecção)

# Intervalo de tempo (dias)
t = np.linspace(0, 160, 160)

# Condição inicial
y0 = [S0/N, I0/N, R0/N]

# Resolver equações diferenciais
sol = odeint(sir_model, y0, t, args=(beta, gamma))
S, I, R = sol.T

# Plotar os resultados
plt.figure(figsize=(10, 5))
plt.plot(t, S, label="Suscetíveis", color="blue")
plt.plot(t, I, label="Infectados", color="red")
plt.plot(t, R, label="Recuperados", color="green")
plt.xlabel("Dias")
plt.ylabel("Proporção da População")
plt.title("Simulação do Modelo SIR")
plt.legend()
plt.grid()
plt.show()
