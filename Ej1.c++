#include <iostream>

class TanqueAgua {
private:
    double capacidadMaxima;
    double nivelActual;

public:
    TanqueAgua(double capacidad) {
        capacidadMaxima = capacidad;
        nivelActual = 0;
    }

    double getCapacidadMaxima() {
        return capacidadMaxima;
    }   
    double getNivelActual() {
        return nivelActual;
    }
    void setNivelActual(double nivel) {
        nivelActual = nivel;
    }
    void aumentarNivel(double cantidad) {
    if (nivelActual + cantidad <= capacidadMaxima) {
        nivelActual += cantidad;
    } else {
        nivelActual = capacidadMaxima;
    }
    std::cout << "El tanque aumenta el nivel a " << nivelActual << std::endl;
}
}:

int main() {
    std::cout << "Iniciando el simulador de un tanque de agua con capacidad de 100 litros." << std::endl;
    TanqueAgua tanque(100);
    double llenador = 15.5

    while (miTanque.getNivelActual() < miTanque.getCapacidadMaxima()) {
        miTanque.aumentarNivel(llenador);
    }

    std::cout << "El tanque se ha llenado al 100%." << std::endl;
    return 0;
}