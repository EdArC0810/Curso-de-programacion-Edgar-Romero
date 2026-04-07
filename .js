//Ejercicio1

const Prducto = "Tablet 10 Pulgadas";
let precio = 450.99;
let stock = 25;
const EnvioGratis = true;

console.log("Nombre del producto: " + Prducto);
console.log("Precio: $" + precio);
console.log("Cantidad disponible: " + stock);
console.log("¿Tiene envío gratis?: " + EnvioGratis);

//Ejercicio2

let cantidad = 3;
let subtotal = precio * cantidad;
let = impuesto = subtotal * 0.07;
let total = subtotal + impuesto;

console.log("El subtotal es: $" + subtotal.toFixed(2));
console.log("El total a pagar, con un 7% impuesto, es: $" + total.toFixed(2));

//Ejercicio3

let edad = 20

if (edad >= 18) {
    console.log("Puedes obtener una licencia de conducir.");
} else {
    console.log("Aun no puedes obtener una licencia de conducir.");
}

//Ejercicio4

let semaforo = "verde";

if (semaforo === "verde") {
    console.log("Puede manejar con normalidad.");
} else if (semaforo === "amarillo") {
    console.log("Precaución, reduce la velocidad y maneja con cuidado.");
} else if (semaforo === "rojo") {
    console.log("Detente, no puedes avanzar.");
} else {
    console.log("Color de semáforo no reconocido.");
}

//Ejercicio5

let dia = 3;
switch (dia) {
    case 1:
        console.log("Hoy es lunes. Hoy tenemos lentejas.");
        break;
    case 2:
        console.log("Hoy es martes. Hoy tenemos Pollo al Horno.");
        break;
    case 3:
        console.log("Hoy es miercoles. Hoy tenemos Pescado a la plancha.");
        break;
    case 4:
        console.log("Hoy es jueves. Hoy tenemos Pasta.");
        break;
    case 5:
        console.log("Hoy es viernes. Hoy tenemos Paella.");
        break;
    default:
        console.log("Día no válido.");
}

//Ejercicio6

for (let i = 1; i <= 10; i++) {
    console.log(i);
}

//Ejercicio7

let contador = 10;
while (contador >= 1) {
    console.log(contador);
    contador = contador - 1;
}

console.log("¡Despegue!");

//Ejercicio8

for (let i = 1; i <= 5; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }

//Ejercicio9

let suma = 0;
for (let i = 1; i <= 100; i++) {
    suma += i;
}

console.log("La suma de los números del 1 al 100 es: " + suma);

//Ejercicio10

let edadUsuario = 19;
let entradaValida = false;

if (edadUsuario >= 18 && entradaValida) {
    console.log("Puedes ingresar al evento.");
} else {
    console.log("No puedes ingresar al evento.");
}