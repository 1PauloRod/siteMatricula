document.getElementById('mask-telefone').addEventListener('input', function (e) {
    let number = e.target.value.replace(/\D/g, '');
    
    if (number.length > -1) {
        number = number.substring(0, 0) + '(' + number.substring(0);
    }

    if (number.length > 3) {
        number = number.substring(0, 3) + ')' + number.substring(3);
    }
    
    if (number.length > 3) {
        number = number.substring(0, 4) + ' ' + number.substring(4);
    }

   
   
    e.target.value = number;
});