const mainWeb = 'http://127.0.0.1:8000'
let btnBuscarId = document.getElementById('btn-get-data')
let btnBuscarLocalidad = document.getElementById('btn-get-localidad')
let selectLocalidad = document.getElementById('get_localidad')
let pressEnterId = document.getElementById('get_id')

// Intergración de la gráfica
let id = document.getElementById('get_id')
let url = `${mainWeb}/core/getdata/${parseInt(id.value)}/`


document.addEventListener('DOMContentLoaded', function(){
    
    id = document.getElementById('get_id')
    localidad = document.getElementById("get_localidad")
    
    url = `${mainWeb}/core/getdata/${parseInt(id.value)}/`
    url2 = `${mainWeb}/core/getdataLocalidad/${localidad.value}/`
    
    fetch(url)
    .then(res => res.json())
    .then(json => {
        window.datos = json[0]
        
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
                scales:{
                    yAxes:[{
                        ticks:{"beginAtZero":true},
                        gridLines: {
                            display: true,
                        },
                    }],

                    xAxes:[{
                        gridLines: {
                            display: true,
                        },
                    }],
                },

            },
        }
        
        window.myChart = new Chart(getMyChart, dataProject)
        
    })


    fetch(url2)
    .then(res => res.json())
    .then(json => {
        window.datosLocalidad = json[0]
            
            window.ChartLocalidad = document.getElementById('chartLocalidad').getContext('2d')
            window.dataLocalidad = {
                type: 'doughnut',
                
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
            
                options: {
                    legend: {
                        display: true,
                        position: 'left',
                        labels: {
                            padding: 20
                        },
                    },
                },
            }

            window.myChartLocalidad = new Chart(ChartLocalidad, dataLocalidad)
    })
    
})

btnBuscarId.addEventListener('click', () => {
    
    url = `${mainWeb}/core/getdata/${parseInt(id.value)}/`

    fetch(url)
    .then(res => res.json())
    .then(json => {
        newData = json[0]
            
            window.dataProject.data.datasets[0].data = newData.data
            window.dataProject.data.datasets[0].label = newData.proyecto

            window.myChart.update()
    })
})

selectLocalidad.addEventListener('change', () => {
    
    url  = `${mainWeb}/core/getdataLocalidad/${localidad.value}/`
    
    fetch(url)
    .then(res => res.json())
    .then(json => {
        newDataLocalidad = json[0]
        window.dataLocalidad.data.datasets[0].data = newDataLocalidad.data
        window.myChartLocalidad.update()
    })
})

pressEnterId.addEventListener('keypress', (e) => {
    if (e.keyCode == 13 & pressEnterId.value !== '') {
        url = `${mainWeb}/core/getdata/${parseInt(id.value)}/`
    
        fetch(url)
        .then(res => res.json())
        .then(json => {
            newData = json[0]
            window.dataProject.data.datasets[0].data = newData.data
            window.dataProject.data.datasets[0].label = newData.proyecto

            window.myChart.update()
        })
    
    }
})
