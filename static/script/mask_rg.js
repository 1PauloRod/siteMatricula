document.getElementById('mask-rg').addEventListener('input', function (e) {
    let rg = e.target.value.replace(/\D/g, '');
    if (rg.length > 2) {
        rg = rg.substring(0, 2) + '.' + rg.substring(2);
    }

    if (rg.length > 6) {
        rg = rg.substring(0, 6) + '.' + rg.substring(6);
    }
   
    if (rg.length > 10) {
        rg = rg.substring(0, 10) + '-' + rg.substring(10);
    }

    e.target.value = rg;
});