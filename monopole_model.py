import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Time period representing the age of the universe (in billions of years)
t_span = (0, 13.8)
t_eval = np.linspace(t_span[0], t_span[1], 500)

# Initial conditions: matter, radiation, monopole densities
rho_m0 = 0.3  # Matter density parameter
rho_r0 = 0.0001 # Radiation intensity
rho_monopole0 = 0.001  # Magnetic singularity density

# Variation of magnetic monopole density with time
def monopole_decay(t, rho_monopole):
    return -0.1 * rho_monopole / (1 + t)  # Monopolies decay over time

# Differential equation describing the expansion dynamics of the universe
def friedmann(t, y):
    rho_m, rho_r, rho_monopole = y
    drho_m_dt = -3 * rho_m / (1 + t)  # Matter density decreases with scale factor
    drho_r_dt = -4 * rho_r / (1 + t)  # Radiation decreases faster
    drho_monopole_dt = monopole_decay(t, rho_monopole)  # Magnetic monopoles decay over time
    return [drho_m_dt, drho_r_dt, drho_monopole_dt]

# Solution
sol = solve_ivp(friedmann, t_span, [rho_m0, rho_r0, rho_monopole0], t_eval=t_eval)

# Graphic drawing
plt.figure(figsize=(10, 6))
plt.plot(t_eval, sol.y[0], label="Madde Yoğunluğu", color="b")
plt.plot(t_eval, sol.y[1], label="Radyasyon Yoğunluğu", color="g", linestyle="--")
plt.plot(t_eval, sol.y[2], label="Manyetik Tekillik Yoğunluğu", color="r", linestyle=":")
plt.xlabel("Zaman (Milyar Yıl)")
plt.ylabel("Yoğunluk")
plt.title("Manyetik Tekilliklerin Zamanla Evrimi")
plt.legend()
plt.grid(True)
plt.show()
