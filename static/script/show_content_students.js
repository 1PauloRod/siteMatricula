function showContent(id) {
    // Esconder todos os conteúdos
    var contents = document.querySelectorAll('div[id^="content"]');
    
    for (var i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    
    // Mostrar o conteúdo selecionado
    var content = document.getElementById(id);
    if (content) {
        content.style.display = 'block';
    }
}

