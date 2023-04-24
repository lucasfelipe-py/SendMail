from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

# Lendo arquivo TXT que contém a senha gerada pelo GMAIL
email_senha = open('senha.txt', 'r').read()

# Adicionando informações cabeçalho e-mail em variáveis
email_origem = 'seuemail@gmail.com' # Alterar (precisa ser o da conta com a senha gerada)
email_destino = ('emaildestino@gmail.com') # Alterar
assunto = 'Teste'

# Lendo arquivo TXT que contém o conteúdo do e-mail
body = open('corpo_email_html.txt', 'r').read()
# body = open('corpo_email.txt', 'r').read() -> Sem HTML

# Instanciando novo objeto da classe EmailMessage
mensagem = EmailMessage()

# Definindo as informações conforme a classe exige
mensagem["From"] = email_origem
mensagem["To"] = email_destino
mensagem["Subject"] = assunto

# Utilizando mimetypes para decodificar imagem que será anexada
anexo_path = 'imagem.png'
mime_type, mime_subtype = mimetypes.guess_type(anexo_path)[0].split('/')

# Setando corpo e-mail
mensagem.set_content(body, subtype='html')
# mensagem.set_content(body) -> Sem HTML

# Utilizando o ssl para criar o contexto padrão de conexão
safe = ssl.create_default_context()

# Anexando imagem decodificada pelo mimetypes
with open(anexo_path, 'rb') as ap:
    mensagem.add_attachment(
        ap.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo_path
    )

# Estabelecendo a conexão e enviando o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())