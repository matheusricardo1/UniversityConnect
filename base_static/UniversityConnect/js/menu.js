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

function checkScreenWidth() {
    if (window.matchMedia("(min-width: 684px)").matches) {
      document.getElementById("sidebar").style.display = "none";
      var sidebaroff = document.getElementById('sidebar-off');
      sidebaroff.style.display = 'none';
    }
}

window.addEventListener("DOMContentLoaded", checkScreenWidth);
window.addEventListener("resize", checkScreenWidth);


