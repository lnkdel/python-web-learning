def application(environ, start_reponse):
    start_reponse('200 OK', [('Content-Type', 'text/html')])
    return '<b>Hello, world!</b>'