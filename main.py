import customtkinter as ctk
from tkinter import *
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder


def verifica():
    base_risco = pd.read_csv('risco_credito.csv')

    x_risco = base_risco.iloc[:, 0:4].values
    y_risco = base_risco.iloc[:, 4].values

    label_encoder_historia = LabelEncoder()
    label_encoder_divida = LabelEncoder()
    label_encoder_garantia = LabelEncoder()
    label_encoder_renda = LabelEncoder()

    x_risco[:, 0] = label_encoder_historia.fit_transform(x_risco[:, 0])
    x_risco[:, 1] = label_encoder_divida.fit_transform(x_risco[:, 1])
    x_risco[:, 2] = label_encoder_garantia.fit_transform(x_risco[:, 2])
    x_risco[:, 3] = label_encoder_renda.fit_transform(x_risco[:, 3])

    naives_risco = GaussianNB()
    naives_risco.fit(x_risco, y_risco)

    historia = entry_historia.get()
    divida = entry_divida.get()
    garantia = entry_garantia.get()
    renda = entry_renda.get()

    if historia == 'boa':
        historia = 0
    elif historia == 'ruim':
        historia = 2
    elif historia == 'desconhecida':
        historia = 1

    if divida == 'alta':
        divida = 0
    elif divida == 'baixa':
        divida = 2

    if garantia == 'nenhuma':
        garantia = 1
    elif garantia == 'adequada':
        garantia = 0

    if float(renda) < 15000:
        renda = 0
    elif float(renda) <= 35000:
        renda = 1
    elif float(renda) > 35000:
        renda = 2

    previsoes = naives_risco.predict([[historia, divida, garantia, renda]])
    risco = str(previsoes[0])
    text_risco.configure(text=f'O risco de conceder emprestimo para esse cliente é {risco.title()}')


root = ctk.CTk()
root.geometry('600x400')
root.title('Consulta de emprestimo')

title = ctk.CTkLabel(root, text='Consulta de Emprestimo', text_color='#f00', font=('Montserrat', 20, 'bold'))
title.pack(pady=20)

text_valor = ctk.CTkLabel(root, text='Qual valor deseja?', text_color='#fff', font=('Montserrat', 15, 'bold'))
text_valor.place(x=10, y=80)
entry_valor = ctk.CTkEntry(root, placeholder_text='Informe o valor', width=100, fg_color='transparent', border_width=1)
entry_valor.place(x=150, y=80)

text_historia = ctk.CTkLabel(root, text='Qual o histórico do cliente (boa - ruim - desconhecido)?', text_color='#fff',
                             font=('Montserrat', 15, 'bold'))
text_historia.place(x=10, y=120)

entry_historia = ctk.CTkEntry(root, placeholder_text='Informe o histórico', width=120, fg_color='transparent', border_width=1)
entry_historia.place(x=410, y=120)

text_divida = ctk.CTkLabel(root, text='Qual a divida do cliente (baixa - alta)?', text_color='#fff',
                           font=('Montserrat', 15, 'bold'))
text_divida.place(x=10, y=160)

entry_divida = ctk.CTkEntry(root, placeholder_text='Informe a divida', width=105, fg_color='transparent', border_width=1)
entry_divida.place(x=280, y=160)

text_garantia = ctk.CTkLabel(root, text='Qual a garantia do cliente (nenhuma - adequada)?', text_color='#fff',
                             font=('Montserrat', 15, 'bold'))
text_garantia.place(x=10, y=200)

entry_garantia = ctk.CTkEntry(root, placeholder_text='Informe a garantia', width=120, fg_color='transparent', border_width=1)
entry_garantia.place(x=370, y=200)

text_renda = ctk.CTkLabel(root, text='Qual a renda do cliente?', text_color='#fff', font=('Montserrat', 15, 'bold'))
text_renda.place(x=10, y=240)

entry_renda = ctk.CTkEntry(root, placeholder_text='Informe a renda', width=120, fg_color='transparent', border_width=1)
entry_renda.place(x=195, y=240)

button = ctk.CTkButton(root, text='Verificar', command=verifica)
button.place(x=220, y=290)

text_risco = ctk.CTkLabel(root, text='', text_color='#fff', font=('Montserrat', 18, 'bold'))
text_risco.place(x=30, y=330)

root.mainloop()