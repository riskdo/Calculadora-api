import urllib.request, json

BASE_URL = "http://127.0.0.1:8000"

def post(endpoint, dados):
    req = urllib.request.Request(
        f"{BASE_URL}{endpoint}",
        data=json.dumps(dados).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

# testar todas as operacoes

r = post("/somar", {"numero1": 10, "numero2": 6})
print(f"Soma: {r['resultado']}")

r = post("/subtrair", {"numero1": 10, "numero2": 4})
print(f"Subtracao: {r['resultado']}")

r = post("/multiplicar", {"numero1": 4, "numero2": 7})
print(f"Multiplicacao: {r['resultado']}")

r = post("/dividir", {"numero1": 32, "numero2": 8})
print(f"Divisao: {r['resultado']}")

r = post("/potencia", {"numero1": 2, "numero2": 5})
print(f"Potencia: {r['resultado']}")

r = post("/raiz", {"numero1": 81, "numero2": 2})
print(f"Raiz: {r['resultado']}")

r = post("/media", {"numero1": 10, "numero2": 6})
print(f"Media: {r['resultado']}")