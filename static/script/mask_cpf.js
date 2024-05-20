document.getElementById('mask-cpf').addEventListener('input', function (e) {
    let cpf = e.target.value.replace(/\D/g, '');
    if (cpf.length > 3) {
        cpf = cpf.substring(0, 3) + '.' + cpf.substring(3);
    }

    if (cpf.length > 7) {
        cpf = cpf.substring(0, 7) + '.' + cpf.substring(7);
    }

    if (cpf.length > 11) {
        cpf = cpf.substring(0, 11) + '-' + cpf.substring(11);
    }
   
    e.target.value = cpf;
});