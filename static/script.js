// Campos select2 nos filtros
$(document).ready(function(){
    $('#multiploBairro').select2({
        closeOnSelect: false,
        placeholder: 'Selecione os bairros',
        width: '300px',

        templateSelection: function (data, container) {
            // Marca os itens selecionados
            return $('<span class="item-selecionado">' + data.text + '</span>');
        }
    });
});

$(document).ready(function(){
    $('#multiploTipo').select2({
        closeOnSelect: false,
        placeholder: 'Selecione o Tipo do Imóvel',
        width: '300px',

        templateSelection: function (data, container) {
            // Marca os itens selecionados
            return $('<span class="item-selecionado">' + data.text + '</span>');
        }
    });
});

// Validações do form Fale Conosco
$(document).ready(function () {
    // Adiciona a máscara e permite apenas números no campo de telefone
    $('#telefone').on('input', function () {
        var telefone = $(this).val().replace(/\D/g, ''); // Remove caracteres não numéricos
        if (telefone.length > 10) {
            $(this).val('(' + telefone.substr(0, 2) + ') ' + telefone.substr(2, 5) + '-' + telefone.substr(7, 4));
        } else {
            $(this).val('(' + telefone.substr(0, 2) + ') ' + telefone.substr(2, 4) + '-' + telefone.substr(6, 4));
        }
    });

    // Permite apenas a digitação de números no campo de telefone
    $('#telefone').on('keypress', function (event) {
        var charCode = event.which;
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            event.preventDefault();
        }
    });

    // Adiciona validação do campo de e-mail
    $('#email').on('input', function () {
        var email = $(this).val();
        if (isValidEmail(email)) {
            $('#email-error').text(''); // Limpa a mensagem de erro se o e-mail for válido
        } else {
            $('#email-error').text('E-mail inválido');
        }
    });

    // Adiciona validação do campo de mensagem
    $('#mensagem').on('input', function () {
        var mensagem = $(this).val();
        if (mensagem.trim() !== '') {
            $('#mensagem-error').text(''); // Limpa a mensagem de erro se a mensagem não estiver vazia
        } else {
            $('#mensagem-error').text('Preencher este campo');
        }
    });

    // Adiciona validação do campo de telefone
    $('#telefone').on('input', function () {
        var telefone = $(this).val().replace(/\D/g, ''); // Remove caracteres não numéricos
        if (telefone.length >= 11) {
            $('#telefone-error').text(''); // Limpa a mensagem de erro se o telefone for válido
        } else {
            $('#telefone-error').text('Telefone inválido');
        }
    });

    // Validação do formulário antes de enviar
    $('.contato-form').on('submit', function () {
        if (validateForm()) {
            alert('Obrigado pelo contato! Sua mensagem foi enviada.');
        } else {
            alert('Por favor, corrija os campos antes de enviar.');
            return false; // Impede o envio do formulário se houver campos inválidos
        }
    });

    // Função para validar o formulário
    function validateForm() {
        var isValid = true;

        // Validação do campo de telefone
        var telefone = $('#telefone').val().replace(/\D/g, ''); // Remove caracteres não numéricos
        if (telefone.length < 11) {
            $('#telefone-error').text('Telefone inválido');
            isValid = false;
        } else {
            $('#telefone-error').text('');
        }

        // Validação do campo de e-mail
        var email = $('#email').val();
        if (!isValidEmail(email)) {
            $('#email-error').text('E-mail inválido');
            isValid = false;
        }

        // Validação do campo de mensagem
        var mensagem = $('#mensagem').val();
        if (mensagem.trim() === '') {
            $('#mensagem-error').text('Preencher este campo');
            isValid = false;
        }

        return isValid;
    }

    // Validação de e-mail
    function isValidEmail(email) {
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});


function confirmExclusao() {
    return confirm("Tem certeza que deseja excluir esta mensagem?");
}