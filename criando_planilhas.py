import os, requests, pandas as pd
from arquivo_token import FOOTBALL_TOKEN

base_url = 'http://api.football-data.org/v4/'

headers = {
    'X-Auth-Token': FOOTBALL_TOKEN
}


def obter_dados(endpoint):
    url = base_url + endpoint

    response = requests.get(url, headers=headers)
       
    dados = response.json()
    return dados


tabela = {
    'Posição' : [],
    'Time': [],
    'Pontos': [],
    'Jogos': [],
    'Vitorias': [],
    'Empates': [],
    'Derrotas': [],
    'Saldo de Gols': []
}

nomes_alterados = {
    "Recife": "Sport",
    "Mineiro": "Atlético Mineiro"
}
def preenchendo_tabela():
    endpoint = 'competitions/BSA/standings'
    dados = obter_dados(endpoint)
    for time in dados['standings'][0]['table']:

        tabela["Posição"].append(time['position'])
        tabela['Time'].append(time['team']['shortName']) if time['team']['shortName'] not in nomes_alterados else tabela['Time'].append(nomes_alterados[time['team']['shortName']])
        tabela['Pontos'].append(time['points'])
        tabela['Jogos'].append(time['playedGames'])
        tabela['Vitorias'].append(time['won'])
        tabela['Empates'].append(time['draw'])
        tabela['Derrotas'].append(time['lost'])
        tabela['Saldo de Gols'].append(time['goalDifference'])
    
    df = pd.DataFrame.from_dict(tabela)
    caminho_arquivo = os.path.join('dados', 'TabelaBrasileirao.xlsx')
    df.to_excel(caminho_arquivo, index=False)


estatisticas_jogadores = {
    'Jogador': [],
    'Time': [],
    'Partidas': [],
    'Gols': [],
    'Assistências': []
}
def preenchendo_estatisticas():
    endpoint = 'competitions/BSA/scorers?limit=300'
    dados = obter_dados(endpoint)
    
    for jogador in dados['scorers']:
        estatisticas_jogadores['Jogador'].append(jogador['player']['name'])
        estatisticas_jogadores['Time'].append(jogador['team']['shortName']) if  jogador['team']['shortName'] not in nomes_alterados else estatisticas_jogadores['Time'].append(nomes_alterados[jogador['team']['shortName']])
        estatisticas_jogadores['Partidas'].append(jogador['playedMatches'])
        estatisticas_jogadores['Gols'].append(jogador['goals'])
        estatisticas_jogadores['Assistências'].append(jogador['assists'])

    df = pd.DataFrame.from_dict(estatisticas_jogadores)
    caminho_arquivo = os.path.join('dados', 'EstatisticasDosJogadores.xlsx')
    df.to_excel(caminho_arquivo, index=False)


# escudos = {
#     'Time': [],
#     'Escudo': []
# }
# def preenchendo_escudos():
#     endpoint = 'competitions/BSA/teams'
#     dados = obter_dados(endpoint)

#     for time in dados['teams']:
#         escudos['Time'].append(time['shortName'])
#         escudos['Escudo'].append(time['crest'])

#     print(escudos)
#     df = pd.DataFrame.from_dict(escudos)
#     df.to_excel("EscudosDosTimes.xlsx", index=False)
#     print(df)


rodadas_geral = {
    'Time da Casa': [],
    'Time de Fora': [],
    'Resultado': [],
    'Vencedor': [],
    'Matchday': []
}
def preenchendo_rodadas():
    endpoint = 'competitions/BSA/matches'
    dados = obter_dados(endpoint)
    partidas = dados['matches']

    status = []
    status_atual = "FINISHED"
    i = 0

    while status_atual == "FINISHED":
        status_atual = partidas[i]['status']
        rodadas_geral['Time da Casa'].append(partidas[i]['homeTeam']['shortName']) if partidas[i]['homeTeam']['shortName'] not in nomes_alterados else rodadas_geral['Time da Casa'].append(nomes_alterados[partidas[i]['homeTeam']['shortName']])
        # rodadas_geral['Time da Casa'].append(partidas[i]['homeTeam']['shortName'])
        rodadas_geral['Time de Fora'].append(partidas[i]['awayTeam']['shortName']) if partidas[i]['awayTeam']['shortName'] not in nomes_alterados else rodadas_geral['Time de Fora'].append(nomes_alterados[partidas[i]['awayTeam']['shortName']])
        # rodadas_geral['Time de Fora'].append(partidas[i]['awayTeam']['shortName'])
        rodadas_geral['Resultado'].append(f"{partidas[i]['score']['fullTime']['home'] if partidas[i]['score']['fullTime']['home'] != None else ""} - {partidas[i]['score']['fullTime']['away'] if partidas[i]['score']['fullTime']['away'] != None else ""}")
        if (partidas[i]['score']['winner']) == "HOME_TEAM":
            rodadas_geral['Vencedor'].append((partidas[i]['homeTeam']['shortName']))
        elif (partidas[i]['score']['winner']) == "AWAY_TEAM":
            rodadas_geral['Vencedor'].append((partidas[i]['awayTeam']['shortName']))
        elif (partidas[i]['score']['winner']) == "DRAW":
            rodadas_geral['Vencedor'].append("Empate")
        else:
            rodadas_geral['Vencedor'].append("  -  ")
        rodadas_geral['Matchday'].append(partidas[i]['matchday'])

        
        status.append(status_atual)
        i += 1
    
    df = pd.DataFrame.from_dict(rodadas_geral)
    caminho_arquivo = os.path.join('dados', 'Rodadas.xlsx')
    df.to_excel(caminho_arquivo, index=False)


elenco = {
    'Time': [],
    'Jogador': [],
    'Posição': []
}
def preenchendo_elenco():
    endpoint = 'competitions/BSA/teams'
    dados = obter_dados(endpoint)
    time = dados['teams']

    for i in range(len(time)):
        for j in range(len(time[i]['squad'])):
            elenco['Time'].append(time[i]['shortName']) if time[i]['shortName'] not in nomes_alterados else elenco['Time'].append(nomes_alterados[time[i]['shortName']])
            elenco['Jogador'].append(time[i]['squad'][j]['name'])
            elenco['Posição'].append(time[i]['squad'][j]['position'])

    df = pd.DataFrame.from_dict(elenco)
    caminho_arquivo = os.path.join('dados', 'Jogadores.xlsx')
    df.to_excel(caminho_arquivo, index=False)


preenchendo_tabela()
preenchendo_rodadas()
preenchendo_estatisticas()
preenchendo_elenco()

