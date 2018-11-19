
from microWebSrv import MicroWebSrv


# ----------------------------------------------------------------------------
#	AQUI DEBE IR UN HTML DEL SERVIOR!!!! CON 3 GRAFICOS, LOS DATOS DEBEN SALIR DE UN ARCHIVO SCV, INCORPORAR LA SOLUCION DE GRAFICAR
# 	DESDE CSV..... SE PUEDE UTILIZAR JAVASCRIPT.


@MicroWebSrv.route('/INDEX')
def _httpHandlerTestGet(httpClient, httpResponse):
	print(httpClient)
	programa="PROGRAMA 20 MIN TOTALES POR NODO 40 MIN TOTAL"
	content= """\
	<!DOCTYPE html>
	<html>
		<head>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" type="text/css" href="style2.css">
		</head>
		<body>
			<div class="sidenav">
				<a href="http://192.168.43.111/INDEX">PROGRAMAS</a>
				<a href="http://192.168.43.111/NODO%20A">NODO A</a>
				<a href="http://192.168.43.111/NODO%20B">NODO B</a>
  				<a href="http://192.168.43.111/CONTACTO">Contacto</a>
			</div>
			<div class="main">
				<h2>CONFIGURACION DE PROGRAMAS DE RIEGO</h2>
				<p>PROGRAMA ACTUAL DE RIEGO: </p>
  				<p>data</p>%s
				<form action="/INDEX" method="post" accept-charset="ISO-8859-1">
					SENSOR A: <input type="text" name="FLUJO"><br />
					SENSOR B: <input type="text" name="CORRIENTE"><br />
					<input type="submit" value="Submit">
				</form>	
			</div>    

		</body>
	</html>
	"""%programa
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

@MicroWebSrv.route('/NODO A')
def _httpHandlerTestGet2(httpClient, httpResponse):
	print(httpClient)
	content= """\
	<!DOCTYPE html>
	<html>
		<head>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" type="text/css" href="style2.css">
		</head>
		<body>
			<div class="sidenav">
				<a href="http://192.168.43.111/INDEX">PROGRAMAS</a>
				<a href="http://192.168.43.111/NODO%20A">NODO A</a>
				<a href="http://192.168.43.111/NODO%20B">NODO B</a>
  				<a href="http://192.168.43.111/CONTACTO">Contacto</a>
			</div>
			<div class="main">
				<h2>MUESTRAS DE NODO A</h2>
				<p>GRAFICA DE CAUDAL</p>
  				<p>GRAFICA DE CORRIENTE</p>
				<p>GRAFICA DE VOLTAJE SOLAR</p>
			</div>    

		</body>
	</html>
	"""
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )			

@MicroWebSrv.route('/NODO B')
def _httpHandlerTestGet3(httpClient, httpResponse):
	print(httpClient)
	content= """\
	<!DOCTYPE html>
	<html>
		<head>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" type="text/css" href="style2.css">
		</head>
		<body>
			<div class="sidenav">
				<a href="http://192.168.43.111/INDEX">PROGRAMAS</a>
				<a href="http://192.168.43.111/NODO%20A">NODO A</a>
				<a href="http://192.168.43.111/NODO%20B">NODO B</a>
  				<a href="http://192.168.43.111/CONTACTO">Contacto</a>
			</div>
			<div class="main">
				<h2>MUESTRAS DE NODO B</h2>
				<p>GRAFICA DE CAUDAL</p>
  				<p>GRAFICA DE CORRIENTE</p>
				<p>GRAFICA DE VOLTAJE SOLAR</p>
			</div>    

		</body>
	</html>
	"""
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

@MicroWebSrv.route('/CONTACTO')
def _httpHandlerTestGet4(httpClient, httpResponse):
	print(httpClient)
	content= """\
	<!DOCTYPE html>
	<html>
		<head>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" type="text/css" href="style2.css">
		</head>
		<body>
			<div class="sidenav">
				<a href="http://192.168.43.111/INDEX">PROGRAMAS</a>
				<a href="http://192.168.43.111/NODO%20A">NODO A</a>
				<a href="http://192.168.43.111/NODO%20B">NODO B</a>
  				<a href="http://192.168.43.111/CONTACTO">Contacto</a>
			</div>
			<div class="main">
				<h2>CONTACTO</h2>
				<p>ALONSO GAJARDO</p>
  				<p>MAIL: ALONSO.GAJARDO@MAIL.UDP.CL</p>
				<p>TEL: 988992732</p>
			</div>    

		</body>
	</html>
	"""
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

