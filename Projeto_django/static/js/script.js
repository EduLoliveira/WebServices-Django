
// Máscaras para os campos
function mascaraCnpj(cnpj) {
    cnpj = cnpj.replace(/\D/g, '');
    cnpj = cnpj.replace(/^(\d{2})(\d)/, '$1.$2');
    cnpj = cnpj.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
    cnpj = cnpj.replace(/\.(\d{3})(\d)/, '.$1/$2');
    cnpj = cnpj.replace(/(\d{4})(\d)/, '$1-$2');
    return cnpj.substring(0, 18);
}

function mascaraTelefone(telefone) {
    telefone = telefone.replace(/\D/g, '');
    if (telefone.length > 10) {
        telefone = telefone.replace(/^(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
    } else {
        telefone = telefone.replace(/^(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
    }
    return telefone.substring(0, 15);
}

function mascaraCep(cep) {
    cep = cep.replace(/\D/g, '');
    cep = cep.replace(/^(\d{5})(\d)/, '$1-$2');
    return cep.substring(0, 9);
}

// Aplicar máscaras enquanto digita
document.getElementById('cnpj').addEventListener('input', function() {
    this.value = mascaraCnpj(this.value);
});

document.getElementById('telefone').addEventListener('input', function() {
    this.value = mascaraTelefone(this.value);
});

document.getElementById('cep').addEventListener('input', function() {
    this.value = mascaraCep(this.value);
});

// Validação de CNPJ
document.getElementById('cnpj').addEventListener('blur', function() {
    const cnpjField = this;
    const cnpj = cnpjField.value.replace(/\D/g, '');
    const feedback = document.getElementById('cnpjFeedback');
    
    if (cnpj.length === 14) {
        fetch(`/api/valida-cnpj/?cnpj=${cnpj}`)
            .then(response => {
                if (!response.ok) throw new Error('Erro na requisição');
                return response.json();
            })
            .then(data => {
                if (data.valido) {
                    cnpjField.classList.add('is-valid');
                    cnpjField.classList.remove('is-invalid');
                    feedback.textContent = '';
                    document.getElementById('nome').value = data.nome || '';
                } else {
                    cnpjField.classList.add('is-invalid');
                    cnpjField.classList.remove('is-valid');
                    feedback.textContent = data.erro || 'CNPJ inválido';
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                feedback.textContent = 'Erro ao validar CNPJ';
            });
    } else if (cnpj.length > 0) {
        cnpjField.classList.add('is-invalid');
        feedback.textContent = 'CNPJ deve ter 14 dígitos';
    }
});

        // Validação do formulário
        (function() {
            'use strict'
            var forms = document.querySelectorAll('.needs-validation')
            Array.prototype.slice.call(forms)
                .forEach(function(form) {
                    form.addEventListener('submit', function(event) {
                        if (!form.checkValidity()) {
                            event.preventDefault()
                            event.stopPropagation()
                        }
                        form.classList.add('was-validated')
                    }, false)
                })
        })()

//Utilizando as API's
// Consulta CEP
document.getElementById('cep').addEventListener('blur', function() {
    const cepField = this;
    const cep = cepField.value.replace(/\D/g, '');
    const feedback = document.getElementById('cepFeedback');
    
    if (cep.length === 8) {
        fetch(`/api/consulta-cep/?cep=${cep}`)
            .then(response => {
                if (!response.ok) throw new Error('Erro na requisição');
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    cepField.classList.add('is-invalid');
                    feedback.textContent = data.error;
                } else {
                    cepField.classList.add('is-valid');
                    cepField.classList.remove('is-invalid');
                    feedback.textContent = '';
                    
                    document.getElementById('endereco').value = data.endereco || '';
                    document.getElementById('bairro').value = data.bairro || '';
                    
                    // Preenche estado e cidade
                    const estadoSelect = document.getElementById('estado');
                    estadoSelect.value = data.estado || '';
                    
                    // Dispara o evento change do estado para carregar cidades
                    if (data.estado) {
                        const event = new Event('change');
                        estadoSelect.dispatchEvent(event);
                        
                        // Espera carregar as cidades antes de selecionar
                        setTimeout(() => {
                            const cidadeSelect = document.getElementById('cidade');
                            cidadeSelect.value = data.cidade || '';
                        }, 500);
                    }
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                feedback.textContent = 'Erro ao consultar CEP';
            });
    } else if (cep.length > 0) {
        cepField.classList.add('is-invalid');
        feedback.textContent = 'CEP deve ter 8 dígitos';
    }
});

// Carrega estados do IBGE
document.addEventListener('DOMContentLoaded', function() {
    fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
        .then(response => response.json())
        .then(estados => {
            const select = document.getElementById('estado');
            estados.sort((a, b) => a.nome.localeCompare(b.nome)).forEach(estado => {
                const option = document.createElement('option');
                option.value = estado.sigla;
                option.textContent = estado.nome;
                select.appendChild(option);
            });
        });
});

// Carrega cidades quando estado é selecionado
document.getElementById('estado').addEventListener('change', function() {
    const uf = this.value;
    const cidadeSelect = document.getElementById('cidade');
    
    if (uf) {
        cidadeSelect.disabled = false;
        fetch(`/api/lista-cidades/${uf}/`)
            .then(response => response.json())
            .then(data => {
                cidadeSelect.innerHTML = '<option value="">Selecione...</option>';
                data.cidades.forEach(cidade => {
                    const option = document.createElement('option');
                    option.value = cidade.nome;
                    option.textContent = cidade.nome;
                    cidadeSelect.appendChild(option);
                });
            });
    } else {
        cidadeSelect.disabled = true;
        cidadeSelect.innerHTML = '<option value="">Selecione o estado primeiro</option>';
    }
});