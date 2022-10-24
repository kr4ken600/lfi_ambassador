## LFI_AMBASSADOR
LFI AMBASSADIR, es un script programado en python diseñado especificamente para la maquina Ambassador de Hack The Box.
Realizando peticiones por GET al servidor, para poder realizar un Local File Inclusion (LFI)
***
## Instalacion
```
https://github.com/kr4ken600/lfi_ambassador.git lfi
cd lfi
pip install -r requirements.txt
```
***
## Uso
El script contiene una opcion de ayuda:
```
python3 lfi_ambassador.py -h
```
En el que se desplegara la forma de usarse y sus diferentes opciones.
![Image Text](/img/help.png)
### Modo Lectura de Archivos
Entre las opciones se encuentra ```-r```, de ```read``` el cual requere de un parametro:
```
python3 lfi_ambassador.py -r [DIR/ARCHIVO]
```
## Ejemplo
![Image Text](/img/image1.png)
![Image Text](/img/image2.png)

### Modo Descarga de Archivos
Entre las opciones se encuentra ```-d```, de ```download``` el cual requere de dos parametros:
```
python3 lfi_ambassador.py -d [DIR/ARCHIVO] [NOMBRE]
```
## Ejemplo
![Image Text](/img/image3.png)
![Image Text](/img/image4.png)