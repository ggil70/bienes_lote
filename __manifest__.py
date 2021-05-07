# -*- coding: utf-8 -*-

{
        'name': "Registro Inicial en Lotes Bienes Publicos",
        'version' : "13.1",
        'author' : "Beatriz Coronel",
        'website' : "",
        'category' : "Bienes Publicos",
        
        'description': """
                 Registro Inicial en  Lotes de Bienes Publicos
         """,
        'depends' : ['base','bienes', 'web_readonly_bypass'],
        
        'data' : ['security/groups.xml',

        'security/ir.model.access.csv',
        
        'views/bieneslote_view.xml',
       



        ], 


       
        
        'installable': True,
        'auto_install': False
        
} 
