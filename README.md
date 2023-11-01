# Consulta de Empréstimo

Este é um aplicativo simples de consulta de empréstimo desenvolvido em Python usando a biblioteca `customtkinter` para criar a interface gráfica. O aplicativo utiliza um modelo de classificação de risco de crédito treinado com o algoritmo Naive Bayes para prever se é seguro conceder um empréstimo a um cliente com base em algumas informações fornecidas.

## Funcionalidades

- **Consulta de Empréstimo:** Permite aos usuários informar o valor desejado, o histórico do cliente, a dívida, a garantia e a renda para verificar o risco de conceder um empréstimo.

## Requisitos

- Python 3.x
- Biblioteca `customtkinter`
- Biblioteca `pandas`
- Biblioteca `scikit-learn`

## Como Executar

1. Certifique-se de ter o Python instalado.<br> Você pode baixá-lo em [python.org](https://www.python.org/).

2. Instale as bibliotecas necessárias usando o seguinte comando:<br>
pip install customtkinter pandas scikit-learn

3. Clone este repositório:<br>
git clone https://github.com/Samuel-Gaudencio/app_emprestimo.git

4. Navegue até o diretório do projeto:<br>
cd consulta-emprestimo

5. Execute o aplicativo:<br>
python main.py

## Funcionamento

O aplicativo solicita ao usuário informações sobre o valor desejado do empréstimo, o histórico do cliente, a dívida, a garantia e a renda. Com base nessas informações, o modelo de classificação de risco de crédito faz uma previsão sobre se é seguro conceder o empréstimo ou não.
