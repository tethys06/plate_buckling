import tomllib
from pathlib import Path
from dataclasses import dataclass
from scipy import optimize

p = Path('config.toml')
with p.open('rb') as f:
    config = tomllib.load(f)



@dataclass
class Inputs:
    Component: str
    a: float
    b: float
    t: float
    E: float
    Fcy: float
    n: float
    Kc: float
    Fc_cr_initial: float
    loading: str

    def __post_init__(self):

        self.loading = self.loading.lower()

        for variable in self.__dataclass_fields__.keys():
            if not isinstance(self.__dict__[variable],self.__dataclass_fields__[variable].type):
                if isinstance(self.__dict__[variable], str):
                    try: 
                        self.__dict__[variable] = float(self.__dict__[variable])
                    except:
                        raise ValueError(f'Invalid value provided for parameter {variable} = {self.__dict__[variable]}. Expecting {self.__dataclass_fields__[variable].type}')
                elif isinstance(self.__dict__[variable], int):
                    self.__dict__[variable] = float(self.__dict__[variable])
                else:
                    raise TypeError(f'Invalid datatype provided for parameter {variable} = {self.__dict__[variable]}. Expecting {self.__dataclass_fields__[variable].type}')
            
            elif self.__dataclass_fields__[variable].type == float:
                if not self.__validate_numerical_inputs__(self.__dict__[variable]):
                    raise ValueError(f'Invalid value specified for parameter {variable} = {self.__dict__[variable]}. Expecting a nonzero positive value.')

        self.__validate_loading__()

    def __validate_numerical_inputs__(self,value):
        if value > 0:
            return True
        else:
            return False
        
    def __validate_loading__(self):

        supported_loadings = ['compression','shear','bending']

        if self.loading not in supported_loadings:
            raise ValueError(f'Invalid loading specified. Given {self.loading}. Expecting {supported_loadings}')
        

    def plasticity_reduction(self, Fc_cr):

        if self.loading == 'compression':

            eta_c = (1/(1 + (0.002*self.E*self.n/self.Fcy)*(Fc_cr/self.Fcy)**(self.n-1)))**(1/2)

        return eta_c
    

    def __CompressionBucklingObjFunc__(self, Fc_cr):

        return self.Kc*self.plasticity_reduction(Fc_cr)*self.E*(self.t/self.b)**2 - Fc_cr
        
    
    def CompressionBucklingAllowable(self):

        root  = optimize.newton(self.__CompressionBucklingObjFunc__, self.Fc_cr_initial)

        return root
    


