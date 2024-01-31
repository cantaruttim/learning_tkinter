import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Cotação de Moedas")

## configurando a janela para ajustar o tamanho automaticamente.
janela.rowconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)

# cria o objeto
msg = tk.Label(text="Sistema de Cotação de Moedas", bg='Black', fg='white', width=35, height=2)
# adiciona o obj na janela
msg.grid(row=0,column=0, columnspan=2, sticky="NSEW")

msg2 = tk.Label(text='Selecione a moeda desejada: ')
msg2.grid(row=1,column=0)

#moeda = tk.Entry()
#moeda.grid(row=1,column=1)


dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Libra': 6.50
}

## combo box
moeda = list(dicionario_cotacoes.keys())
moedas = ttk.Combobox(janela, values=moeda) # janela correspondente, valores
moedas.grid(row=1, column=1)

def buscar_cotacao():
    moeda_preenchida = moedas.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    msg_cotacao = tk.Label(text='Cotação não Encontrada')
    msg_cotacao.grid(row=4,column=0)
    if cotacao_moeda:
        msg_cotacao['text'] = f'Cotação do {moeda_preenchida} é de R$ {cotacao_moeda} reais'
    else:
        pass


botao = tk.Button(text='Buscar Cotação', command=buscar_cotacao)
botao.grid(row=2, column=1)

msg3 = tk.Label(text='Caso queira pegar mais de uma cotação, digite uma por linha')
msg3.grid(row=4,column=0, columnspan=2)

caixa = tk.Text(width=10, height=5)
caixa.grid(row=5, column=0, sticky='NSWE')


def buscar_cotacoes():
    texto = caixa.get("1.0", tk.END) # linha . coluna
    lista_moedas = texto.split('\n')
    mensagens_cotacoes = []

    for item in lista_moedas:
        cotacoes = dicionario_cotacoes.get(item)
        if cotacoes:
            mensagens_cotacoes.append(f"{item}: R$ {cotacoes}")
    msg4 = tk.Label(text='\n'.join(mensagens_cotacoes))
    msg4.grid(row=6, column=1)



botaomultiplo = tk.Button(text='Buscar Cotações', command=buscar_cotacoes)
botaomultiplo.grid(row=5, column=1)



janela.mainloop()
