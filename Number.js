const l1= 9 ;
const l2= 3 ;
const l3= 3;

if (l1 === l2 & l1 ===l3 &l2 === l3){
    console.log("triangulo equilatero");
} else if(l1 === l2|| l1 === l3 || l2 === l3){
    console.log("triangulo isoscele");
}else {
    console.log("triangulo escaleno");
}
