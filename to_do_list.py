tarefas = []  # Lista para armazenar as tarefas

def adicionar_tarefa(nova_tarefa):
  """Adiciona uma nova tarefa à lista de tarefas.

  Args:
    nova_tarefa: A descrição da nova tarefa.
  """
  tarefas.append(nova_tarefa)
  print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")

# Exemplo de uso:
adicionar_tarefa("Fazer compras")
adicionar_tarefa("Estudar Python")

def listar_tarefas():
    if not tarefas:
        print("Sua lista de tarefas está vazia.")
    else:
        for indice, tarefa in enumerate(tarefas):
            print(f"{indice+1}. {tarefa}")

def atualizar_tarefa(indice, nova_tarefa):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice] = nova_tarefa
        print("Tarefa atualizada com sucesso!")
    else:
        print("Índice inválido.")

def deletar_tarefa(indice):
    if indice >= 0 and indice < len(tarefas):
        del tarefas[indice]
        print("Tarefa deletada com sucesso!")
    else:
        print("Índice inválido.")

adicionar_tarefa("Fazer compras")
listar_tarefas()
adicionar_tarefa("Estudar Python")
listar_tarefas()
atualizar_tarefa(1, "Estudar Ciência de Dados")
listar_tarefas()
deletar_tarefa(0)
listar_tarefas()