const mainWeb = 'http://127.0.0.1:8000'
let btnBuscarId = document.getElementById('btn-get-data')
let btnBuscarLocalidad = document.getElementById('btn-get-localidad')

// Conexión con servidor
let req = new XMLHttpRequest();
let req2 = new XMLHttpRequest();

// Intergración de la gráfica
let id = document.getElementById('get_id')
let url = `${mainWeb}/core/getdata/${parseInt(id.value)}/`
let reset = false
let destroy = false

document.addEventListener('DOMContentLoaded', function(){
    id = document.getElementById('get_id')
    localidad = document.getElementById('get_localidad')

    url = `${mainWeb}/core/getdata/${parseInt(id.value)}/`
    url2 = `${mainWeb}/core/getdataLocalidad/${slugify(localidad.value)}/`

    req.open('GET', url)
    req2.open('GET', url2)
    
    req.send()
    req2.send()

    req.onreadystatechange = function () {
        if(req.readyState === XMLHttpRequest.DONE && req.status === 200){
            window.datos = JSON.parse(req.response)
            window.datos = datos[0]
            
            window.getMyChart = document.getElementById('myChart').getContext('2d')
            window.dataProject = {
                type: 'bar',
                
                data: {
                    labels: datos.labels,
                    datasets: [{
                        label: datos.proyecto,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgb(255, 99, 132)',
                        borderWidth: 1,
                        data: datos.data,
                    }]
                },
            
                options: {
                    "scales":{
                        "yAxes":[{"ticks":{"beginAtZero":true}}]
                    }
                },
            }
            
            window.myChart = new Chart(getMyChart, dataProject)
        }
    }
    
    req2.onreadystatechange = function () {
        if(req2.readyState === XMLHttpRequest.DONE && req2.status === 200){
            window.datosLocalidad = JSON.parse(req2.response)
            window.datosLocalidad = datosLocalidad[0]
            
            console.log(datosLocalidad)
            
            window.ChartLocalidad = document.getElementById('chartLocalidad').getContext('2d')
            window.dataLocalidad = {
                type: 'pie',
                
                data: {
                    labels: datosLocalidad.labels,
                    datasets: [{
                        backgroundColor: [
                            'rgba(155, 80, 25, 0.5)',
                            'rgba(55, 20, 125, 0.5)',
                            'rgba(5, 100, 85, 0.5)',
                            'rgba(305, 70, 560, 0.5)',
                            'rgba(220, 155, 65, 0.5)',                            
                        ],
                        data: datosLocalidad.data,
                    }]
                },
            
                options: { },
            }

            window.myChartLocalidad = new Chart(ChartLocalidad, dataLocalidad)
        }
    }
    
})

btnBuscarId.addEventListener('click', () => {
    
    id = document.getElementById('get_id')
    url = `${mainWeb}/core/getdata/${parseInt(id.value)}/`

    req.open('GET', url)
    req.send()

    req.onreadystatechange = function () {
        if(req.readyState === XMLHttpRequest.DONE && req.status === 200){
            newData = JSON.parse(req.response)
            newData = newData[0]
            
            window.dataProject.data.datasets[0].data = newData.data
            window.dataProject.data.datasets[0].label = newData.proyecto

            window.myChart.update()
        }
    }
})

btnBuscarLocalidad.addEventListener('click', () => {
    
    console.log('Estoy funcionando')
    localidad = document.getElementById('get_localidad')
    url  = `${mainWeb}/core/getdataLocalidad/${slugify(localidad.value)}/`

    req2.open('GET', url)
    req2.send()

    req2.onreadystatechange = function () {
        if(req2.readyState === XMLHttpRequest.DONE && req2.status === 200){
            newDataLocalidad = JSON.parse(req2.response)
            newDataLocalidad = newDataLocalidad[0]
            
            console.log(newDataLocalidad)

            window.dataLocalidad.data.datasets[0].data = newDataLocalidad.data

            window.myChartLocalidad.update()
        }
    }
})

function slugify(str) {
    str = str.replace(/^\s+|\s+$/g, ""); // trim
    str = str.toLowerCase();
  
    // remove accents, swap ñ for n, etc
    var from = "åàáãäâèéëêìíïîòóöôùúüûñç·/_,:;";
    var to = "aaaaaaeeeeiiiioooouuuunc------";
  
    for (var i = 0, l = from.length; i < l; i++) {
      str = str.replace(new RegExp(from.charAt(i), "g"), to.charAt(i));
    }
  
    str = str
      .replace(/[^a-z0-9 -]/g, "") // remove invalid chars
      .replace(/\s+/g, "-") // collapse whitespace and replace by -
      .replace(/-+/g, "-"); // collapse dashes
  
    return str;
  }