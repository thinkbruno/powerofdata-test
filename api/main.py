import json

def api(request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    if request.method == "OPTIONS":
        return ("", 204, headers)

    if request.method == "GET":
        return (
            json.dumps({"status": "ok", "mensagem": "API funcionando"}),
            200,
            headers
        )

    if request.method == "POST":
        body = request.get_json()
        return (
            json.dumps({
                "mensagem": "POST recebido",
                "body": body
            }),
            200,
            headers
        )

    return (json.dumps({"erro": "Método não permitido"}), 405, headers)