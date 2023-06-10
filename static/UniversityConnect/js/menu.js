function entrar(){
    var sidebar = document.getElementById('sidebar');
    sidebar.style.display = 'block';
    var sidebaroff = document.getElementById('sidebar-off');
    sidebaroff.style.display = 'block';
    sidebar.classList.add("sidebar-show");
}
function sair(){
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.remove("sidebar-show");
    sidebar.style.display = 'none';
    var sidebaroff = document.getElementById('sidebar-off');
    sidebaroff.style.display = 'none';
    
}



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


