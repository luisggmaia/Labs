# Investigação Experimental dos Efeitos do Alongamento, Enflechamento e Afilamento sobre o Comportamento Aerodinâmico de Asas Finitas

## Descrição

Este repositório contém os materiais desenvolvidos para o estudo experimental da influência de parâmetros geométricos de asas sobre suas características aerodinâmicas.

Foram investigados os efeitos de:

- Alongamento (Λ);
- Enflechamento (φ);
- Afilamento (λ);

sobre os coeficientes aerodinâmicos de sustentação (CL), arrasto (CD) e momento (CM), bem como sobre a posição do centro aerodinâmico e a eficiência aerodinâmica das configurações ensaiadas.

Os resultados experimentais foram comparados com previsões teóricas obtidas a partir da Teoria da Linha Sustentadora de Prandtl e de modelos clássicos da aerodinâmica incompressível.

---

## Objetivos

Os principais objetivos do trabalho foram:

- Caracterizar experimentalmente o comportamento aerodinâmico de asas finitas;
- Avaliar a influência do alongamento sobre sustentação, arrasto induzido e eficiência aerodinâmica;
- Investigar os efeitos do enflechamento sobre a curva de sustentação, o estol e a posição do centro aerodinâmico;
- Analisar a influência do afilamento sobre a distribuição de sustentação e as características de estol;
- Comparar resultados experimentais com previsões teóricas clássicas.

---

## Relatório

O relatório apresenta:

- Fundamentação teórica;
- Metodologia experimental;
- Tratamento de dados;
- Discussão dos resultados;
- Comparação entre teoria e experimento.

## Notebook de Análise

O notebook contém:

- Importação e organização dos dados experimentais;
- Cálculo das propriedades do ar;
- Determinação dos parâmetros geométricos das asas;
- Ajustes lineares e quadráticos;
- Determinação de:
  - CLα;
  - Polar de arrasto;
  - Fator de eficiência de Oswald;
  - Centro aerodinâmico;
- Geração automática das figuras utilizadas no relatório.

---

## Principais Resultados

### Alongamento

- O coeficiente de sustentação angular aumenta com o alongamento;
- O arrasto induzido diminui para um mesmo coeficiente de sustentação;
- A eficiência aerodinâmica aumenta significativamente;
- O centro aerodinâmico permanece próximo de 25% da corda média aerodinâmica.

### Enflechamento

- O enflechamento reduz a inclinação da curva de sustentação;
- O estol ocorre em ângulos de ataque mais elevados;
- O centro aerodinâmico desloca-se para jusante;
- Surgem efeitos importantes sobre o momento de arfagem, incluindo tendências de *pitch-up* para grandes enflechamentos.

### Afilamento

- O afilamento exerce pouca influência sobre CLα;
- O centro aerodinâmico desloca-se para posições mais posteriores;
- O estol torna-se mais gradual;
- As diferenças de eficiência aerodinâmica foram pequenas nas condições experimentais analisadas.

---

## Referências

1. Anderson, J. D. *Fundamentals of Aerodynamics*. 6th Edition. McGraw-Hill, 2017.
2. Schlichting, H.; Truckenbrodt, E. *Aerodynamics of the Airplane*. McGraw-Hill, 1979.
3. Helmbold, H. B. *Zur Theorie der Tragflügel geringer Streckung*. 1942.
4. Brederode, V. de. *Aerodinâmica Incompressível: Fundamentos*. UERJ, 2003.

---

## Ferramentas Utilizadas

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- Jupyter Notebook
- LaTeX

