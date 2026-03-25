# Calculador-api

Projeto Avaliativo desenvolvido para disciplina programação de sistemas distribuidos da universidade dos grandes lagos - UNILAGO sob supervisão do professor Gleydes Oliveira, com menção ao perfil @gleydes.

## Visao Geral
API de calculadora com operacoes basicas e uma interface simples em HTML + JS que consome a API.

## Requisitos
- Python 3.12+ (ou compatível com o ambiente local)

## Como Rodar
1. Crie e ative o ambiente virtual
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instale as dependencias
```powershell
python -m pip install -r requirements.txt
```

3. Suba a API
```powershell
uvicorn main:app --reload
```

4. Abra o front
- Abra `index.html` no navegador

## Endpoints
- `GET /` - mensagem de boas-vindas
- `POST /somar`
- `POST /subtrair`
- `POST /multiplicar`
- `POST /dividir`
- `POST /potencia`
- `POST /raiz`
- `POST /media`
- `GET /calcular?numero1=...&numero2=...&operacao=...`

## Exemplo de Body (POST)
```json
{
  "numero1": 10,
  "numero2": 5
}
```