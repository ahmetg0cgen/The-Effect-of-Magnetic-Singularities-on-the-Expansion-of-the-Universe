# The-Effect-of-Magnetic-Singularities-on-the-Expansion-of-the-Universe
This project aims to create a simplified cosmological system that models how magnetic singularities affect the expansion of the universe.

Modern cosmology predicts that magnetic singularities may have formed during the Big Bang, but cannot be observed today. This "magnetic monopole problem" occupies an important place in grand unified theories (GUT).

In this project, we will try to understand why magnetic monopoles are missing from today's observations by modeling their evolution over time.

## 📌 Features
✅ A structure that models how magnetic monopoles disappear in cosmological evolution has been created.

✅ Changes in matter, radiation and monopole densities over time were analyzed.

✅ The resulting graph shows how monopoles were dominant in the early universe but decreased over time.

## 🔧 Requirements
📌 Python 3.x

📌 NumPy

📌 Matplotlib

📌 SciPy

For installation:

`pip install numpy matplotlib scipy`

## 📊 Model Description
In this model:

- Matter density decreases inversely proportional to the scale factor.
- Radiation intensity decreases more rapidly and becomes dominant in the early universe.
- Magnetic monopoles decay over time and become unobservable.
- The components of the universe were analyzed by modeling with differential equations.

**Significant changes may need to be made to variables within the code to obtain final, effective and accurate graphs!**

### 🌌 Theoretical Background
#### 🔹 1. Energy Components of the Universe

The density of the universe basically consists of three main components:

-**Matter Density ($\rho_m$):** Varies as $\rho_m \propto a^{-3}$ depending on the scale factor ($a$).

-**Radiation Density ($\rho_r$):** Varies as $\rho_r \propto a^{-4}$, meaning radiation dilutes faster as the universe expands.

-**Magnetic Singularity Density ($\rho_{mon}$):** If the monopole density has a decay process, it will decrease over time.

Density changes during the expansion process can be determined using the Friedmann equation:

$$
H^2 = \frac{8 \pi G}{3}(\rho_m + \rho_r + \rho_{mon})
$$

Here $H$ is the Hubble parameter and determines the expansion rate of the universe.

#### 🔹 2. Evolution of Magnetic Singularities

Since magnetic monopoles are heavy particles, they will be rapidly diluted in the expanding universe. However, they could survive in the early universe.

In this project, we express the decrease in monopoly density over time with the following model:

$$
\frac{d \rho_{mon}}{dt} = - \frac{\lambda \rho_{mon}}{1+t}
$$

Here $\lambda$ is a decay coefficient and describes the decrease of monopole density with the age of the universe.

## 🚀 Operation
To run the project:

`python monopole_model.py`

## 📈 Output
When the code is run, a graph will be created showing the change of matter, radiation, and magnetic monopoles over time.

## 🔍 Advanced Development Suggestions
- We can detail how magnetic monopoles decay in the context of particle physics.
- Within the framework of general relativity, we can examine the effect of the existence of monopoles on the expansion rate.
- We can test the roles magnetic singularities may play in alternative expansion scenarios.

#### 📢 Contribute!
If you would like to contribute to the project, you can open a pull request or share your suggestions.
