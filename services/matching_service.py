
def vaga_combina_com_alerta(vaga, alerta) -> bool:

     """
    Regra de negócio principal do sistema:
    uma vaga é compatível com um alerta se TODOS os
    critérios preenchidos no alerta forem satisfeitos.
    Critérios em branco (None) são ignorados.
    """

     if not alerta.ativo:
          return False

     if alerta.palavra_chave:
          if alerta.palavra_chave.lower() not in vaga.titulo.lower():
               return False

     if alerta.localizacao:
          if alerta.localizacao.lower() != vaga.localizacao.lower():
               return False
     if alerta.modalidade:
          if alerta.modalidade.lower() != vaga.modalidade.lower():
               return False

     if alerta.salario_min_desejado:
          if vaga.salario_min is None or vaga.salario_min < alerta.salario_min_desejado:
               return False

     return True