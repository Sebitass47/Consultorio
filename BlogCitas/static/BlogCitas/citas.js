document.addEventListener("DOMContentLoaded", function(){

    const form_registro = document.getElementById("registro");
    const form_cita = document.getElementById("fecha-cita");
    const horario_cita = document.getElementById("horario-cita");
    const alert_success = document.getElementById("alert-success");
    const alert_danger = document.getElementById("alert-danger");

    form_registro.style.display = "none";
    form_cita.style.display = "none";
    horario_cita.style.display = "none";

    alert_success.style.display = "none";
    alert_danger.style.display = "none";

    document.addEventListener("click", event => {
        const element = event.target;
        if (element.id === "primera_cita"){
            form_registro.style.display = "block";
            form_cita.style.display = "none";
            horario_cita.style.display = "none";
            registro();
        }
        else if (element.id === "paciente_recurrente"){
            form_cita.style.display = "block";
            form_registro.style.display = "none";
        }
        else if (element.id === "fecha_cita"){
            horarios()
        }
    });


})


function registro(){

    document.querySelector("#registro").onsubmit = function(){
        let nombre = document.querySelector("#nombre").value;
        const correo = document.querySelector("#correo").value;
        const fecha_nacimiento = document.querySelector("#fecha_nacimiento").value;
        const genero = document.querySelector("#genero").value;
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const request = new Request(
            "/registro",
            {headers: {'X-CSRFToken': csrftoken}}
        );

        fetch(request,{
            method: "POST",
            mode: "same-origin",
            body: JSON.stringify({
                nombre: nombre,
                correo: correo,
                fecha_nacimiento : fecha_nacimiento,
                genero : genero
            })
        })
        .then(res => res.json())
        .then(res => {
            if (res.success){
                console.log("Usuario creado")
                alertas("success", res.success)
                document.getElementById("registro").style.display = "none";
                document.getElementById("fecha-cita").style.display = "block";
                document.getElementById("correo_registrado").value = correo;
            }
            else{
                console.log(res.error);
                alertas("danger", res.error);
            }
        })
        return false;
    }
}

function horarios(){

    document.getElementById("fecha_cita").onchange = function(){
        
        var x = document.getElementById("horario_cita");
        if (x.length > 1) {

            for(var i = x.length; i >= 2; i--){
                x.remove(i-1);
            } 
           
        }

        const fecha = document.getElementById("fecha_cita").value;
        fetch(`/horarios/${fecha}`)
        .then(res => res.json())
        .then(res => {
            document.getElementById("horario-cita").style.display = "block";
            res.horarios.forEach(horario => {
                const option = document.createElement('option');
                option.innerHTML = horario;
                option.value = horario;
                document.getElementById("horario_cita").append(option);
            })
        })
    }
}



function alertas(tipo, mensaje){
    
    const alert_success = document.getElementById("alert-success");
    const alert_danger = document.getElementById("alert-danger");

    alert_success.style.display = "none";
    alert_danger.style.display = "none";

    if (tipo === "success"){
        alert_success.style.display = "block";
        alert_success.innerHTML = mensaje;

        setTimeout(() => {
            alert_success.style.display = 'none';
        }, 5000);
    } 
    else if (tipo == "danger"){
        alert_danger.style.display = "block";
        alert_danger.innerHTML = mensaje;

        setTimeout(() => {
            alert_danger.style.display = 'none';
        }, 5000);
    }
}