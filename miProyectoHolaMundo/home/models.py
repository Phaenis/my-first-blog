from django.db import models
from django.db.models.fields import CharField

# Crea tus modelos aqui.
#-------------------------------------------------------------------
class Paciente(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Paciente")
        verbose_name_plural = ("Pacientes")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse("Paciente_detail", kwargs={"pk": self.pk})
    
#----------------------------------------------------------------------------
class Tessiu(models.Model):
    #Esta es una base de datos:
    #y se tiene que hacer una migracion de esta forma:
    #python manage.py makemigrations
    #python manage.py migrate
    Temperatura = models.FloatField()
    Color = models.FloatField()
    inflammation = models.FloatField(verbose_name="Inflamacion")
    #Esto es una llabe foranea
    name = models.ForeignKey(Paciente ,blank=True , null=True ,verbose_name = "nombre" , on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Tejido")
        verbose_name_plural = ("Tejidos")

    def __str__(self):
        if self.name is not None:
            return str(self.Temperatura) 
        else:
            return str(self.Temperatura)
    #def get_absolute_url(self):
    #    return reverse("Tejido_detail", kwargs={"pk": self.pk})
#--------------------------------------------------------------------------------
