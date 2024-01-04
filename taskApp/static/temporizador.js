
function temporizador(){
    const time = document.getElementById('time')
    const button_temp = document.getElementById('button_temp')
    const endTemp = document.getElementById("endTemp")
    
    button_temp.className = 'btn-none' //Desaparecer el boton

    let time_task = 0.1 * 60 //Convierte a segundos
    const interval = setInterval(() => {
        let minutos = Math.floor(time_task / 60)
        let segundos = time_task % 60
        segundos = segundos < 10 ? '0' + segundos : segundos
        time.innerText = `${minutos}:${segundos}`

        if(time_task <= 0){
            clearInterval(interval)
            endTemp.play() //Efecutar sonido  
            button_temp.className = '' //Aparecer el boton
            time.innerText = '' //Desaparecer temporizador

        }else{
            time_task--
        }

    },1000)
}