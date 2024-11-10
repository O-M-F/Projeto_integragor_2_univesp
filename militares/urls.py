from django.urls import path
from . import views
from .views import (
    MilitarListView, MilitarDetailView, MilitarCreateView, MilitarUpdateView, MilitarDeleteView,
    BeneficiarioCreateView, BeneficiarioUpdateView, BeneficiarioDeleteView, mover_para_finalizados,
    view_tb_vencimentos, editar_valor_tb_vencimentos, edit_tb_vencimento,
    ListaMemoriaisView, DetalhesMemorialView, EditarMemorialView, CriarMemorialView, criar_memorial, tela_memorial, detalhes_militar, militares_finalizados, militar_finalizado_detail, gerar_memorial, salvar_memorial_pdf, DeletarMemorialView
)

app_name = 'militares'

urlpatterns = [
    path('', MilitarListView.as_view(), name='militar_list'),
    path('<int:pk>/', MilitarDetailView.as_view(), name='militar_detail'),
    path('novo/', MilitarCreateView.as_view(), name='militar_create'),
    path('<int:pk>/editar/', MilitarUpdateView.as_view(), name='militar_update'),
    path('<int:pk>/deletar/', MilitarDeleteView.as_view(), name='militar_delete'),
    path('<int:pk>/beneficiario/novo/', BeneficiarioCreateView.as_view(), name='beneficiario_create'),
    path('<int:pk>/beneficiario/<int:pk_beneficiario>/editar/', BeneficiarioUpdateView.as_view(), name='beneficiario_update'),
    path('<int:pk>/beneficiario/<int:pk_beneficiario>/deletar/', BeneficiarioDeleteView.as_view(), name='beneficiario_delete'),
    path('mover_para_finalizados/<int:pk>/', mover_para_finalizados, name='mover_para_finalizados'),
    path('tb_vencimentos/', view_tb_vencimentos, name='view_tb_vencimentos'),
    path('tb_vencimentos/editar/', editar_valor_tb_vencimentos, name='editar_valor_tb_vencimentos'),
    path('tb_vencimentos/<str:codigo>/editar/', edit_tb_vencimento, name='edit_tb_vencimento'),
    path('memoriais/', ListaMemoriaisView.as_view(), name='lista_memoriais'),
    path('memoriais/<int:pk>/', DetalhesMemorialView.as_view(), name='detalhes_memorial'),
    path('memoriais/<int:pk>/editar/', EditarMemorialView.as_view(), name='editar_memorial'),
    path('memoriais/novo/', CriarMemorialView.as_view(), name='criar_memorial'),
    path('tela_memorial/', tela_memorial, name='tela_memorial'),
    path('detalhes_militar/<int:pk>/', detalhes_militar, name='detalhes_militar'),
    path('memoriais/criar/<int:militar_id>/', criar_memorial, name='criar_memorial_com_militar'),
    path('militares_finalizados/', militares_finalizados, name='militares_finalizados'),
    path('militar_finalizado/<str:re>/', militar_finalizado_detail, name='militar_finalizado_detail'),
    path('gerar_memorial/<int:pk>/', gerar_memorial, name='gerar_memorial'),
    path('salvar_memorial_pdf/<int:pk>/', salvar_memorial_pdf, name='salvar_memorial_pdf'),
    path('memoriais/novo/<int:pk>/', views.criar_memorial, name='criar_memorial'),
    path('memoriais/<int:pk>/editar/', EditarMemorialView.as_view(), name='editar_memorial'),
    path('memoriais/<int:pk>/deletar/', DeletarMemorialView.as_view(), name='deletar_memorial')


]

militares_finalizados_urlpatterns = [


]
