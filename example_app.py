from newf import Application, Response, ResponseRedirect
       
def foo(request):
    return Response("<h1>Hello World!</h1>")

def bar(request):
    return ResponseRedirect("/foo")
    
    
def test_debug(request):
    raise Exception, 'I am the exception'
    
    
urls = (
    (r'^/foo$', foo),
    (r'^/bar$', bar),
    (r'^/test-debug$', test_debug),
)

application = Application(urls, debug=True)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 8000, application)
    server.serve_forever()
