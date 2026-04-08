//Ejercicio 1

#include <iostream>
using namespace std;

int main() {
    cout << "Hola, Mundo" <<  endl;

    int edad = 17
    float temperatura = 36.5;
    char inicial = "A";
    bool Estudiante = true 

cout << "Entero: " << edad << endl;
    cout << "Flotante: " << temperatura << endl;
    cout << "Caracter: " << inicial << endl;
    cout << "Booleano: " << esEstudiante << endl;

return 0 ; 
}

//Ejercicio 3

#include <iostream>
using namespace std;

int main() {
    int numeroSecreto = 42;
    int intento = 0; // Inicializamos con un valor diferente al secreto

    cout << "¡Adivina el numero secreto!" << endl;

    // El bucle se repite mientras el intento sea distinto al numero secreto
    while (intento != numeroSecreto) {
        cout << "Ingresa un numero: ";
        cin >> intento;

        if (intento > numeroSecreto) {
            cout << "Mas bajo..." << endl;
        } else if (intento < numeroSecreto) {
            cout << "Mas alto..." << endl;
        }
    }

    // Si sale del bucle, es porque adivinó
    cout << "¡Felicidades! Adivinaste el numero." << endl;

    return 0;
}

