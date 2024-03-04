# TechChallenge

## Setup inicial

### Criar env

```shell
python -m venv [env_curso]
```

### Ativar a env
```shell
.\[env_curso]\Scripts/activate
```
- Em caso de erro, comando do powershell para habilitar o activate (rodar powershell como adm) 
- Set-ExecutionPolicy Unrestricted -Force 

### Instalar libs

```shell
python -m pip install -r requirements.txt
```

### Rodar o app
```shell
streamlit run Dash.py
```