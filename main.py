from app.main import swapi_proxy

def api_pod(request):
    return swapi_proxy(request)
