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
    int edad;

    cout << "Ingresa tu edad: ";
    cin >> edad;
    if (edad >= 18) {
        cout << "Eres mayor de edad." << endl;
    } else {
        cout << "Eres menor de edad." << endl;
    }
    return 0;
}

//Ejercicio 5

#include <iostream>
using namespace std;

int main() {
    int numeroSecreto = 42;
    int intento = 0;

    cout << "¡Adivina el numero secreto!" << endl;

    while (intento != numeroSecreto) {
        cout << "Ingresa un numero: ";
        cin >> intento;

        if (intento > numeroSecreto) {
            cout << "Mas bajo..." << endl;
        } else if (intento < numeroSecreto) {
            cout << "Mas alto..." << endl;
        }
    }
    cout << "¡Felicidades! Adivinaste el numero." << endl;

    return 0;
}

//Ejercicio 7

#include <iostream>
using namespace std;

float calcularAreaRectangulo(float base, float altura);

int main() {
    float base, altura;
    cout << "Ingresa la base del rectangulo: ";
    cin >> base;
    cout << "Ingresa la altura del rectangulo: ";
    cin >> altura;
    float area = calcularAreaRectangulo(base, altura);
    cout << "La area del rectangulo es: " << area << endl;
    return 0;
}

//Ejercicio 9

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> ComidaFav;
    string comida;

    cout << "Ingresa tus 3 comidas favoritas: ";

    for (int i = 0; i < 3; i++) {
        cin >> comida;
        ComidaFav.push_back(comida);
    }

    cout << "Tus comidas favoritas son: ";
    for (int i = 0; i < 3; i++) {
        cout << ComidaFav[i] << endl;
    }

    return 0;
}