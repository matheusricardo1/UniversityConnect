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
    var sidebar = document.getElementById("sidebar");
    if (window.matchMedia("(min-width: 714px)").matches && sidebar.classList.contains("sidebar-show")) {
        var sidebar = document.getElementById("sidebar");
        sidebar.style.display = "none";
        sidebar.classList.toggle("sidebar-show");
        document.getElementById('sidebar-off').style.display = "none";

    }
}

window.addEventListener("DOMContentLoaded", checkScreenWidth);
window.addEventListener("resize", checkScreenWidth);

function updateLanguageURL(linkId) {
    const selectElement = document.getElementById(linkId.replace("lang-link", "lang-options"));
    const selectedValue = selectElement.value;
    const langLink = document.getElementById(linkId);
  
    // Obter a URL atual da tag <a>
    const currentURL = langLink.getAttribute("href");
  
    // Verificar se a URL contém 'en' ou 'pt-br' e alternar entre eles, exceto se já estiver em 'en'
    const newURL = currentURL.includes("en") ? currentURL.replace("en", "pt-br") : currentURL;
  
    // Se a opção selecionada for 'pt-br', definir a URL com 'pt-br'
    if (selectedValue === "pt-br") {
      langLink.setAttribute("href", newURL);
    } else {
      // Caso contrário, a opção selecionada é 'en', definir a URL com 'en'
      langLink.setAttribute("href", currentURL.replace("pt-br", "en"));
    }
  
    // Redirecionar a página para a nova URL
    window.location.href = langLink.getAttribute("href");
  }
  
  
  
  
  







function redirectToLang() {
    const selectElement = document.getElementById("lang-options");
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const selectedValue = selectedOption.value;
    const urlBase = "/set_language/";
  
    if (selectedValue && urlBase) {
      const url = urlBase + selectedValue;
      const langLink = document.getElementById("lang-link");
      langLink.setAttribute("href", url);
     
      setTimeout(function() {
        window.location.href = url
      }, 200);
    }
  }
  