@MicroWebSrv.route('/INDEX', 'POST')
def _httpHandlerTestPost(httpClient, httpResponse) :
	formData  = httpClient.ReadRequestPostedFormData()
	print(httpResponse)
	print("/test/post de data con: ", formData)
	flujo = formData["FLUJO"]
	corriente  = formData["CORRIENTE"]
	content   = """\
	<!DOCTYPE html>
	<html lang=en>
		<head>
			<meta charset="UTF-8" />
            <title>TEST POST</title>
        </head>
        <body>
            <h1>TEST POST</h1>
            Flujo = %s<br />
            Corriente = %s<br />
        </body>
    </html>
	""" % ( MicroWebSrv.HTMLEscape(flujo),
		    MicroWebSrv.HTMLEscape(corriente) )

	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )



@MicroWebSrv.route('/NODOASSFLUJO', 'POST')
def _httpHandlerTestPostA(httpClient, httpResponse) :
	status_riego=False
	formData  = httpClient.ReadRequestPostedFormData()
	print("/NODOASSFLUJO/POST: ", formData)
	flujo = formData["FLUJO"]
	secuencia  = formData["SECUENCIA"]
	content   = """\
	<!DOCTYPE html>
	<html>
		<body>
			<h1>
			DATA RECIBIDO OK DE NODO A
			ESTADO DE RIEGO: %s
			</h1>
		</body>
		
    </html>
	""" %status_riego

	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

@MicroWebSrv.route('/NODOASSCORRIENTE', 'POST')
def _httpHandlerTestPostA2(httpClient, httpResponse) :
	status_riego=False
	formData  = httpClient.ReadRequestPostedFormData()
	print("/NODOASSCORRIENTE/POST: ", formData)
	corriente = formData["CORRIENTE"]
	secuencia  = formData["SECUENCIA"]
	content   = """\
	<!DOCTYPE html>
	<html>
		<body>
			<h1>
			DATA RECIBIDO OK DE NODO B
			ESTADO DE RIEGO: %s
			</h1>
		</body>
		
    </html>
	""" %status_riego

	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

# ----------------------------------------------------------------------------

def _acceptWebSocketCallback(webSocket, httpClient) :
	print("WS ACCEPT")
	webSocket.RecvTextCallback   = _recvTextCallback
	webSocket.RecvBinaryCallback = _recvBinaryCallback
	webSocket.ClosedCallback 	 = _closedCallback

def _recvTextCallback(webSocket, msg) :
	print("WS RECV TEXT : %s" % msg)
	webSocket.SendText("Reply for %s" % msg)

def _recvBinaryCallback(webSocket, data) :
	print("WS RECV DATA : %s" % data)

def _closedCallback(webSocket) :
	print("WS CLOSED")

# ----------------------------------------------------------------------------

routeHandlers = [
	( "/INDEX",	"GET",	_httpHandlerTestGet ),
	( "/INDEX",	"POST",	_httpHandlerTestPost ),
	( "/NODO%20A",	"GET",	_httpHandlerTestGet2 ),
	( "/NODO%20B",	"GET",	_httpHandlerTestGet3 ),
	( "/CONTACTO",	"GET",	_httpHandlerTestGet4 ),
	( "/NODOASSFLUJO",	"POST",	_httpHandlerTestPostA2 ),
	( "/NODOASSCORRIENTE",	"POST",	_httpHandlerTestPostA2 )

]
do_connect("Invitado","1a2s3d4f5")
print("Conexion ok, servidor apunto de iniciar")
srv = MicroWebSrv()
srv.MaxWebSocketRecvLen     = 256
srv.WebSocketThreaded		= False
srv.AcceptWebSocketCallback = _acceptWebSocketCallback
srv.Start(threaded=False)

i