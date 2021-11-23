document.addEventListener("DOMContentLoaded", function(){
    const form_horario = document.getElementById("form-horario");
    const titulo = document.getElementById("titulo");
    const accion = document.getElementById("accion");

    form_horario.style.display = "none";

    document.addEventListener("click", event => {
        const element = event.target;
        if (element.id === "horario"){
            titulo.innerHTML = "Saber el horario de mi cita";
            accion.value = "horario";
            form_horario.style.display = "block";
        }
        else if (element.id === "eliminar"){
            titulo.innerHTML = "Eliminar cita";
            accion.value = "eliminar";
            form_horario.style.display = "block";
        }


    })
})