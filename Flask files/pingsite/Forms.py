from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

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