import streamlit as st
from streamlit_option_menu import option_menu
from functions import *

st.session_state.user_email = st.context.headers.get("X-Forwarded-Email")
user_access_token = st.context.headers.get('X-Forwarded-Access-Token')


# Configurações iniciais
st.set_page_config(
    page_title="Mini Cientista",
    page_icon="https://www.sicredi.com.br/static/home/favicon.ico",
    layout="wide", 
    menu_items={
        "Get help": "https://teams.microsoft.com/l/chat/0/0?users=nicolas_santos@sicredi.com.br,matos_renan@sicredi.com.br",
        "About": "Aplicativo desenvolvido pela Engenharia de Dados do Time de Associação e Contas."
    }
)

# Tira o botão fullscrean dos elementos
disable_fs = '''
<style>
button[title="View fullscreen"]{visibility: hidden; display: none;}
.st-emotion-cache-1u2dcfn{visibility: hidden; display: none;}
.st-emotion-cache-gi0tri {visibility: hidden; display: none;}
</style>
'''
st.markdown(disable_fs, True)

# Defaults de sessão
if "etapa_atual" not in st.session_state:
    st.session_state.etapa_atual = 1


def on_change(key):
    st.session_state.etapa_atual = int(key)

# Função do Menu do APP  
with st.sidebar:
    st.image("assets/img/logo_gold.png")
    st.session_state.selected = option_menu (
        menu_title = "",
        options = [
            "Projeção",
            "Análise de Sentimento",
            "Classificação",
            "Extração de Entidade",
            "Geração de Texto",
            "Tradução",
            "Sumarização",
            "Correção de Gramática",
            "Detecção de Idioma",
            "Genie Chat",
            "AutoML",
            "Sobre"
        ],
        on_change = on_change, key = '1',
        styles={
            "container": {"background-color": "rgba(255, 255, 255, 0)"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "17px", "text-align": "left"},
            "nav-link-selected": {"font-size": "19px", "background-color": "#3FA110"}}
        )

if st.session_state.selected == "Projeção":
    st.markdown("## 🚧 Página em construção... 🚧")
    st.write("Este aplicativo foi desenvolvido pela Engenharia de Dados do Time de Associação e Contas para acelerar a criação e alteração de tabelas dentro da Camada Gold.")
    st.write("Para mais informações sobre como utilizar o aplicativo e como criar ou alterar tabelas de forma eficiente, visite nossa [Wiki](https://wiki.sicredi.io/pages/viewpage.action?pageId=350389058) e [GIT](https://gitlab.sicredi.net/camada-gold/camada_gold_app/app_gold)")
elif st.session_state.selected == "Análise de Sentimento":
    analyze_sentiment()
elif st.session_state.selected == "Classificação":
    classify()
elif st.session_state.selected == "Extração de Entidade":
    extract_entities()
elif st.session_state.selected == "Geração de Texto":
    gen_text()
elif st.session_state.selected == "Tradução":
    translate_text()
elif st.session_state.selected == "Sumarização":
    summarize_text()
elif st.session_state.selected == "Correção de Gramática":
    fix_grammar_page()
elif st.session_state.selected == "Detecção de Idioma":
    detect_language_page()
elif st.session_state.selected == "Genie Chat":
    genie_chat()
elif st.session_state.selected == "AutoML":
    automl_page()
else:
    st.markdown("## 🚧 Página em construção... 🚧")
    st.write("Este aplicativo foi desenvolvido pela Engenharia de Dados do Time de Associação e Contas para acelerar a criação e alteração de tabelas dentro da Camada Gold.")
    st.write("Para mais informações sobre como utilizar o aplicativo e como criar ou alterar tabelas de forma eficiente, visite nossa [Wiki](https://wiki.sicredi.io/pages/viewpage.action?pageId=350389058) e [GIT](https://gitlab.sicredi.net/camada-gold/camada_gold_app/app_gold)")
