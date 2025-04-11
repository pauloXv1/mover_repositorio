import gitlab
import json
import time
from autenticar_gitlab import autenticando


#GITLAB_URL = '' coloque aqui a url do seu gitlab
#PRIVATE_TOKEN ='' coloque aqui o seu token de acesso 

gl = autenticando()
if not gl:
    exit("Falha na autenticação")

def buscar_id(nome_repositorio):
    try:
        projetos = gl.projects.list(search=nome_repositorio, get_all=True)
        for projeto in projetos:
            if projeto.name == nome_repositorio:
                return projeto.id
            print(projeto.id)
    except gitlab.exceptions.GitlabError as e:
        print(f"erro {nome_repositorio}: {e}" )
        return None

def buscar_subgrupo(nome_subrupo):
    subgrupo = gl.groups.list(search=nome_subrupo)
    for grupo in subgrupo:
        if grupo.name == nome_subrupo:
            return grupo

time.sleep(1)
def mover_repositorio(repo_id, subgrupo):
    try:
        projeto = gl.projects.get(repo_id)
        grupo_destino = buscar_subgrupo(subgrupo)
        print(grupo_destino) 
        novo_namespace = grupo_destino.full_path
        print("Movendo {projeto.name} para  {novo_namespace}..")

        projeto.transfer(to_namespace_grupo_id=grupo_destino.id)
        print(f"Repositório {projeto.name} movido para {novo_namespace}")
    except gitlab.exceptions.GitlabError as e:
        print(f"erro {projeto.name}: {e}" )

try:
    with open("Book.json", "r", encoding="utf-8") as file:
        repositorios = json.load(file)
        print(repositorios)
except FileNotFoundError:
    exit("erro")

for item in repositorios:
    nome_repositorio = item ["repositorio"]
    subgrupo = item["subgrupo"]
    repo_id = buscar_id(nome_repositorio)

    if repo_id:
        mover_repositorio(repo_id, subgrupo)
    else:
        print(f"repositorio {nome_repositorio} não encontrado no gtilab")
