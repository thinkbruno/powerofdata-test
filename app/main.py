import requests
from flask import jsonify, Request

SWAPI_BASE_URL = "https://swapi.dev/api"
ALLOWED_RESOURCES = {"people", "films", "planets", "starships"}

def sort_results(results, sort):
    if not sort:
        return results
    reverse = sort.startswith("-")
    field = sort.lstrip("-")
    return sorted(results, key=lambda x: x.get(field, ""), reverse=reverse)

def paginate(results, page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    return results[start:end]

def swapi_proxy(request: Request):
    resource = request.args.get("resource")
    name = request.args.get("name")
    sort = request.args.get("sort")
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("page_size", 10))

    if not resource:
        return jsonify({"error": "Parameter 'resource' is required"}), 400

    if resource not in ALLOWED_RESOURCES:
        return jsonify({"error": "Invalid resource"}), 400

    response = requests.get(f"{SWAPI_BASE_URL}/{resource}/")
    data = response.json()
    results = data.get("results", [])

    if name:
        results = [
            r for r in results
            if name.lower() in r.get("name", "").lower()
            or name.lower() in r.get("title", "").lower()
        ]

    results = sort_results(results, sort)
    paged = paginate(results, page, page_size)

    return jsonify({
        "resource": resource,
        "count": len(results),
        "results": paged
    })