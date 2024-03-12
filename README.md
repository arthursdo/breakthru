# Breakthru: Estratégia e Inteligência Artificial

## Sobre o Jogo
Breakthru é um jogo de estratégia para dois jogadores, desenvolvido por Alex Randolph e comercializado pela 3M em 1965. Semelhante ao Hnefatafl, envolve equipes desiguais com objetivos distintos em um tabuleiro de 11 × 11 casas. O jogo segue uma dinâmica semelhante à batalha naval, com estratégias comparáveis ao jogo de cerco de Hnefatafl.

## Discussão dos Resultados dos Diferentes Algoritmos
A implementação do algoritmo Minimax com poda alfa-beta tem demonstrado melhorias significativas na performance da inteligência artificial do jogo. Esse algoritmo permite que a IA avalie os movimentos disponíveis para alcançar a posição mais vantajosa no tabuleiro, com base em uma função de avaliação que considera a quantidade e a posição das peças para ambos os jogadores.

## Vantagens do Algoritmo Minimax com Poda Alfa-Beta
### Eficiência:
A poda alfa-beta reduz o número de nós avaliados, otimizando a busca e economizando recursos computacionais.

### Profundidade de Análise:
Com a poda alfa-beta, a IA pode explorar sequências de jogadas mais profundamente sem um aumento significativo no tempo de processamento.

### Adaptabilidade:
A função de avaliação adaptativa permite que a IA ajuste suas estratégias de acordo com as mudanças no tabuleiro, tornando-a adaptável a diferentes situações de jogo.

## Desafios e Limitações
### Complexidade Computacional:
Apesar da eficiência da poda alfa-beta, a complexidade computacional do Minimax pode resultar em tempos de espera mais longos, especialmente em jogos com grande profundidade de análise.

### Dependência da Função de Avaliação:
A eficácia da IA é fortemente influenciada pela precisão da função de avaliação, tornando crucial o desenvolvimento adequado e ajuste dos parâmetros de avaliação.

## Considerações Finais
O algoritmo Minimax com poda alfa-beta aprimora consideravelmente a jogabilidade da IA no Breakthru, permitindo que ela antecipe jogadas de forma eficiente. No entanto, a eficácia da IA está diretamente ligada à qualidade da função de avaliação. Uma função mal projetada pode comprometer suas decisões.
