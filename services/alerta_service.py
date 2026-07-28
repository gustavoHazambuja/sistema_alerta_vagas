from services.matching_service import vaga_combina_com_alerta
from models.notificacao_model import Notificacao


def processar_nova_vaga(db, vaga, alertas_ativos):

    """
    Regra: quando uma vaga nova é cadastrada,
    percorre todos os alertas ativos e cria
    notificação para os que combinam.
    """

    notificacoes_criadas = []

    for alerta in alertas_ativos:
        if not vaga_combina_com_alerta(vaga, alerta):
            continue

        ja_existe = db.query(Notificacao).filter(
             Notificacao.usuario_id == alerta.usuario_id,
             Notificacao.vaga_id == vaga.id
        ).fist()

        if ja_existe:
             continue

        notificacao = Notificacao(
        usuario_id = alerta.usuario_id,
        vaga_id = vaga.id
        )
        db.add(notificacao)
        notificacoes_criadas.append(notificacao)

    db.commit()
    return notificacoes_criadas