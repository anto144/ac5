from planAhorro import PlanAhorro
import csv
import os

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []
    
    def Carga(self):
        archivo = open("planes.csv")
        lector = csv.reader(archivo, delimiter=";")
        for fila in lector:
            codigo = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            valor = int(fila[3])
            nuevoplan = PlanAhorro(codigo, modelo, version, valor)
            self.__lista.append(nuevoplan)
        archivo.close()
    
    def Listar(self):
        for i in range(len(self.__lista)):
            print("COD. PLAN: {}".format(self.__lista[i].getCodigo()))
            print("MODELO: {}".format(self.__lista[i].getModelo()))
            print("VERSION: {}".format(self.__lista[i].getVersion()))
            print("Valor: ${}".format(self.__lista[i].getValor()))
            print("".center(20,"-"))   
        return
    
    def opcion1(self, ValorNuevo):

        for i in range(len(self.__lista)):
            print("COD. PLAN: {}".format(self.__lista[i].getCodigo()))
            print("MODELO: {}".format(self.__lista[i].getModelo()))
            print("VERSION: {}".format(self.__lista[i].getVersion()))
            self.__lista[i].modificarValor(ValorNuevo)
            print("Valor actualizado: ${}".format(self.__lista[i].getValor()))
            print("".center(20,"-"))

        return    
    
    def opcion2(self, valorAComparar):
        print("Vehiculos de cuota menor o igual a: {}".format(valorAComparar))
        for i in range (len(self.__lista)):
            valorCuotaPlan = (self.__lista[i].getValor() / self.__lista[i].getCuotas()) + self.__lista[i].getValor()*0.1
            if(valorCuotaPlan <= valorAComparar):
                print("Codigo del plan: {}".format(self.__lista[i].getCodigo()))
                print("Modelo: {}".format(self.__lista[i].getModelo()))
                print("Version: {}".format(self.__lista[i].getVersion()))
                print("Valor de cuota: ${}".format(round(valorCuotaPlan,2)))
                print("".center(20,"-"))

        return

    def opcion3(self):
        for i in range (len(self.__lista)):
            valorCuotaPlan = (self.__lista[i].getValor() / self.__lista[i].getCuotas()) + self.__lista[i].getValor()*0.1
            montoAPagar = valorCuotaPlan * self.__lista[i].getCuotasLicitar()
            print("Codigo del plan: {}".format(self.__lista[i].getCodigo()))
            print("Modelo: {}".format(self.__lista[i].getModelo()))
            print("Version: {}".format(self.__lista[i].getVersion()))
            print("Monto que se debe pagar para licitar el vehículo: ${}".format(round(montoAPagar,2)))
            print("".center(20,"-"))

        return

    def opcion4(self, codigo, cantCuotas):
        plan = self.buscar(codigo)
        if (plan != None):
            plan.modificarCuotasLicitar(cantCuotas)
            print("Cambio realizado con exito")
            print(plan.mostrarCuotasLicitar())
            print("".center(20,"-"))

    def buscar(self,codigo):
        i = 0

        while (self.__lista[i].getCodigo() != codigo):
            i += 1
        if(self.__lista[i].getCodigo() == codigo):
            plan = self.__lista[i]
            print("Plan encontrado")
        else:
            print("Plan no existente")
        return plan