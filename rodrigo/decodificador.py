def  codificar ( f ):
    letras = { ' a ' : ' f ' , ' b ' : ' g ' , ' c ' : ' h ' , ' d ' : ' i ' , ' e ' : ' j ' , ' f ' : ' k ' , ' g ' : 'l ' , 'h ' : ' m ' , ' i ' : ' n ' , ' j ' : ' o ' , ' k ' : ' p ' , ' l ' : ' q ' , ' m ' : ' r ' , ' n ' : ' s ' , ' o ': ' t' , ' p ' : ' u ' , ' q ' : ' v ' ,
              ' r ' : ' w ' , ' s ' : ' x ' , ' t ' : ' y ' , ' u ' : ' z ' , ' v ' : ' a ' , ' w ' : ' b ' , ' x ' : ' c ' , 'y ' : 'd ' , ' z ' : ' e ' , ' ñ ' : ' ñ ' , ' , ' : ' ; ' , ' ! ' : ' < ' , ' " ' : ' > ' , ' # ' : ' - ' , ' $ ' : '' : ' | ' , ' Y ' : ' ¬ ' ,
              ' / ' : ' _ ' , ' ( ' : ' { ' , ' ) ' : ' } ' , ' = ' : ' [ ' , ' ? ' : ' ' ' , ' ¿ ' : ' ' ' , ' ¡ ' : ' ° ' , ' .+ ' , ' 0 ' : ' 9 ' , ' 1 ' : ' 8 ' , ' 2 ' : ' 7 ' , ' 3 ' : ' 6 ' , ' 4 ' : ' 5 ' , ' 5 ' : ' 4 ' , ' 6 ' : ' 3 ', ' 7' : ' 2 ' , ' 8 ' : ' 1 ' , ' 9 ' : ' 0 ' ,
              ' A ' : ' F ' , ' B ' : ' G ' , ' C ' : ' H ' , ' D ' : ' I ' , ' E ' : ' J ' , ' F ' : ' K ' , ' G ' : ' L ' , 'H ' : 'M ' , ' I ' : ' N ' , ' J ' : ' O ' , ' K ' : ' P ' , ' L ' : ' Q ' , ' M ' : ' R ' , ' N ' : ' S ' , ' O ' : ' T ', ' P' : ' U ' , ' Q ' : ' V ' , ' R ' : ' W ' ,
              ' S ' : ' X ' , ' T ' : ' Y ' , ' U ' : ' Z ' , ' V ' : ' A ' , ' W ' : ' B ' , ' X ' : ' C ' , ' Y ' : ' D ' , 'Z ' : 'E ' , ' Ñ ' : ' Ñ ' , ' á ' : ' Á ' , ' é ' : ' É ' , ' í ' : ' Í ' , ' ó ' : ' Ó ' , ' ú ' : ' Ú ' , ' ü ' : ' Ü '}
    frasec =  ' '
    para l en f:
        si l ==  '  ' :
            frasec + =  '  '
        else :
            para letra en letras:
                si l == letra:
                    frasec + = letras [letra]
    print ( " LA FRASE CODIFICADA ES: " , frasec, " \ n " )
        
def  decodificar ( f ):
    letras = { ' f ' : ' a ' , ' g ' : ' b ' , ' h ' : ' c ' , ' i ' : ' d ' , ' j ' : ' e ' , ' k ' : ' f ' , ' l ' : 'g ' , 'm ' : ' h ' , ' n ' : ' i ' , ' o ' : ' j ' , ' p ' : ' k ' , ' q ' : ' l ' , ' r ' : ' m ' , ' s ' : ' n ' , ' t ': ' o' , ' u ' : ' p ' , ' v ' : ' q ' ,
              ' w ' : ' r ' , ' x ' : ' s ' , ' y ' : ' t ' , ' z ' : ' u ' , ' a ' : ' v ' , ' b ' : ' w ' , ' c ' : ' x ' , 'd ' : 'y ' , ' e ' : ' z ' , ' ñ ' : ' ñ ' , ' ; ' : ' , ' , ' < ' : ' ! ' , ' > ' : ' " ' , ' - ' : ' # ' , ' * ' : '' : ' % ' , ' ¬ ' : ' & ' ,
              ' _ ' : ' / ' , ' { ' : ' ( ' , ' } ' : ' ) ' , ' [ ' : ' = ' , ' ' ' : ' ? ' , ' ` ' : ' ¿ ' , ' ° ' : ' ¡ ' , '. ' , ' 9 ' : ' 0 ' , ' 8 ' : ' 1 ' , ' 7 ' : ' 2 ' , ' 6 ' : ' 3 ' , ' 5 ' : ' 4 ' , ' 4 ' : ' 5 ' , ' 3 ' : ' 6 '' : ' 7 ' , ' 1 ' : ' 8 ' , ' 0 ' : ' 9 ' ,
              ' F ' : ' A ' , ' G ' : ' B ' , ' H ' : ' C ' , ' I ' : ' D ' , ' J ' : ' E ' , ' K ' : ' F ' , ' L ' : ' G ' , 'M ' : 'H ' , ' N ' : ' I ' , ' O ' : ' J ' , ' P ' : ' K ' , ' Q ' : ' L ' , ' R ' : ' M ' , ' S ' : ' N ' , ' T ' : ' O ', ' U' : ' P ' , ' V ' : ' Q ' , ' W ' : ' R ' ,
              ' X ' : ' S ' , ' Y ' : ' T ' , ' Z ' : ' U ' , ' A ' : ' V ' , ' B ' : ' W ' , ' C ' : ' X ' , ' D ' : ' S ' , 'E ' : 'Z ' , ' Ñ ' : ' Ñ ' , ' Á ' : ' á ' , ' É ' : ' é ' , ' Í ' : ' í ' , ' Ó ' : ' ó ' , ' Ú ' : ' ú ' , ' Ü ' : ' ü '}
    frasec =  ' '
    para l en f:
        si l ==  '  ' :
            frasec + =  '  '
        else :
            para letra en letras:
                si l == letra:
                    frasec + = letras [letra]
    print ( " LA FRASE CODIFICADA ES: " , frasec, " \ n " )

# MENÚ
     
print ( " ********************************** " )
imprimir ( " * DECODIFICADOR * " )
print ( " ********************************** \ n " )

opc =  1
mientras que opc ! =  0 :
    imprimir ( " 1.- CODIFICAR " )
    print ( " 2.- DECODIFICAR " )
    print ( " 0.- SALIR " )
    opc =  input ( " INGRESA LA OPCION QUE QUIERES REALIZAR: " )
    si opc ==  ' 1 ' :
        fr =  entrada ( " \ n Ingresa una frase: " )
        codificar (fr)
    elif opc == ' 2 ' :
        fr =  entrada ( " \ n Ingresa una frase: " )
        decodificar (fr)
    elif opc ==  ' 0 ' :
        salir ()
    else :
        imprimir ( " \ n " )
        print ( " Ingresa una opción valida " )