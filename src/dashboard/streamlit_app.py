import streamlit as tf
import pandas as pd
import httpx
import asyncio

# Configuração de Layout de Alta Performance da Página
tf.set_page_config(
    page_title="Skill2Income AI - Dashboard Executivo",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Customizada CSS para Visual Clean (Filtro Luiz Café)
tf.markdown("""
    <style>
    .main-title { font-size:38px !important; font-weight: 800; color: #1E3A8A; margin-bottom: 5px; }
    .subtitle { font-size:18px !important; color: #4B5563; margin-bottom: 25px; }
    .metric-box { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #10B981; }
    .card-oportunidade { background-color: #FFFFFF; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 15px; border: 1px solid #E5E7EB; }
    </style>
""", unsafe_allowed_html=True)

# URL da API FastAPI (Mapeamento de Produção)
API_URL = "http://localhost:8000/api/v1/analyze"

async def call_ai_pipeline(usuario_id: str, raw_text: str):
    """Efetua a chamada assíncrona para a API de IA Core."""
    payload = {"usuario_id": usuario_id, "raw_text": raw_text}
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(API_URL, json=payload)
        response.raise_for_status()
        return response.json()

# ----------------- SIDEBAR: INPUTS & CONTEXTO -----------------
with tf.sidebar:
    tf.image("https://img.icons8.com/fluent/96/artificial-intelligence.png", width=80)
    tf.markdown("## **Skill2Income AI Engine**")
    tf.markdown("---")
    
    usuario_id = tf.text_input("ID do Usuário/Candidato:", value="usr_sergio_santos_2026")
    
    tf.markdown("### **Insumos de Entrada**")
    tipo_input = tf.radio("Selecione a fonte de análise:", ["Currículo / Perfil Profissional", "Respostas do Inventário DIO"])
    
    # Texto Padrão de Exemplo baseado no Perfil Sênior de Sérgio Santos
    default_text = """SÉRGIO LUIZ DOS SANTOS
Cientista de Dados | Soluções de Machine Learning Orientadas a Risco.
Mais de 20 anos de experiência em sistemas críticos e bancários (Bradesco).
Habilidades: Python, SQL, FastAPI, Streamlit, Power BI, Docker, Azure Databricks, Redução de Risco Operacional, Governança de Dados, Storytelling de Dados, Liderança Técnica."""
    
    raw_text = tf.text_area(
        "Cole o texto bruto aqui para inferência da IA:",
        value=default_text,
        height=300
    )
    
    btn_analisar = tf.button("🚀 Processar com IA", use_container_width=True)

# ----------------- PAINEL PRINCIPAL -----------------
tf.markdown('<p class="main-title">💰 Skill2Income AI</p>', unsafe_allowed_html=True)
tf.markdown('<p class="subtitle">Transforme competências técnicas, comportamentais e criativas em ativos financeiros mensuráveis.</p>', unsafe_allowed_html=True)

if btn_analisar:
    if not raw_text.strip():
        tf.warning("Por favor, insira um texto válido na barra lateral para iniciar a análise.")
    else:
        with tf.spinner("🤖 Os Motores de IA estão analisando o perfil e mapeando o mercado de trabalho..."):
            try:
                # Executa a pipeline assíncrona em ambiente síncrono do Streamlit
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(call_ai_pipeline(usuario_id, raw_text))
                
                # Extração dos dados limpos do JSON tipado pelo Pydantic
                skills = result["skills_identificadas"]
                plano = result["plano_monetizacao"]
                renda_estimada = result["potencial_renda_mensal_estimado"]
                
                # ----------------- ABA 1: BUSINESS PERFORMANCE (FOCO MEIGAROM) -----------------
                tf.markdown("### 📈 Impacto de Negócio & Retorno Financeiro")
                
                col1, col2 = tf.columns([1, 2])
                
                with col1:
                    tf.markdown(
                        f"""
                        <div class="metric-box">
                            <span style='font-size: 14px; color: #4B5563; font-weight: bold;'>POTENCIAL DE RENDA ESTIMADO</span><br>
                            <span style='font-size: 36px; font-weight: 800; color: #059669;'>R$ {renda_estimada:,.2f}</span><br>
                            <span style='font-size: 12px; color: #6B7280;'>Média calculada por projetos ativos de escopo fechado</span>
                        </div>
                        """, 
                        unsafe_allowed_html=True
                    )
                    tf.markdown("<br>", unsafe_allowed_html=True)
                    
                    # Gráfico de Distribuição das Habilidades Mapeadas
                    dados_grafico = {
                        "Categoria": ["Técnicas", "Comportamentais", "Criativas"],
                        "Quantidade": [len(skills["tecnicas"]), len(skills["comportamentais"]), len(skills["criativas"])]
                    }
                    df_skills = pd.DataFrame(dados_grafico)
                    tf.markdown("**Distribuição de Competências (Mapeamento DIO)**")
                    tf.bar_chart(df_skills.set_index("Categoria"), color="#1E3A8A")
                
                with col2:
                    tf.markdown("#### **Plano de Monetização Recomendado (Caminhos de Renda)**")
                    
                    if not plano:
                        tf.info("A IA não identificou canais imediatos de monetização para as entradas fornecidas.")
                    else:
                        for item in plano:
                            tf.markdown(f"""
                                <div class="card-oportunidade">
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="font-size: 18px; font-weight: bold; color: #1E3A8A;">🛠️ {item['servico']}</span>
                                        <span style="background-color: #D1FAE5; color: #065F46; padding: 5px 10px; border-radius: 15px; font-size: 14px; font-weight: bold;">
                                            R$ {item['ticket_medio_reais']:,.2f}
                                        </span>
                                    </div>
                                    <p style="margin-top: 10px; color: #374151;"><b>Onde vender:</b> {item['plataforma_sugerida']}</p>
                                    <p style="color: #6B7280; font-size: 14px;"><b>Justificativa de Mercado:</b> {item['justificativa_negocio']}</p>
                                </div>
                            """, unsafe_allowed_html=True)
                
                # ----------------- ABA 2: INVENTÁRIO DETALHADO (FOCO LUIZ CAFÉ) -----------------
                tf.markdown("---")
                tf.markdown("### 📂 Inventário Estruturado de Competências")
                
                tab_tec, tab_comp, tab_criat = tf.tabs([
                    f"💻 Técnicas ({len(skills['tecnicas'])})", 
                    f"🤝 Comportamentais ({len(skills['comportamentais'])})", 
                    f"🎨 Criativas ({len(skills['criativas'])})"
                ])
                
                with tab_tec:
                    tf.markdown("##### Hard Skills Detectadas")
                    tf.write(", ".join([f"`{sk}`" for sk in skills["tecnicas"]]))
                    
                with tab_comp:
                    tf.markdown("##### Soft Skills Detectadas")
                    tf.write(", ".join([f"`{sk}`" for sk in skills["comportamentais"]]))
                    
                with tab_criat:
                    tf.markdown("##### Habilidades Criativas / Conteúdo")
                    tf.write(", ".join([f"`{sk}`" for sk in skills["criativas"]]))
                    
            except httpx.HTTPStatusError:
                tf.error("Erro de comunicação: Certifique-se de que a API FastAPI está rodando em segundo plano (`uvicorn src.app.main:app --reload`).")
            except Exception as e:
                tf.error(f"Ocorreu um erro inesperado no processamento da interface: {str(e)}")

else:
    # Estado Inicial da Tela (Antes do clique no botão)
    tf.info("👈 Configure os parâmetros na barra lateral e clique em 'Processar com IA' para rodar o motor analítico.")
    
    # Demonstração de Storytelling para encantar o Tech Recruiter no primeiro acesso
    tf.markdown("---")
    tf.markdown("#### **Como Funciona a Arquitetura da Solução?**")
    col_a, col_b, col_c = tf.columns(3)
    with col_a:
        tf.markdown("##### **1. Ingestão e NLP Estrito**")
        tf.caption("A IA consome textos complexos e desestruturados (currículos ou inputs de questionários) e padroniza os dados utilizando Engenharia de Prompts estruturada via JSON Schema.")
    with col_b:
        tf.markdown("##### **2. Mapeamento de Mercado**")
        tf.caption("As competências são confrontadas com os motores de demanda de plataformas de economia aberta (Freelance, Mentorias, B2B), encontrando gargalos reais de clientes.")
    with col_c:
        tf.markdown("##### **3. Geração de Valor Financeiro**")
        tf.caption("O sistema calcula o ticket médio realista e justifica a oportunidade comercial, removendo o profissional da camada técnica pura e elevando-o para a camada de Solução.")
