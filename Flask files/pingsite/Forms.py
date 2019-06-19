from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, Length

class Lugarform(FlaskForm):
    lugarF = SelectField('Lugar: ', choices=[
        ('01','Auditório'),('02','Banheiro masculino (térreo)'),('03','Banheiro feminino (térreo)'),
        ('04','Banheiro masculino (escadas-térreo)'),('05','Banheiro feminino (escadas-térreo)'),
        ('06','Banheiro masculino (1º andar)'),('07','Banheiro feminino (1º andar)'),
        ('08','Banheiro masculino (2º andar)'),('09','Banheiro feminino (2º andar)'),
        ('10','Banheiro masculino (3º andar)'),('11','Banheiro feminino (3º andar)'),
        ('12','Banheiro masculino (4º andar)'),('13','Banheiro feminino (4º andar)'),
        ('14','Banheiro acessibilidade (térreo)'),('15','Banheiro acessibilidade (2º andar)'),
        ('16','Diretoria - Carol Salgado'),('17','Diretoria - Felipe Furtado'),('18','Impressora Color - Secretaria'),
        ('19','Impressora P&B - Secretaria'),('20','Impressora - Proj. Educacionais'),
        ('21','Relógio de Ponto - Corredor (térreo)'),('21','Sala 1'),('22','Sala 2'),('23','Sala 3'),
        ('24','Sala 4'),('25','Sala 5'),('26','Sala 6'),('27','Sala 7'),('28','Sala 8')])
    submit = SubmitField('Entrar com sua conta CESAR')

class Loginform(FlaskForm):
    nomeF = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    hole = SelectField('buraco', choices=[('B1','@cesar.school'),('B2','@cesar.org.br')])
    submit = SubmitField('Confirmar')
class ProblemasForm(FlaskForm):
    problemas=SelectField('Problemas:', choices=[
        ('A0','Projetor'),('A1','Ar condicionado não funciona corretamente'),('A2','Cadeira quebrada'),
        ('A3','Caixa de som não funciona'),('A4','Lâmpada apagada ou piscando'),('A5','Microfone não funciona'),
        ('A6','Porta com defeito'),('A7','Preciso de um adaptador ou cabo'),('A8','Projetor não funciona'),
        ('A9','Rede cabeada não funciona'),('A10','Rede wifi não funciona'),('A11','TV não funciona'),
        ('A12','Outros')])
    extra = StringField ('Comentario')
    botao =  SubmitField('Reportar')
