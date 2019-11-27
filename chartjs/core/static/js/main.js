var ctx = document.getElementById('myChart').getContext('2d');
var req = new XMLHttpRequest();
let id = document.getElementById('get_id')
let btnBuscarId = document.getElementById('btn-get-data')

btnBuscarId.addEventListener('click', () =>{

    console.log('Hola, desde el boton')
    if (id.value === null){
        id = 1
    }else{
        id = id.value
    }
})
console.log(id)
// const url = `http://127.0.0.1:8000/core/getdata/${parseInt(id)}'`;

req.open('GET', url)
req.send()

req.onreadystatechange = function () {
    if(req.readyState === XMLHttpRequest.DONE && req.status === 200){
        var datos = JSON.parse(req.response)
        console.log(datos)
        console.log(typeof(datos.data))
    }
}


function plot(datos){
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
    
        // The data for our dataset
        data: {
            labels: datos.labels,
            datasets: [{
                label: datos.name,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: datos.data,
            }]
        },
    
        // Configuration options go here
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Chart.js Line Chart'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Month'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    });
}
