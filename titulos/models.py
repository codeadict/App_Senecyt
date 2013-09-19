# -*- coding: utf-8 -*-
# Copyright (C) 2013 Dairon Medina (http://dairon.org)
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Description: Aplicación Móvil para consultas al SENECYT(www.senescyt.gob.ec)
from django.db import models


class Titulo(models.Model):
    """
    Modelo de Datos para Webservice de Títulos
    """
    nombres = models.CharField('NOMBRES', max_length=255, null=True, blank=True)
    cedula = models.CharField('CEDULA', max_length=10, null=True, blank=True)
    nombre_titulo = models.CharField('NOMBRE_TITULO', max_length=255, null=True, blank=True)
    institucion = models.CharField('INSTITUCION', max_length=255, null=True, blank=True)
    cod_registro = models.CharField('CODIGO DE REGISTRO', max_length=120, null=True, blank=True)
    nivel_carrera = models.CharField('DENOM NIVEL CARRERA', max_length=80, null=True, blank=True)
    tipo = models.CharField('TIPO', max_length=80, null=True, blank=True)

    texto = models.TextField('TEXTO', null=True, blank=True)



    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'

    def __unicode__(self):
        return self.nombres
