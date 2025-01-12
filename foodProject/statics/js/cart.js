let cart = document.querySelector('.cartTab');
let close = document.querySelector('.close');
let cartOpCl='0';

function cartOpen(){
    if(cartOpCl === '0'){
        cart.style.right='0';
        cartOpCl = '1';
        console.log('working')
    }else{
        cart.style.right='-400px';
        cartOpCl='0';
        console.log('not working')
    }
   
}
function cartClose(){
    cart.style.right='-400px';
    cartOpCl='0';

}