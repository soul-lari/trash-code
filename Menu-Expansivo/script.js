const bntMenu = document.querySelector('#header nav button');

bntMenu.addEventListener('click', function(){
    const menuExpansivo = document.querySelector('#header nav ul');
    console.log(menuExpansivo.classList);

    // const classes = Array.from(menuExpansivo.classList);

    // if(classes.includes("ativado")){
    //     menuExpansivo.classList.remove("ativado");
    // }else{
    //     menuExpansivo.classList.add("ativado");

    menuExpansivo.classList.toggle("ativado");
    }
);























