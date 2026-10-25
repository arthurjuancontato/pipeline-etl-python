from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    Organizador: int = Field(..., description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês do registro")
    Dia_da_Semana: str = Field(..., description="Dia da semana correspondente à data")
    Tipo_Dia: str = Field(..., description="Classificação do dia: útil, feriado, etc.")
    Objetivo: str = Field(..., description="Objetivo da campanha ou ação")
    Date: str = Field(..., description="Data da entrada no formato YYYY-MM-DD")
    AdSet_name: Optional[str] = Field(None, description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(0.0, ge=0, le=1200.00, description="Valor gasto no anúncio (mínimo 0, máximo 1200.00)")    
    Link_clicks: Optional[int] = Field(None, description="Número de cliques no link")
    Impressions: int = Field(0, description="Número de impressões do anúncio")
    Conversions: Optional[int] = Field(None, description="Número de conversões registradas")
    Segmentacao: Optional[str] = Field(None, description="Segmentação usada no anúncio")
    Tipo_de_Anuncio: str = Field(..., description="Tipo do anúncio")
    Fase: str = Field(..., description="Fase da campanha")