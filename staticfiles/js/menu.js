function entrar(){
    var sidebar = document.getElementById('sidebar');
    sidebar.style.display = 'block';
    var sidebaroff = document.getElementById('sidebar-off');
    sidebaroff.style.display = 'block';

}
function sair(){
    var sidebar = document.getElementById('sidebar');
    sidebar.style.display = 'none';
    var sidebaroff = document.getElementById('sidebar-off');
    sidebaroff.style.display = 'none';
    
}

document.addEventListener("DOMContentLoaded", function() {
    var menuBtn = document.getElementById("home-linkstyle-menu");
    var sidebar = document.getElementById("sidebar");
    var sidebarOff = document.getElementById("sidebar-off");

    function toggleSidebar() {
        sidebar.classList.toggle("sidebar-show");
    }

    menuBtn.addEventListener("click", toggleSidebar);
    sidebarOff.addEventListener("click", toggleSidebar);
  });

window.onscroll = function arrowOff(){
    var arrow = document.getElementById('arrow');
    arrow.style.display ='none';
}

function checkScreenWidth() {
    if (window.matchMedia("(min-width: 684px)").matches) {
      document.getElementById("sidebar").style.display = "none";
      var sidebaroff = document.getElementById('sidebar-off');
      sidebaroff.style.display = 'none';
    }
}

window.addEventListener("DOMContentLoaded", checkScreenWidth);
window.addEventListener("resize", checkScreenWidth);


document.getElementById('theme-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    this.submit(); // Envia o formulário programaticamente
});

window.onbeforeunload = function() {
    // Limpa o evento de submissão do formulário para evitar o alerta de confirmação
    document.getElementById('theme-form').removeEventListener('submit', preventUnloadAlert);
};

function preventUnloadAlert() {
    // Retorna uma string vazia para evitar o alerta de confirmação
    return '';
}

document.getElementById('theme-form').addEventListener('submit', preventUnloadAlert);
