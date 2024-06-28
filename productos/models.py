from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto         = models.IntegerField(primary_key=True, max_length=10)
    nombre_producto     = models.CharField(max_length=30)
    id_categoria        = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='id_categoria')
    precio              = models.IntegerField(max_length=10)
    descripcion         = models.CharField(max_length=200)
    foto                = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return str(self.nombre_producto)

class Categoria(models.Model):
    id_categoria        = models.AutoField(db_column='id_categoria',primary_key=True)
    categoria           = models.CharField(max_length=20,null=False)

    def __str__(self):
        return str(self.categoria)