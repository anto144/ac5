class PlanAhorro:
    __codigo = 0
    __modelo = ""
    __version = ""
    __valor = 0
    cantCuotas = 60
    cantCuotaspag = 10

    def __init__(self, codigo, modelo, version, valor):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor

    
    def __str__(self):
        print("Codigo: {}\nModelo: {}\nVersion: {}\nValor: {}\nCantidad de cuotas: {}\nCantidad de cuotas pagadas: {}".format(self.__codigo, self.__modelo, self.__version, self.__valor, self.getCuotas, self.getCuotasLicitar))
    
    def getCodigo(self):
        return self.__codigo
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValor(self):
        return self.__valor
    
    def modificarValor(self,val):
        self.__valor = val
        return 


    @classmethod
    def getCuotas(cls):
        return cls.cantCuotas
    
    @classmethod
    def getCuotasLicitar(cls):
        return cls.cantCuotaspag

    @classmethod
    def modificarCuotasLicitar(cls,cuotas):
        cls.cantCuotaspag =  cuotas
        print("Cambio realizado con exito")
        return
    @classmethod
    def mostrarCuotasLicitar(cls):
        return print("Cuotas necesarias para licitar el vehiculo: {}".format(cls.getCuotasLicitar()))