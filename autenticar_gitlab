import gitlab
import time

def autenticando():
    #gl = gitlab.Gitlab('', private_token='') coloque aqui a url do seu gitlab e o seu toen de acesso

    print("Processando.................")
    time.sleep(2)

    try:
        gl.auth()
        print(f"Autenticação bem-sucedida: ")
    except gitlab.GitlabAuthenticationError as e:
        print(f"Erro de autenticação: {e}")
    except Exception as e:
        print(f"Ocorreu outro erro: {e} ")

    grupo = gl.groups.get("sefa_teste")
    print("GRUPO: {}".format(grupo.name))

    subgrupos = gl.groups.list()
    gp_excluid = "sefa_teste"

    print("SUBGRUPOS: ")
    for grup in subgrupos:
        if grup.name != gp_excluid:
            print(grup.name)

    print('REPOSITÓRIOS: ')
    time.sleep(0.1)
    projects = grupo.projects.list(all=True)
    for project  in projects:
        print("NOME: {}  ID: {}".format(project.name, project.id))

    return gl
