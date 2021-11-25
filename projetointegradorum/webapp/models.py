from django.db import models

# Create your models here.
OPCOES_CHOICES = (
    ('Conforme', 'Conforme'),
    ('Não conforme', 'Não conforme'),
    ('Não se aplica', 'Não se aplica'),
)
class MeuFormulario(models.Model):
    usina = models.CharField(max_length=50)
    datainsp = models.DateField()
    opcoes = models.CharField('Estado', max_length=13, choices=OPCOES_CHOICES)
    opcoes2 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes3 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes4 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes5 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes6 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes7 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes8 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes9 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes10 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes11 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes12 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes13 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes14 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    opcoes15 = models.CharField('Estado',max_length=13, choices=OPCOES_CHOICES)
    observacoes1 = models.CharField(max_length=250, blank=True) 