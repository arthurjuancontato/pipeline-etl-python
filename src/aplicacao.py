import pandas as pd
import streamlit as st
from pydantic import ValidationError

from validador import PlanilhaVendas


def validar_dados(df):
    erros = []
    dados_validados = []

    for numero_linha, (_, row) in enumerate(df.iterrows(), start=2):
        try:
            # Converte valores ausentes do CSV para None
            dados = {
                coluna: None if pd.isna(valor) else valor
                for coluna, valor in row.to_dict().items()
            }

            registro_validado = PlanilhaVendas(**dados)
            dados_validados.append(registro_validado)

        except ValidationError as e:
            erros.append(f"Erro na linha {numero_linha}: {e}")

    return dados_validados, erros


def main():
    st.title("Validador de Dados de Campanhas")
    st.write("Envie um arquivo CSV para validação.")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo CSV",
        type=["csv"],
    )

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            # Ajusta os nomes das colunas para corresponder ao modelo
            df = df.rename(columns={
                "Tipo_de_Anúncio": "Tipo_de_Anuncio",
                "Segmentação": "Segmentacao",
            })

            st.write("Prévia dos dados:")
            st.dataframe(df.head())

            if st.button("Validar Dados"):
                with st.spinner("Validando dados..."):
                    dados_validados, erros = validar_dados(df)

                if erros:
                    st.error("Foram encontrados erros na validação:")
                    for erro in erros:
                        st.write(erro)
                else:
                    st.success("Todos os dados foram validados com sucesso!")
                    st.write(
                        f"Total de registros validados: {len(dados_validados)}"
                    )

                    df_validado = pd.DataFrame(
                        [
                            registro.model_dump()
                            for registro in dados_validados
                        ]
                    )

                    st.download_button(
                        label="Download dos dados validados",
                        data=df_validado.to_csv(index=False).encode("utf-8-sig"),
                        file_name="dados_validados.csv",
                        mime="text/csv",
                    )

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")


if __name__ == "__main__":
    main()