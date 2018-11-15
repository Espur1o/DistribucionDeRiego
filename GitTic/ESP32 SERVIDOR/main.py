
from microWebSrv import MicroWebSrv


# ----------------------------------------------------------------------------
#	AQUI DEBE IR UN HTML DEL SERVIOR!!!! CON 3 GRAFICOS, LOS DATOS DEBEN SALIR DE UN ARCHIVO SCV, INCORPORAR LA SOLUCION DE GRAFICAR
# 	DESDE CSV..... SE PUEDE UTILIZAR JAVASCRIPT.

@MicroWebSrv.route('/test')
def _httpHandlerTestGet(httpClient, httpResponse) :
	content = """\
	<!DOCTYPE html>
	<html lang=en>
        <head>
			<link rel="stylesheet" href="style.css">
        	<meta charset="UTF-8" />
            <title>Proyecto TIC'S 2018 SEGUNDO SEMESTRE</title>
        </head>
        <body>
            <h2>PAGINA WEBA</h2>
			<div id="navbar">
				<a href="#SERVIDOR">SERVIDOR</a>
				<a href="#NODO A">NODO A</a>
				<a href="#NODO B">NODO B</a>
			</div>
            DIRECCION IP DEL CLIENTE = %s
            <br />
			<form action="/test" method="post" accept-charset="ISO-8859-1">
				First name: <input type="text" name="firstname"><br />
				Last name: <input type="text" name="lastname"><br />
				<input type="submit" value="Submit">
			</form>
        </body>
    </html>
	""" % httpClient.GetIPAddr()
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

@MicroWebSrv.route('/NODOB')
def _httpHandlerTestGet(httpClient, httpResponse) :
	content = """\
	<!DOCTYPE html>
	<html lang=en>
        <head>
			<link rel="stylesheet" href="style.css">
        	<meta charset="UTF-8" />
            <title>Proyecto TIC'S 2018 SEGUNDO SEMESTRE</title>
        </head>
        <body>
            <h2>MODULO NODO B</h2>
			<div id="navbar">
				<a href="#SERVIDOR">SERVIDOR</a>
				<a href="#NODO A">NODO A</a>
				<a href="#NODO B">NODO B</a>
			</div>
        </body>
    </html>
	""" % httpClient.GetIPAddr()
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )
@MicroWebSrv.route('/NODOA')
def _httpHandlerTestGet(httpClient, httpResponse) :
	content = """\
	<!DOCTYPE html>
	<html lang=en>
        <head>
			<link rel="stylesheet" href="style.css">
        	<meta charset="UTF-8" />
            <title>Proyecto TIC'S 2018 SEGUNDO SEMESTRE</title>
        </head>
        <body>
            <h2>MODULO NODO A</h2>
			<div id="navbar">
				<a href="#SERVIDOR">SERVIDOR</a>
				<a href="#NODO A">NODO A</a>
				<a href="#NODO B">NODO B</a>
			</div>
        </body>
    </html>
	""" % httpClient.GetIPAddr()
	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )

@MicroWebSrv.route('/test', 'POST')
def _httpHandlerTestPost(httpClient, httpResponse) :
	formData  = httpClient.ReadRequestPostedFormData()
	print("/test/post de data con: ", formData)
	firstname = formData["firstname"]
	lastname  = formData["lastname"]
	content   = """\
	<!DOCTYPE html>
	<html lang=en>
		<head>
			<meta charset="UTF-8" />
            <title>TEST POST</title>
        </head>
        <body>
            <h1>TEST POST</h1>
            Firstname = %s<br />
            Lastname = %s<br />
        </body>
    </html>
	""" % ( MicroWebSrv.HTMLEscape(firstname),
		    MicroWebSrv.HTMLEscape(lastname) )

	httpResponse.WriteResponseOk( headers		 = None,
								  contentType	 = "text/html",
								  contentCharset = "UTF-8",
								  content 		 = content )


@MicroWebSrv.route('/edit/<index>')             # <IP>/edit/123           ->   args['index']=123
@MicroWebSrv.route('/edit/<index>/abc/<foo>')   # <IP>/edit/123/abc/bar   ->   args['index']=123  args['foo']='bar'
@MicroWebSrv.route('/edit')                     # <IP>/edit               ->   args={}
def _httpHandlerEditWithArgs(httpClient, httpResponse, args={}) :
	content = """\
	<!DOCTYPE html>
	<html lang=en>
        <head>
        	<meta charset="UTF-8" />
            <title>TEST EDIT</title>
        </head>
        <body>
	"""
	content += "<h1>EDIT item with {} variable arguments</h1>"\
		.format(len(args))
	
	if 'index' in args :
		content += "<p>index = {}</p>".format(args['index'])
	
	if 'foo' in args :
		content += "<p>foo = {}</p>".format(args['foo'])
	
	content += """
        </body>
    </html>
	"""
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
	( "/test",	"GET",	_httpHandlerTestGet ),
	( "/test",	"POST",	_httpHandlerTestPost )
]
do_connect("iPhone de Benjamin","arduinoUno")
print("Conexion ok, servidor apunto de iniciar")
srv = MicroWebSrv()
srv.MaxWebSocketRecvLen     = 256
srv.WebSocketThreaded		= False
srv.AcceptWebSocketCallback = _acceptWebSocketCallback
srv.Start(threaded=False)

# ----------------------------------------------------------------------------
