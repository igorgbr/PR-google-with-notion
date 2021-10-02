# About this project
O objetivo desse projeto é integrar o Notion e o Google Sheet's para automatizar uma parte dos passos para organização dos inputs diários nescessários.

###Primeiros Passos:
1. Criar um Project no Google Cloud, [video](https://youtu.be/Urh5BQmssJs).
2. Criar um Project no Notion [video](https://www.youtube.com/watch?v=sdn1HgxLwEg).
Você pode assistir só o inicio dos dois video, até o final da criação do project. ;)
3. Criar os arquivos `keys.json` com os token's das duas API's nas suas respectivas pastas.
4. Instalar as dependencia na pasta googleAPI com o comando:`pip install -r requirements.txt`

### Como usar:
1. Clone o projeto: `git clone https://github.com/igorgbr/PR-google-with-notion.git`
2. Acesse o projeto: `cd PR-google-with-notion `
3. Crie a planilha de acordo com o exemplo abaixo:
[Google Sheet](imgs/sheets.png "Exemplo de planilha")
4. Crie uma página no notion de acordo com o exemplo:
[Notion](imgs/notion.png "Exemplo de Página no Notion") 

Na raiz do projeto temos o arquivo main.py com um exemplo de código, substitua a o valor da constante `SPREADSHEET_ID` na linha 6 de acordo com o ID da planilha que você ira utilizar, ná dúvida assista este [video](https://youtu.be/Urh5BQmssJs).


#### Call to Action:
Vamos deixar o projeto mais amigavel! <br>
Contribua com seu PR! 💚    
