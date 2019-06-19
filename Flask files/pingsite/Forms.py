from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from pingsite.models import models
class Lugarform(FlaskForm):
        
    problemas=SelectField('Problemas:', choices=[
        ('Projetor','Projetor'),
        ('Ar condicionado não funciona corretamente','Ar condicionado não funciona corretamente'),
        ('Cadeira quebrada','Cadeira quebrada'),
        ('Caixa de som não funciona','Caixa de som não funciona'),
        ('Lâmpada apagada ou piscando','Lâmpada apagada ou piscando'),
        ('Microfone não funciona','Microfone não funciona'),
        ('Porta com defeito','Porta com defeito'),
        ('Preciso de um adaptador ou cabo','Preciso de um adaptador ou cabo'),
        ('Projetor não funciona','Projetor não funciona'),
        ('Rede cabeada não funciona','Rede cabeada não funciona'),
        ('Rede wifi não funciona','Rede wifi não funciona'),
        ('TV não funciona','TV não funciona'),
        ('Outros','Outros')])
    extra = StringField ('Comentario')

    lugarF = SelectField('Lugar: ', choices=[
        ('Auditório','Auditório'),('Banheiro masculino(térreo)','Banheiro masculino (térreo)'),
        ('Banheiro feminino(térreo','Banheiro feminino (térreo)'),
        ('Banheiro masculino(escadas-térreo)','Banheiro masculino (escadas-térreo)'),
        ('Banheiro feminino(escadas-térreo)','Banheiro feminino (escadas-térreo)'),
        ('Banheiro masculino (1º andar)','Banheiro masculino (1º andar)'),
        ('Banheiro feminino (1º andar)','Banheiro feminino (1º andar)'),
        ('Banheiro masculino (2º andar)','Banheiro masculino (2º andar)'),
        ('Banheiro feminino (2º andar)','Banheiro feminino (2º andar)'),
        ('Banheiro masculino (3º andar)','Banheiro masculino (3º andar)'),
        ('Banheiro feminino (3º andar)','Banheiro feminino (3º andar)'),
        ('Banheiro masculino (4º andar)','Banheiro masculino (4º andar)'),
        ('Banheiro feminino (4º andar)','Banheiro feminino (4º andar)'),
        ('Banheiro acessibilidade (térreo)','Banheiro acessibilidade (térreo)'),
        ('Banheiro acessibilidade (2º andar)','Banheiro acessibilidade (2º andar)'),
        ('Diretoria - Carol Salgado','Diretoria - Carol Salgado'),
        ('Diretoria - Felipe Furtado','Diretoria - Felipe Furtado'),
        ('Impressora Color - Secretaria','Impressora Color - Secretaria'),
        ('Impressora P&B - Secretaria','Impressora P&B - Secretaria'),
        ('Impressora - Proj. Educacionais','Impressora - Proj. Educacionais'),
        ('Relógio de Ponto - Corredor (térreo)','Relógio de Ponto - Corredor (térreo)'),
        ('Sala 1','Sala 1'),('Sala 2','Sala 2'),('Sala 3','Sala 3'),
        ('Sala 4','Sala 4'),('Sala 5','Sala 5'),('Sala 6','Sala 6'),
        ('Sala 7','Sala 7'),('Sala 8','Sala 8')])
    submit = SubmitField('Entrar com sua conta CESAR')

class Loginform(FlaskForm):
    nomeF = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    hole = SelectField('buraco', choices=[('@cesar.school','@cesar.school'),('@cesar.org.br','@cesar.org.br')])
    submit = SubmitField('Confirmar')

    def validate_email(self,email):
        user = Login.query.filter_by(email=nomeF).first()
        if user:
            raise ValidationError('Sua conta existe')