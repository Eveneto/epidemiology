# Simulação Epidemiológica com Autômatos Celulares

## Descrição
Este projeto implementa uma simulação epidemiológica baseada no modelo SIR (Suscetível-Infectado-Recuperado) utilizando autômatos celulares. A simulação ocorre em uma grade bidimensional, onde células representam indivíduos e seguem regras locais para propagação da infecção.

## Como Funciona
- Cada célula pode estar em um dos três estados: **Suscetível**, **Infectado** ou **Recuperado**.
- Um indivíduo infectado pode infectar vizinhos com uma determinada probabilidade.
- Indivíduos infectados se recuperam após um tempo fixo.
- A simulação evolui em etapas discretas, exibindo a progressão da doença.

## Requisitos
Instale as dependências utilizando o seguinte comando:

```sh
pip install -r requirements.txt


