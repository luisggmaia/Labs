from quantity import Quantity

class Ar:

    def __init__(self, T = None, p = None):

        self.T = T # Quantity, temperatura (K)
        self.p = p # Quantity, pressão (Pa)

        self.rho = None
        self.mu = None
        self.nu = None

    def get_rho(self):
        # Equação dos gases ideais, ρ = p/(R·T)

        R = 287.05 # J/(kg·K), constante dos gases ideais para o ar
        self.rho = self.p/(R*self.T) # Quantity, kg/m^3, densidade do ar

        return self.rho

    def get_mu_nu(self):

        # Sutherland, mu = mu_0*(T/T_0)**(1.5)*(T_0 + S)/(T + S)
        mu_0 = 1.7894e-5 # kg/(m·s)
        T_0 = 288.16 # K
        S = 100 # K
        self.mu = mu_0*(self.T/T_0)**1.5*(T_0 + S)/(self.T + S)
        
        # Viscosidade cinemática, nu = mu/rho
        self.nu = self.mu/self.rho

        return self.mu, self.nu

    def read_data(self):
        pass
    
    def print(self):

        print(f'T: {self.T} K')
        print(f'p: {self.p} Pa')
        print(f'rho: {self.rho} kg/m^3')
        print(f'mu: {self.mu} kg/(m·s)')
        print(f'nu: {self.nu} m^2/s')
