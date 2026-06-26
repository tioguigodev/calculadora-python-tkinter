# Calculadora Python Tkinter
projeto em desenvolvimento.

## Objetivo
Criar uma calculadora gráfica utilizando Python e Tkinter.

## Status do Projeto

- [x] Estrutura inicial
- [x] Configuração da janela
- [x] Definição das cores
- [x] Botões iniciais
- [x] Botões finais
- [x] Operações matemáticas
- [ ] Tratamento de erros
- [ ] Interface final

## Diário de desenvolvimento

### Dia 1
- Criação do repositório no GitHub
- Criação do arquivo `calculadora.py`
- Importação da biblioteca Tkinter
- Criação da janela principal com `Tk()`
- Definição do título da aplicação
- Primeira execução da aplicação

### Dia 2
- Escolha de cores
- Definir o tamanho da janela
- Bloquear redimensionamento tamanho da janela
- Determinar tamanho de tela
- Determinar cor da tela

### Dia 3
- Criação dos frames da aplicação (frame_tela e frame_corpo)
- Separação da tela em visor e área de botões
- Posicionamento dor frames com grid()
- Criação dos primeiros botões da calculadora
- Aprindizado de frame(), grid() e place()
- Início de montagem da interface gráfica

### Dia 4
- Criação da váriavel tela = StringVar() para controlar o conteúdo exibido no visor.
- Criação da váriavel todas_entradas = '' para armazenar a expressão digitada pelo usuário
- Criação do visor digital ultilizando Label
- Associação visual do visor (cores, fonte, aliunhamento à direita e posicionamento)
- Início da implementação da função de entrada der dados com lamda
- Associação dos botões numéricos à função entrada()
- Inclusão de operações especiais:
   - Parénteses ( e )
   - Valor de pi (math.pi)
   - Raiz quadrada sqrt()
   - Potência ao quadrado **2
   - Porcentagem /100

### Dia 5
- Implementação da função entrada() para capturar clics nos botões e escrever na tela
- Exibição dos botões bo visor
- Teste das entradas com números e operações
- Ainda sem mostrar resultado
