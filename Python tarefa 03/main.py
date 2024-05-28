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
            nome = input("Digite o nome do(a) aluno(a): ")
            matricula = input("Digite a matrícula do(a) aluno(a): ")
            alunos[matricula] = nome
        case "2":
            aluno_delete = input("Digite o número de matrícula do(a) aluno(a) que deseja deletar: ")
            if aluno_delete in alunos:
                print(f"Aluno(a) {alunos[aluno_delete]} removido com sucesso")
                alunos.pop(aluno_delete)               
            else:
                print("Aluno(a) não encontrado")
        case "3":
            if alunos:
                for matriculaAluno, nomeAluno in alunos.items():
                    print(f"""
Aluno(a): {nomeAluno} 
Número de matrícula: {matriculaAluno}
""")
            else:
                print("Nenhum aluno cadastrado")
        case "0":
            break
        case _:
            print("A opção que você digitou não é válida")