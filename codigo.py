importar  sys , pygame
importar  imagen
desde  sys  import  argv
de  importación matemática  *
importar  numpy
 tiempo de importación
importar  matemáticas

def  main ():
    ima , ancho , alto , vecino_n =  pixel ( argv [ 1 ])
    i_filtro  =  filtros ( ima , ancho , alto , vecino_n )
    pantalla  =  pygame . pantalla . set_mode (( ancho , alto ))
    pygame . pantalla . set_caption ( 'Imagenes' )
    img  =  pygame . imagen . cargar ( i_filtro )
    pantalla  =  pygame . pantalla . get_surface ()
    mientras que es  cierto :
        para  eventos  en  pygame . evento . obtener ():
            si  eventos . tipo  ==  pygame . SALIR :
                sys . salir ( 0 )
        pantalla . blit ( img , ( 0 , 0 ))
        pygame . pantalla . actualizar ()
    

def  filtros ( ima , ancho , alto , vecino_n ):
    tiempo1  =  tiempo . tiempo ()
    imagen  =  ima . cargar ()
    val_1  = [ - 1 , 0 , 1 ]
    para  i  en  rango ( ancho ):
        para  j  en  rango ( alto ):
            pm  =  vecinos ( i , j , val_1 , vecino_n )
            imagen [ i , j ] = ( pm , pm , pm )
    nueva  =  'filtro.png'
    i_filtro  =  ima . guardar ( nueva )
    tiempo2  =  tiempo . tiempo ()
    imprimir  "Tiempo de procesamiento filtro"
    volver  nueva

#def conv (i_filtro,)

def  vecinos ( i , j , vec_1 , vecino_n ):
    pm  =  0
    índice  =  0
    para  x  en  vec_1 :
        para  y  en  vec_1 :
            sumav_1  =  i + x  # sumamos los vecinos
            sumav_2  =  j + y  # sumamos los vecinos
            prueba :
                if  vecino_n [ sumav_1 , sumav_2 ]: #ciclo
                    pm  + =  vecino_n [ sumav_1 , sumav_2 ]
                    índice + = 1
            excepto  IndexError :
                pasar
    prueba :
        pm = int ( pm / indice )
        regreso  pm
    excepto  ZeroDivisionError :
        volver  0

#Escala de grises
def  píxel ( ima ):
    ima  =  Imagen . abierto ( ima )
    nueva  =  'escala_grises.png'
    imagen  =  ima . cargar ()
    ancho , alto  =  ima . Talla
    vecino_n  =  numpy . vacío (( ancho , alto ))
    para  i  en  rango ( ancho ):
        para  j  en  rango ( alto ):
            ( r , g , b ) =  ima . getpixel (( i , j ))
            pix  = ( r + g + b ) / 3
            imagen [ i , j ] = ( pix , pix , pix )
            vecino_n [ i , j ] =  int ( pix )
    i_filtro  =  ima . copiar ()
    
    imagen  =  ima . guardar ( nueva )
    volver  i_filtro , ancho , alto , vecino_n

if  __name__  ==  "__main__" :
    principal ()