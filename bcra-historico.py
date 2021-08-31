#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Dolar History - Ambito Financiero Scrapping
# https://github.com/st1tch-bl/dolar-history
#
# Copyright 2021 St1tch3
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#
#Opciones:
#0 - Reservas Internacionales
#1 - Tasa de Política Monetaria (en n.a.)
#2 - Tasa de Política Monetaria (en e.a.)
#3 - Tasa fija de precancelación para depósitos con opción de cancelación anticipada en UVA (en n.a.)
#4 - Tasa mínima para plazos fijos de personas humanas hasta $1 millón (en n.a.)
#5 - Tasa mínima para plazos fijos de personas humanas hasta $1 millón (en e.a. para depósitos a 30 días)
#6 - BADLAR en pesos de bancos privados (en n.a.)
#7 - BADLAR en pesos de bancos privados (en e.a.)
#8 - TM20 en pesos de bancos privados (en n.a.)
#9 - Base monetaria - Total (en millones de pesos)
#10 - Circulación monetaria (en millones de pesos)
#11 - M2 privado, promedio móvil de 30 días, variación interanual (en )
#12 - Inflación mensual (variación en )
#13 - CER (Base 2.2.2002=1)
#14 - Unidad de Valor Adquisitivo (UVA) (en pesos -con dos decimales-, base 31.3.2016=14.05)
#15 - Unidad de Vivienda (UVI) (en pesos -con dos decimales-, base 31.3.2016=14.0


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


tipo="ee"
tipo = input('Ingrese opción: ')
url="0"
desde = input('Ingrese Fecha de inicio(en formato Año-Mes-Di­a, Ejemplo,2021-05-23): ')
hasta = input('Ingrese Fecha de fin(en formato Año-Mes-Dia, Ejemplo,2021-05-23): ')

url_base= "http://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?fecha_desde="+desde+"&fecha_hasta="+hasta
if tipo=="0":
#Reservas Internacionales
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=246&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Reservas+Internacionales+del+BCRA%A0%28en+millones+de+d%F3lares+-+cifras+provisorias+sujetas+a+cambio+de+valuaci%F3n%29"
if tipo=="1":
#Tasa de Política Monetaria (en n.a.)
  url="&B1=Enviar&primeravez=1&serie=7935&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Tasa+de+Pol%EDtica+Monetaria+%28en++n.a.%29"
#Tasa de Política Monetaria (en e.a.)
if tipo=="2":
  url="&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=7936&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Tasa+de+Pol%EDtica+Monetaria+%28en++e.a.%29"
if tipo=="3":
#Tasa fija de precancelación para depósitos con opción de cancelación anticipada en UVA (en n.a.)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=7934&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Tasa+fija+de+precancelaci%F3n+para+dep%F3sitos+con+opci%F3n+de+cancelaci%F3n+anticipada+en+UVA+%28en++n.a.%29"
if tipo=="4":
#Tasa mínima para plazos fijos de personas humanas hasta $1 millón (en n.a.)
    url = "&B1=Enviar&primeravez=1&serie=7938&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Tasa+m%EDnima+para+plazos+fijos+de+personas+humanas+hasta+%241+mill%F3n+%28en++n.a.%29"
if tipo=="5":
#Tasa mínima para plazos fijos de personas humanas hasta $1 millón (en e.a. para depósitos a 30 días)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=7939&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Tasa+m%EDnima+para+plazos+fijos+de+personas+humanas+hasta+%241+mill%F3n+%28en++e.a.+para+dep%F3sitos+a+30+d%EDas%29"
if tipo=="6":
#BADLAR en pesos de bancos privados (en n.a.)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=1222&serie1=0&serie2=0&serie3=0&serie4=0&detalle=BADLAR+en+pesos+de+bancos+privados+%28en++n.a.%29"
if tipo=="7":
#BADLAR en pesos de bancos privados (en e.a.)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=7937&serie1=0&serie2=0&serie3=0&serie4=0&detalle=BADLAR+en+pesos+de+bancos+privados+%28en++e.a.%29"
if tipo=="8":
#TM20 en pesos de bancos privados (en n.a.)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=7922&serie1=0&serie2=0&serie3=0&serie4=0&detalle=TM20+en+pesos+de+bancos+privados%A0%28en++n.a.%29"
if tipo=="9":
#Base monetaria - Total (en millones de pesos)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=250&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Base+monetaria%A0-+Total+%28en+millones+de+pesos%29"
if tipo=="10":
#Circulación monetaria (en millones de pesos)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=251&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Circulaci%F3n+monetaria%A0%28en+millones+de+pesos%29"
if tipo=="11":
#M2 privado, promedio móvil de 30 días, variación interanual (en )
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=7919&serie1=0&serie2=0&serie3=0&serie4=0&detalle=M2+privado%2C+promedio+m%F3vil+de+30+d%EDas%2C+variaci%F3n+interanual%A0%28en+%29"
if tipo=="12":
#Inflación mensual (variación en )
    url = "&B1=Enviar&primeravez=1&serie=7931&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Inflaci%F3n+mensual%A0%28variaci%F3n+en+%29"
if tipo=="13":
#CER (Base 2.2.2002=1)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=3540&serie1=0&serie2=0&serie3=0&serie4=0&detalle=CER%A0%28Base+2.2.2002%3D1%29"
if tipo=="14":
#Unidad de Valor Adquisitivo (UVA) (en pesos -con dos decimales-, base 31.3.2016=14.05)
    url = "&B1=Enviar&primeravez=1&fecha_desde=&fecha_hasta=&serie=7913&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Unidad+de+Valor+Adquisitivo+%28UVA%29%A0%28en+pesos+-con+dos+decimales-%2C+base+31.3.2016%3D14.05%29"
if tipo=="15":
#Unidad de Vivienda (UVI) (en pesos -con dos decimales-, base 31.3.2016=14.05)
    url = "&B1=Enviar&primeravez=1&serie=7914&serie1=0&serie2=0&serie3=0&serie4=0&detalle=Unidad+de+Vivienda+%28UVI%29%A0%28en+pesos+-con+dos+decimales-%2C+base+31.3.2016%3D14.05%29"

res =requests.get(url_base+url)
soup = BeautifulSoup(res.content, 'html.parser') 

table = soup.find_all('table')
data = pd.read_html(str(table))[0]

list=["9","10"]
if (tipo in list):
    data['Valor'] = data['Valor'].str.replace(".", "").astype(int)
if tipo=="0":
    data["Valor"]=data["Valor"]*1000000
    data['Valor'] = data['Valor'].astype(int)

list=["1","2","3","4","5","14","15"]
if (tipo in list):
    data["Valor"]=data["Valor"]/100
list=["6","7","8","13"]
if (tipo in list):
    data["Valor"]=data["Valor"]/10000
list=["11","12"]
if (tipo in list):
    data["Valor"]=data["Valor"]/10

for i in range(len(data)):
    var = data.iloc[i]['Fecha']
    var= var.split("/")
    day=int(var[0])
    month=int(var[1])
    year=int(var[2])
    data.loc[i]['Fecha'] =datetime.date(year, month, day)

data = data.set_index("Fecha")
print(data)
