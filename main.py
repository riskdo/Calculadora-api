from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title= "Calculadora Funcional",
    description= "API para realizar operações matemáticas básicas",
    version= "1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OperacaoRequest(BaseModel):
    numero1: float
    numero2: float
    
    model_config = {
        "json_schema_extra": {
            "example": {"numero1": 10, "numero2": 5}
        }
    }
    
class ResultadoResponse(BaseModel):
    operacao: str
    numero1: float
    numero2: float
    resultado: float

# metodo Get 
  
@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à Calculadora Funcional API!", "docs": "/docs"}

#metodo Post

@app.post(
    "/somar",
    response_model=ResultadoResponse,
    summary="Realiza a soma de dois números",
    responses={
        200: {
            "description": "Resultado da soma",
            "content": {
                "application/json": {
                    "example": {
                        "operacao": "soma",
                        "numero1": 10,
                        "numero2": 6,
                        "resultado": 16
                    }
                }
            }
        }
    }
    )
def somar(dados: OperacaoRequest):
    resultado = dados.numero1 + dados.numero2
    return ResultadoResponse(
        operacao = "soma",
        numero1 = dados.numero1,
        numero2 = dados.numero2,
        resultado = resultado
    )
    
@app.post(
    "/subtrair",
    response_model=ResultadoResponse,
    summary="Subtrai dois numeros",
    responses={
        200: {
            "description": "Resultado da subtracao",
            "content": {
                "application/json": {
                    "example": {
                        "operacao": "subtracao",
                        "numero1": 10,
                        "numero2": 4,
                        "resultado": 6
                    }
                }
            }
        }
    }
)
def subtrair(dados: OperacaoRequest):
    resultado = dados.numero1 - dados.numero2
    return ResultadoResponse(
        operacao = "subtração",
        numero1 = dados.numero1,
        numero2 = dados.numero2,
        resultado = resultado
    )
    
@app.post(
    "/multiplicar",
    response_model=ResultadoResponse,
    summary="Multiplica dois numeros",
    responses={
        200: {
            "description": "Resultado da multiplicacao",
            "content": {
                "application/json": {
                    "example": {
                        "operacao": "multiplicacao",
                        "numero1": 4,
                        "numero2": 7,
                        "resultado": 28
                    }
                }
            }
        }
    }
)
def multiplicar(dados: OperacaoRequest):
    resultado = dados.numero1 * dados.numero2
    return ResultadoResponse(
        operacao = "multiplicação",
        numero1 = dados.numero1,
        numero2 = dados.numero2,
        resultado = resultado
    )

@app.post(
    "/dividir",
    response_model=ResultadoResponse,
    summary="Divide dois numeros",
    responses={
        200: {
            "description": "Resultado da divisao",
            "content": {
                "application/json": {
                    "example": {
                        "operacao": "divisao",
                        "numero1": 32,
                        "numero2": 8,
                        "resultado": 4
                    }
                }
            }
        },
        400: {
            "description": "Erro de validacao",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "O segundo número não pode ser zero."
                    }
                }
            }
        }
    }
)
def dividir(dados: OperacaoRequest):
    if dados.numero2 == 0:
        raise HTTPException(
            status_code=400,
            detail="O segundo número não pode ser zero."
            )
    resultado = dados.numero1 / dados.numero2
    return ResultadoResponse(
        operacao = "divisão",
        numero1 = dados.numero1,
        numero2 = dados.numero2,
        resultado = resultado
    )

@app.post(
    "/potencia",
    response_model=ResultadoResponse,
    summary="Calcula potencia",
    responses={
        200: {
            "description": "Resultado da potencia",
            "content": {
                "application/json": {
                    "example": {
                        "operacao": "potencia",
                        "numero1": 2,
                        "numero2": 5,
                        "resultado": 32
                    }
                }
            }
        }
    }
)
def potencia(dados: OperacaoRequest):
    resultado = dados.numero1 ** dados.numero2
    return ResultadoResponse(
        operacao = "potencia",
        numero1 = dados.numero1,
        numero2 = dados.numero2,
        resultado = resultado
    )

@app.post(
    "/raiz",
    response_model=ResultadoResponse,
    summary="Calcula raiz",
    responses={
        200: {
            "description": "Resultado da raiz",
            "content": {
                "application/json": {
                    "example": {
                        "operacao": "raiz",
                        "numero1": 81,
                        "numero2": 2,
                        "resultado": 9
                    }
                }
            }
        },
        400: {
            "description": "Erro de validacao",
            "content": {
                "application/json": {
                    "examples": {
                        "indice_zero": {
                            "summary": "Indice zero",
                            "value": {"detail": "O indice da raiz nao pode ser zero."}
                        },
                        "numero_negativo": {
                            "summary": "Numero negativo",
                            "value": {"detail": "Raiz de numero negativo nao e permitida."}
                        }
                    }
                }
            }
        }
    }
)
def raiz_operacao(dados: OperacaoRequest):
    if dados.numero2 == 0:
        raise HTTPException(
            status_code=400,
            detail="O indice da raiz nao pode ser zero."
            )
    if dados.numero1 < 0:
        raise HTTPException(
            status_code=400,
            detail="Raiz de numero negativo nao e permitida."
            )
    resultado = dados.numero1 ** (1 / dados.numero2)
    return ResultadoResponse(
        operacao = "raiz",
        numero1 = dados.numero1,
        numero2 = dados.numero2,
        resultado = resultado
    )

@app.post(
    "/media",
    response_model=ResultadoResponse,
    summary="Calcula media",
    responses={
        200: {
            "description": "Resultado da media",
            "content": {
                "application/json": {
                    "example": {
                        "operacao": "media",
                        "numero1": 10,
                        "numero2": 6,
                        "resultado": 8
                    }
                }
            }
        }
    }
)
def media(dados: OperacaoRequest):
    resultado = (dados.numero1 + dados.numero2) / 2
    return ResultadoResponse(
        operacao = "media",
        numero1 = dados.numero1,
        numero2 = dados.numero2,
        resultado = resultado
    )
    
@app.get("/calcular")
def calcular_query(numero1: float, numero2: float, operacao: str):
    operacoes = {
        "soma":             lambda a, b: a + b,
        "subtracao":        lambda a, b: a - b,
        "multiplicacao":    lambda a, b: a * b,
        "divisao":          lambda a, b: a / b,
        "potencia":         lambda a, b: a ** b,
        "raiz":             lambda a, b: a ** (1 / b),
        "media":            lambda a, b: (a + b) / 2
    }
    
    if operacao not in operacoes:
        raise HTTPException(
            status_code=400,
            detail=f'Operação inválida. Use: {list(operacoes.keys())}'
        )
    if operacao == "divisao" and numero2 == 0:
        raise HTTPException(
            status_code=400,
            detail="Divisão por zero não é permitida."
        )
    if operacao == "raiz":
        if numero2 == 0:
            raise HTTPException(
                status_code=400,
                detail="Indice da raiz nao pode ser zero."
            )
        if numero1 < 0:
            raise HTTPException(
                status_code=400,
                detail="Raiz de numero negativo nao e permitida."
            )
    return {
        "operacao": operacao,
        "numero1": numero1,
        "numero2": numero2,
        "resultado": operacoes[operacao](numero1, numero2)
    }
    
