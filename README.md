# 🔍 Case de Redução de Inadimplência com Machine Learning

Este projeto tem como objetivo aplicar técnicas de aprendizado de máquina para prever inadimplência de clientes e propor ações que reduzam a taxa de inadimplência de **35% para abaixo de 25%**.

---

## 📁 Estrutura do Projeto

```
inadimplencia_case/
│
├── data/
│   ├── raw/           # Dados brutos exportados do PostgreSQL
│   ├── processed/     # Dados tratados e prontos para modelagem
│   └── models/        # Modelos treinados salvos (.pkl)
│
├── notebooks/
│   ├── 01_exploracao_dados.ipynb
│   ├── 02_preprocessamento.ipynb
│   ├── 03_modelagem_avaliacao.ipynb
│   └── 04_simulacao_impacto_modelo.ipynb
│
├── reports/
│   └── figures/       # Gráficos gerados para análise
│
├── src/               # Código fonte modular (data_processing, modeling, evaluation, DB_connection)
│
├── .env               # Variáveis de ambiente (se necessário)
├── .gitignore         # Arquivos ignorados pelo Git
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```

---

## 🧪 Tecnologias utilizadas

- Python 3.10+
- Pandas, NumPy, Scikit-learn
- Seaborn, Matplotlib
- JupyterLab
- PostgreSQL (exportação de dados)

---

## 📊 Resultados

- **Modelo final:** Random Forest Classifier
- **Acurácia:** 89%
- **Precision (inadimplentes):** 75%
- **Recall (inadimplentes):** 96%
- **Conclusão:**  
  O modelo é altamente eficiente para detectar inadimplentes reais (recall = 96%) e confiável para aprovar adimplentes (precision = 98%).  
  A aplicação estratégica do modelo pode **reduzir a inadimplência estimada de 35% para abaixo de 25%**, quando integrado a uma política de crédito baseada em risco.

---

## ▶️ Como executar

```bash
# Crie o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

# Instale dependências
pip install -r requirements.txt

# Execute os notebooks na pasta notebooks/
jupyter lab
```

---

## 📜 Licença

Este projeto está sob a licença MIT.
