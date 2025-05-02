from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import requests
from .models import Empresa, Endereco
from .forms import EmpresaForm, EnderecoForm
from django.contrib import messages

def home(request):
    return render(request, 'empresa/home.html')

def nova_empresa(request):
    if request.method == 'POST':
        # Versão híbrida - trabalha com forms e request.POST direto
        empresa_form = EmpresaForm(request.POST)
        endereco_form = EnderecoForm(request.POST)
        
        if empresa_form.is_valid() and endereco_form.is_valid():
            try:
                endereco = Endereco(
                    cep=request.POST.get('cep'),
                    endereco=request.POST.get('endereco'),
                    numero=request.POST.get('numero'),
                    bairro=request.POST.get('bairro'),
                    cidade=request.POST.get('cidade'),
                    estado=request.POST.get('estado')
                )
                endereco.save()
                
                empresa = Empresa(
                    nome=request.POST.get('nome'),
                    cnpj=request.POST.get('cnpj'),
                    telefone=request.POST.get('telefone'),
                    endereco=endereco
                )
                empresa.save()
                
                messages.success(request, 'Empresa cadastrada com sucesso!')
                return redirect('listagem_empresas')
                
            except Exception as e:
                messages.error(request, f'Erro ao salvar: {str(e)}')
        else:
            messages.error(request, 'Corrija os erros no formulário')
    else:
        empresa_form = EmpresaForm()
        endereco_form = EnderecoForm()
    
    return render(request, 'empresa/nova_empresa.html', {
        'empresa_form': empresa_form,
        'endereco_form': endereco_form
    })

def listagem_empresas(request):
    if request.method == 'POST':
        # Mantendo a mesma lógica do seu código funcional
        nova_empresa = Empresa(
            nome=request.POST.get('nome'),
            cnpj=request.POST.get('cnpj'),
            telefone=request.POST.get('telefone')
        )
        endereco = Endereco(
            cep=request.POST.get('cep'),
            endereco=request.POST.get('endereco'),
            numero=request.POST.get('numero'),
            bairro=request.POST.get('bairro'),
            cidade=request.POST.get('cidade'),
            estado=request.POST.get('estado')
        )
        endereco.save()
        nova_empresa.endereco = endereco
        nova_empresa.save()
        return redirect('listagem_empresas')
    
    empresas = Empresa.objects.all().select_related('endereco')
    return render(request, 'empresa/listagem_empresas.html', {'empresas': empresas})

def editar_empresa(request, id):
    emp = get_object_or_404(Empresa, id=id)
    
    if request.method == 'POST':
        # Atualização direta como no seu código funcional
        emp.nome = request.POST.get('nome')
        emp.cnpj = request.POST.get('cnpj')
        emp.telefone = request.POST.get('telefone')
        emp.endereco.cep = request.POST.get('cep')
        emp.endereco.endereco = request.POST.get('endereco')
        emp.endereco.numero = request.POST.get('numero')
        emp.endereco.bairro = request.POST.get('bairro')
        emp.endereco.cidade = request.POST.get('cidade')
        emp.endereco.estado = request.POST.get('estado')
        
        emp.endereco.save()
        emp.save()
        messages.success(request, 'Empresa atualizada com sucesso!')
        return redirect('listagem_empresas')
    
    return render(request, 'empresa/editar_empresa.html', {'empresa': emp})

def excluir_empresa(request, id):
    emp = get_object_or_404(Empresa, id=id)
    if request.method == 'POST':
        emp.endereco.delete()
        emp.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('listagem_empresas')
    return render(request, 'empresa/confirmar_exclusao.html', {'empresa': emp})

# APIs (mantidas intactas)
def valida_cnpj(request):
    cnpj = request.GET.get('cnpj', '').replace('.', '').replace('/', '').replace('-', '')
    if len(cnpj) != 14:
        return JsonResponse({'valido': False, 'erro': 'CNPJ deve ter 14 dígitos'}, status=400)
    
    try:
        response = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}', timeout=10)
        data = response.json()
        return JsonResponse({
            'valido': data.get('status', '').upper() == 'OK',
            'nome': data.get('nome', ''),
            'situacao': data.get('situacao', '')
        })
    except Exception as e:
        return JsonResponse({'valido': False, 'erro': str(e)}, status=400)

def consulta_cep(request):
    cep = request.GET.get('cep', '').replace('-', '')
    if len(cep) != 8:
        return JsonResponse({'error': 'CEP deve ter 8 dígitos'}, status=400)
    
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        data = response.json()
        if data.get('erro'):
            return JsonResponse({'error': 'CEP não encontrado'}, status=404)
        return JsonResponse({
            'endereco': data.get('logradouro', ''),
            'bairro': data.get('bairro', ''),
            'cidade': data.get('localidade', ''),
            'estado': data.get('uf', '')
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def lista_cidades(request, uf):
    try:
        response = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')
        cidades = [{'nome': mun['nome']} for mun in response.json()]
        return JsonResponse({'cidades': cidades})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)