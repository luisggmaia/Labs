# Experimental Data Analysis Utilities

A lightweight Python toolkit for experimental data analysis, uncertainty propagation, and sensor calibration.

This project was developed to support engineering laboratory activities, particularly in aerodynamics and experimental measurements, by providing reusable tools for handling measured quantities, propagating uncertainties, calibrating sensors, and computing derived physical properties.

---

## Features

### Quantity

A class for representing physical quantities with associated uncertainties.

Features include:

* Automatic uncertainty propagation through arithmetic operations;
* Support for scalar values, vectors, and NumPy arrays;
* Mathematical functions with uncertainty propagation:

  * `sin`
  * `cos`
  * `tan`
  * `atan`
  * `exp`
  * `log`
* Comparison operators;
* Convenient manipulation of arrays of uncertain quantities.

### Example

```python
from quantity import Quantity

length = Quantity(10.0, 0.1)
width = Quantity(5.0, 0.05)

area = length * width

print(area)
# 50.0 ± 0.71
```

---

### Sensor

Tools for sensor calibration and measurement conversion.

Features include:

* Polynomial calibration models;
* Weighted Least Squares (WLS) regression;
* Automatic outlier detection and rejection;
* Confidence interval estimation;
* Calibration curve visualization.

### Example

```python
from quantity import Quantity
from sensor import Sensor

sensor = Sensor()

sensor.calibrate(
    q_x,
    q_y,
    degree=1
)

measurement = Quantity(2.5, 0.01)

result = sensor.read(measurement)
```

---

### Air Properties

Utilities for computing atmospheric properties from temperature and pressure measurements.

Implemented models:

* Ideal Gas Law
* Sutherland's Law

Computed quantities:

* Density (ρ)
* Dynamic viscosity (μ)
* Kinematic viscosity (ν)

### Example

```python
from quantity import Quantity
from aed_utils import Ar

air = Ar(
    T=Quantity(298.15, 0.5),
    p=Quantity(101325, 100)
)

rho = air.get_rho()
mu, nu = air.get_mu_nu()
```

---

## Repository Structure

```text
.
├── quantity.py
├── sensor.py
├── aed_utils.py
└── README.md
```

---

## Dependencies

### Required Libraries

* NumPy
* SciPy
* Statsmodels
* Matplotlib

---

## Applications

This toolkit has been used in:

* Experimental Aerodynamics
* Wind Tunnel Data Processing
* Sensor Calibration
* Experimental Mechanics
* Engineering Laboratories
* Measurement Uncertainty Analysis

Although originally developed for aerodynamics experiments, the library is general-purpose and can be applied to a wide range of engineering and scientific measurement problems.

---

## Methodology

The implemented uncertainty calculations are based on first-order uncertainty propagation using partial derivatives. Sensor calibration relies on Weighted Least Squares (WLS) regression, allowing measurements with different uncertainty levels to be appropriately weighted during model fitting.

---

## Future Improvements

Potential extensions include:

* Correlated uncertainty propagation;
* Monte Carlo uncertainty analysis;
* Additional atmospheric models;
* Residual diagnostics for calibration models;
* Unit-aware quantities;
* Packaging and PyPI distribution.

