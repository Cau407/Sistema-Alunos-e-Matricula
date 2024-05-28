alunos = {}

while True:
    menu = input("""
Escolha entre as seguintes alternativas:
[1] - Adicionar um aluno
[2] - Remover um aluno
[3] - Visualizar os alunos
[0] - Sair
""")
    
    match menu:
        case "1":
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula do aluno: ")
            alunos[nome] = matricula
        case "2":
            aluno_delete = input("Digite o nome do aluno que deseja deletar: ")
            if aluno_delete in alunos:
                alunos.pop(aluno_delete)
                print(f"Aluno {aluno_delete} removido com sucesso")
            else:
                print("Aluno não encontrado")
        case "3":
            if alunos:
                for nomeAluno, matriculaAluno in alunos.items():
                    print(f"""
Aluno: {nomeAluno} 
Número de matrícula: {matriculaAluno}

///""")
            else:
                print("Nenhum aluno cadastrado")
        case "0":
            break
        case _:
            print("A opção que você digitou não é válida")