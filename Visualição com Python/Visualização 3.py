import pandas as pd 
import matplotlib.pyplot as plt

dados = {
    'turma': ['A', 'B', 'C'], 
    'qtde_alunos': [20, 17, 10]
}

df = pd.DataFrame(dados)
df.set_index('turma')

df.plot(x = 'turma', y = 'qtde_alunos', kind = 'bar', 
        title = 'Quantidade de alunos por turma', color = 'red', 
         legend = True)

df.plot(y = 'qtde_alunos', kind = 'pie')

plt.show()