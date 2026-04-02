# Dashboard Brasileirão Série A

Pipeline ETL e dashboard interativo no Power BI para o Campeonato Brasileiro Série A,
com dados em tempo real de classificação, resultados e estatísticas de jogadores.

## 📊 Visão Geral

| Página | Conteúdo |
|---|---|
| Geral | tabela de classificação, resultados da rodada, próximos jogos, artilheiros e assistências |
| Por Time | vitórias/empates/derrotas, saldo de gols, desempenho casa/fora, estatísticas de jogadores |

## Pipeline
```
API-Football-Data → Python (pandas) → Excel → Power BI
```

1. **Extração** — coleta de dados ao vivo via API-Football-Data (jogos, tabela, estatísticas)
2. **Transformação** — limpeza e estruturação em DataFrames com pandas, exportação para Excel
3. **Carregamento** — conexão do Excel com Power BI, criação de gráficos dinâmicos e filtros interativos

## 🛠️ Tecnologias

| Ferramenta | Uso |
|---|---|
| Python | extração e transformação dos dados |
| Pandas | limpeza e estruturação |
| Excel | camada intermediária para conexão com Power BI |
| Power BI | visualização e dashboard interativo |
| API-Football-Data | fonte de dados em tempo real |

## ▶️ Como executar
```bash
pip install -r requirements.txt
python criando_planilhas.py
```
Abra o arquivo `DashboardBrasileirao.pbix` no Power BI Desktop.
