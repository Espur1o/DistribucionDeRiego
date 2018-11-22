 var morris1 = new Morris.Line({
    // ID of the element in which to draw the chart.
    element:'graficas de lineas',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: [
      { dia: '2018-10-1', value: 20, value2: 30 },
      { dia: '2018-10-10', value: 10, value2: 40 },
      { dia: '2018-10-15', value: 5,  value2: 10 },
      { dia: '2018-10-20', value: 5,  value2: 4 },
      { dia: '2018-10-25', value: 20, value2: 1 }
    ],
    lineWidth:1,
    // The name of the data record attribute that contains x-values.
    xkey: 'dia',
    // A list of names of data record attributes that contain y-values.
    ykeys: ['value','value2'],
    // Labels for the ykeys -- will be displayed when you hover over the
    // chart.
    
    lineColors:['#C14D9F','#2CB4AC','#2CB4AC'],
    resize:true,
    labels: ['NODO 1 ', 'NODO 2 '  ]
  });
  // configuración del boton para que cargue los datos 
    //#"tiene que ir el nombre que se le puso a los datos del boton"
    // ver jquery 
  $("#botData").on("click",function(){
    console.log(morris1);
    var nuevaData=  [
      { dia: '2018-10-1', value: 20, value2: 30 },
      { dia: '2018-10-5', value: 10, value2: 40 },
      { dia: '2018-10-10', value: 5,  value2: 10 },
      { dia: '2018-10-15', value: 5,  value2: 4 },
      { dia: '2018-10-', value: 20, value2: 1 }
    ];
    morris1.setData(nuevaData);
  });