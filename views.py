from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.agencia.models import Agencia, Empresa

def Information(request):
    input1 = Agencia.objects.raw("SELECT u.USUA_LOGIN, u.USUA_NOMBRE, ua.EMPR_CODIGO, e.EMPR_NOMBRE, e.EMPR_IMAGEN, e.EMPR_IDENTIFICACION, ucd.AGEN_CODIGO, ucd.ZONA_CODIGO, ucd.CETC_CODIGO, z.ZONA_DESCRIPCION, a.AGEN_DESCRIPCION, cdc.CETC_DESCRIPCION, ms.TIPE_CODIGO, tp.TIPE_DESCRIPCION from  usuario u inner join usuario_empresa ua on u.USUA_CODIGO=ua.USUA_CODIGO  inner join EMPRESA e on ua.EMPR_CODIGO=e.EMPR_CODIGO inner join USUARIO_CENTRO_DE_COSTO ucd on u.USUA_CODIGO=ucd.USUA_CODIGO inner join zona z on ucd.ZONA_CODIGO=z.ZONA_CODIGO inner join agencia a on ucd.AGEN_CODIGO = a.AGEN_CODIGO inner join CENTRO_DE_COSTO cdc on ucd.CETC_CODIGO = cdc.CETC_CODIGO inner join usuario_modulo ms on u.USUA_CODIGO = ms.usua_codigo inner join tipo_perfil tp on ms.TIPE_CODIGO = tp.TIPE_CODIGO where u.USUA_login='ADMINISTRADOR' and ms.MOSI_CODIGO= 1")
    print(input1)
    return render(Information,"menu.html",input1)

def menuOpc(request):
    input2=Agencia.objects.raw("SELECT u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO= tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO = om.MOSI_CODIGO inner join perfil_ventana pf on um.MOSI_CODIGO= pf.MOSI_CODIGO inner join ventana ve on ve.VENT_DESCRIPCION like '%WEB%' where u.USUA_CODIGO = 'ADMINISTRADOR' and um.MOSI_CODIGO in (4,8,10) and om.OPME_DESCRIPCION like '%WEB%' AND PF.VENT_CODIGO like '80%'")
    print(input2)
    return render(menuOpc,"menu.html",input2)

def menu(request):
    entrada = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")    
    context = {'agencias': entrada}
    return render(request, 'menu.html', context)

def menue(request):
    entrada = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")
    for s in Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]"):
        print(s)
        print("LLLLLLLLLLLLLL")
    
    context = {'agencias': entrada}
    return render(request, 'menu.html', context)



def menus(request):
    #AGENCIA = Agencia.objects.raw("SELECT * FROM AGENCIA")
    #AGENCIA = Agencia.objects.raw("SELECT AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")[0]
    #AGENCIA = Agencia.objects.raw("SELECT 1 as id AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")
    #entrada = Agencia.objects.raw("SELECT AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")
    entrada = Agencia.objects.raw("SELECT PK_AGENCIA, AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")
    for s in Agencia.objects.raw("SELECT PK_AGENCIA, AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM AGENCIA"):
        print(s)
    
    context = {'agencias': entrada}
    print("HIZO LA CONSULTA ----------------------------")
    print(entrada)
    print(context)
    print(connection.queries)
    
    print("HIZO LA CONSULTA ---------------------------- FIN")
    return render(request, 'menu.html', context)

def Information(request):
    input1 = Agencia.objects.raw("SELECT u.USUA_LOGIN, u.USUA_NOMBRE, ua.EMPR_CODIGO, e.EMPR_NOMBRE, e.EMPR_IMAGEN, e.EMPR_IDENTIFICACION, ucd.AGEN_CODIGO, ucd.ZONA_CODIGO, ucd.CETC_CODIGO, z.ZONA_DESCRIPCION, a.AGEN_DESCRIPCION, cdc.CETC_DESCRIPCION, ms.TIPE_CODIGO, tp.TIPE_DESCRIPCION from  usuario u inner join usuario_empresa ua on u.USUA_CODIGO=ua.USUA_CODIGO  inner join EMPRESA e on ua.EMPR_CODIGO=e.EMPR_CODIGO inner join USUARIO_CENTRO_DE_COSTO ucd on u.USUA_CODIGO=ucd.USUA_CODIGO inner join zona z on ucd.ZONA_CODIGO=z.ZONA_CODIGO inner join agencia a on ucd.AGEN_CODIGO = a.AGEN_CODIGO inner join CENTRO_DE_COSTO cdc on ucd.CETC_CODIGO = cdc.CETC_CODIGO inner join usuario_modulo ms on u.USUA_CODIGO = ms.usua_codigo inner join tipo_perfil tp on ms.TIPE_CODIGO = tp.TIPE_CODIGO where u.USUA_login='ADMINISTRADOR' and ms.MOSI_CODIGO= 1")
    print(input1)
    return render(Information,"menu.html",input1)

def menuOpc(request):
    input2=Agencia.objects.raw("SELECT u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO= tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO = om.MOSI_CODIGO inner join perfil_ventana pf on um.MOSI_CODIGO= pf.MOSI_CODIGO inner join ventana ve on ve.VENT_DESCRIPCION like '%WEB%' where u.USUA_CODIGO = 'ADMINISTRADOR' and um.MOSI_CODIGO in (4,8,10) and om.OPME_DESCRIPCION like '%WEB%' AND PF.VENT_CODIGO like '80%'")
    print(input2)
    return render(menuOpc,"menu.html",input2)
