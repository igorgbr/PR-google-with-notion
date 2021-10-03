# About this project
O objetivo desse projeto é integrar o Notion e o Google Sheet's para automatizar uma parte dos processo do [Performance Review](https://playbook.betrybe.com/docs/people/performance_review/2021-h1_pr/).

Obs. Você precisa ter o [Python](https://www.python.org/downloads/) instalado no seu computador para rodar o script.<br>
Segue um [tutorial do course](https://app.betrybe.com/course/real-life-engineer/python) caso ainda não tenha configurado seu ambiente 

### Primeiros Passos:
1. Crie um Project no Google Cloud, de acordo com o  [video](https://youtu.be/Urh5BQmssJs).
2. Crie um Project no Notion de acordo com o [video](https://www.youtube.com/watch?v=sdn1HgxLwEg).<br>
Você pode assistir só o inicio dos dois video, até a parte da criação do project. 😉
3. Clone o projeto: `git clone https://github.com/igorgbr/PR-google-with-notion.git`
4. Acesse o projeto: `cd PR-google-with-notion `
5. Crie os arquivos `keys.json` com os token's das duas API's nas suas respectivas pastas.
6. Instale as dependencia na pasta googleAPI com o comando:`pip install -r requirements.txt`
7. Crie a planilha de acordo com o exemplo abaixo:
<img src = "https://github.com/igorgbr/PR-google-with-notion/blob/main/imgs/sheets.png" />
8. Crie uma página no notion de acordo com o exemplo:
<img src = "https://github.com/igorgbr/PR-google-with-notion/blob/main/imgs/notion.png" /> 


### Como usar:
Na raiz do projeto temos o arquivo main.py com um exemplo de código, substitua a o valor da constante `SPREADSHEET_ID` na linha 6 de acordo com o ID da planilha que você ira utilizar, ná dúvida assista este [video](https://youtu.be/Urh5BQmssJs).<br>
Rode o comando `python -m main.py` na raiz pro projeto para rodar o script.


#### Call to Action:
Vamos deixar o projeto mais amigavel! <br>
Contribua com seu PR! 💚    
