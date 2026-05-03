# Como executar o projeto

Este arquivo contém as instruções para clonar, instalar as dependências e executar o projeto localmente.

## 1. Clonar o repositório

Usando SSH:

```bash
git clone git@github.com:printfgabriel/Mapa-Comida-de-Buteco.git
```

Ou, usando HTTPS:

```bash
git clone https://github.com/printfgabriel/Mapa-Comida-de-Buteco.git
```

Depois, entre na pasta do projeto:

```bash
cd Mapa-Comida-de-Buteco
```

## 2. Criar o ambiente virtual

No Linux ou Mac:

```bash
python3 -m venv venv
```

No Windows:

```bash
python -m venv venv
```

## 3. Ativar o ambiente virtual

No Linux ou Mac:

```bash
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

Após a ativação, o terminal deve exibir algo parecido com:

```bash
(venv) usuario@computador:~/Mapa-Comida-de-Buteco$
```

## 4. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## 5. Executar o projeto

Execute o arquivo principal:

```bash
python main.py
```

Em alguns sistemas Linux, pode ser necessário usar:

```bash
python3 main.py
```

Depois disso, o terminal deve exibir um endereço local semelhante a:

```text
http://127.0.0.1:8050/
```

Abra esse endereço no navegador para acessar a aplicação.

## Observações importantes

A pasta `data` deve estar presente no projeto, contendo os arquivos necessários para o carregamento dos dados e do mapa.

Em especial, os arquivos abaixo não devem ser removidos:

```text
data/butecos_com_coords.csv
data/bairros_bh.geojson
```

O arquivo `data/butecos_com_coords.csv` contém os bares com suas respectivas coordenadas geográficas. O arquivo `data/bairros_bh.geojson` é usado para carregar os limites dos bairros no mapa.

## Possíveis problemas

### Erro: `python: command not found`

Em alguns sistemas Linux, o comando `python` pode não estar disponível. Nesse caso, use `python3`:

```bash
python3 main.py
```

ou:

```bash
python3 -m venv venv
```

### Erro ao criar o ambiente virtual no Linux

Se ocorrer erro ao executar:

```bash
python3 -m venv venv
```

instale o pacote necessário:

```bash
sudo apt update
sudo apt install python3-venv
```

Depois, tente criar o ambiente novamente:

```bash
python3 -m venv venv
```

### Erro de biblioteca não encontrada

Verifique se o ambiente virtual está ativado e reinstale as dependências:

```bash
pip install -r requirements.txt
```

### Porta 8050 já está em uso

Se a aplicação não iniciar porque a porta `8050` já está ocupada, encerre a execução anterior no terminal e rode o projeto novamente.
