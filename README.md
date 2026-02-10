# Conversão Decimal para Binário e Hexadecimal

Programas em Python que convertem números decimais para binário e hexadecimal.

**Autor:** Pedro do Couto Rosa Canova

## Descrição

Este projeto contém programas que convertem números decimais para suas representações binária e hexadecimal usando algoritmos de divisões sucessivas.

## Arquivos

- **conversao.py** - Converte o número decimal 24015709
- **conversao2.py** - Converte o número decimal 24015032

## Como Executar

```bash
python conversao.py
# ou
python conversao2.py
```

## Resultados

### conversao.py (24015709)
- **Binário:** 1011011100111001101011101
- **Binário em quartetos:** 1 0110 1110 0111 0011 0101 1101
- **Hexadecimal:** 16E735D
- **Quantidade de bits:** 25

### conversao2.py (24015032)
- **Binário:** 1011011100111000010111000
- **Binário em quartetos:** 1 0110 1110 0111 0000 1011 1000
- **Hexadecimal:** 16E70B8
- **Quantidade de bits:** 25

## Funcionalidades

- Implementação manual dos algoritmos de conversão
- Separação do binário em quartetos para melhor legibilidade
- Verificação usando funções nativas do Python (`bin()` e `hex()`)
- Exibição formatada dos resultados
