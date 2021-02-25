# Primer Script

Este primer Script sirve para ver la versión del SO del ordenador

Primero debemos de abrir un programa tipi Vim, Sublime Text, Editor de textos etc.


```python
! echo "Examinando versión de Ubuntu y fecha de instalación"
```

    Examinando versión de Ubuntu y fecha de instalación



```python
! lsb_release -a
```

    No LSB modules are available.
    Distributor ID:	Ubuntu
    Description:	Ubuntu 20.04.2 LTS
    Release:	20.04
    Codename:	focal



```python
! ls -alct / |tail -1|awk '{print $6, $7, $8}'
```

    Jun 9 2020



```python
! neofetch
```

    [?25l[?7l[0m[31m[1m            .-/+oossssoo+/-.
            `:+ssssssssssssssssss+:`
          -+ssssssssssssssssssyyssss+-
        .ossssssssssssssssss[37m[0m[1mdMMMNy[0m[31m[1msssso.
       /sssssssssss[37m[0m[1mhdmmNNmmyNMMMMh[0m[31m[1mssssss/
      +sssssssss[37m[0m[1mhm[0m[31m[1myd[37m[0m[1mMMMMMMMNddddy[0m[31m[1mssssssss+
     /ssssssss[37m[0m[1mhNMMM[0m[31m[1myh[37m[0m[1mhyyyyhmNMMMNh[0m[31m[1mssssssss/
    .ssssssss[37m[0m[1mdMMMNh[0m[31m[1mssssssssss[37m[0m[1mhNMMMd[0m[31m[1mssssssss.
    +ssss[37m[0m[1mhhhyNMMNy[0m[31m[1mssssssssssss[37m[0m[1myNMMMy[0m[31m[1msssssss+
    oss[37m[0m[1myNMMMNyMMh[0m[31m[1mssssssssssssss[37m[0m[1mhmmmh[0m[31m[1mssssssso
    oss[37m[0m[1myNMMMNyMMh[0m[31m[1msssssssssssssshmmmh[0m[31m[1mssssssso
    +ssss[37m[0m[1mhhhyNMMNy[0m[31m[1mssssssssssss[37m[0m[1myNMMMy[0m[31m[1msssssss+
    .ssssssss[37m[0m[1mdMMMNh[0m[31m[1mssssssssss[37m[0m[1mhNMMMd[0m[31m[1mssssssss.
     /ssssssss[37m[0m[1mhNMMM[0m[31m[1myh[37m[0m[1mhyyyyhdNMMMNh[0m[31m[1mssssssss/
      +sssssssss[37m[0m[1mdm[0m[31m[1myd[37m[0m[1mMMMMMMMMddddy[0m[31m[1mssssssss+
       /sssssssssss[37m[0m[1mhdmNNNNmyNMMMMh[0m[31m[1mssssss/
        .ossssssssssssssssss[37m[0m[1mdMMMNy[0m[31m[1msssso.
          -+sssssssssssssssss[37m[0m[1myyy[0m[31m[1mssss+-
            `:+ssssssssssssssssss+:`
                .-/+oossssoo+/-.[0m
    [20A[9999999D[43C[0m[1m[31m[1moscar[0m@[31m[1moscar[0m 
    [43C[0m-----------[0m 
    [43C[0m[31m[1mOS[0m[0m:[0m Ubuntu 20.04.2 LTS x86_64[0m 
    [43C[0m[31m[1mHost[0m[0m:[0m Aspire E5-573G V3.72[0m 
    [43C[0m[31m[1mKernel[0m[0m:[0m 5.8.0-43-generic[0m 
    [43C[0m[31m[1mUptime[0m[0m:[0m 13 hours, 13 mins[0m 
    [43C[0m[31m[1mPackages[0m[0m:[0m 2520 (dpkg), 23 (snap)[0m 
    [43C[0m[31m[1mShell[0m[0m:[0m bash 5.0.17[0m 
    [43C[0m[31m[1mResolution[0m[0m:[0m 1366x768, 1920x1080[0m 
    [43C[0m[31m[1mDE[0m[0m:[0m GNOME[0m 
    [43C[0m[31m[1mWM[0m[0m:[0m Mutter[0m 
    [43C[0m[31m[1mWM Theme[0m[0m:[0m Adwaita[0m 
    [43C[0m[31m[1mTheme[0m[0m:[0m Yaru-dark [GTK2/3][0m 
    [43C[0m[31m[1mIcons[0m[0m:[0m Yaru [GTK2/3][0m 
    [43C[0m[31m[1mTerminal[0m[0m:[0m jupyter-lab[0m 
    [43C[0m[31m[1mCPU[0m[0m:[0m Intel i7-5500U (4) @ 3.000GHz[0m 
    [43C[0m[31m[1mGPU[0m[0m:[0m Intel HD Graphics 5500[0m 
    [43C[0m[31m[1mGPU[0m[0m:[0m NVIDIA GeForce 920M[0m 
    [43C[0m[31m[1mMemory[0m[0m:[0m 8054MiB / 15927MiB[0m 
    
    [43C[30m[40m   [31m[41m   [32m[42m   [33m[43m   [34m[44m   [35m[45m   [36m[46m   [37m[47m   [m
    [43C[38;5;8m[48;5;8m   [38;5;9m[48;5;9m   [38;5;10m[48;5;10m   [38;5;11m[48;5;11m   [38;5;12m[48;5;12m   [38;5;13m[48;5;13m   [38;5;14m[48;5;14m   [38;5;15m[48;5;15m   [m
    
    
    [?25h[?7h


```python
! echo "Examinando usuarios:"
```

    Examinando usuarios:



```python
! whoami
```

    oscar



```python
! id
```

    uid=1000(oscar) gid=1000(oscar) groups=1000(oscar),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),997(docker)



```python
! echo "Examinando conexión a Internet"
```

    Examinando conexión a Internet



```python
! ping -c 1 https://theegg.ai/
```

    ping: https://theegg.ai/: Name or service not known



```python
! a=$(wc -l /etc/passwd | cut -f 1 -d " ")
```


```python
! echo "Total de líneas en el fichero de passwords: " $a
```

    Total de líneas en el fichero de passwords: 



```python
! echo "Examinando sistema de ficheros"
```

    Examinando sistema de ficheros



```python
! df -h | grep -v loop | grep -v tmpfs
```

    Filesystem      Size  Used Avail Use% Mounted on
    udev            7.8G     0  7.8G   0% /dev
    /dev/sda2       439G  319G   98G  77% /
    /dev/sda1       511M  7.9M  504M   2% /boot/efi


### Excaminamos la instalación del software


```python
! echo "Examinando la instalación de software: "
```

    Examinando la instalación de software: 



```python
! awk -W version 2> /dev/null | head -1
```

    GNU Awk 5.0.1, API: 2.0 (GNU MPFR 4.0.2, GNU MP 6.2.0)



```python
! sed --version | head -1
```

    sed (GNU sed) 4.7



```python
! grep --version | head -1
```

    grep (GNU grep) 3.4



```python
### Vemos las versiones de diferentes programas
```


```python
! java -version
```

    openjdk version "1.8.0_282"
    OpenJDK Runtime Environment (build 1.8.0_282-8u282-b08-0ubuntu1~20.04-b08)
    OpenJDK 64-Bit Server VM (build 25.282-b08, mixed mode)



```python
! python --version
```

    Python 3.7.6


Todo Junto:

    #!/bin/bash
    echo "Examinando versión de Ubuntu y fecha de instalación"
    neofetch
    lsb_release -a
    ls -alct / |tail -1|awk '{print $6, $7, $8}'
    echo "Examinando usuarios:"
    whoami
    id
    a=$(wc -l /etc/passwd | cut -f 1 -d " ")
    echo "Examinando conexión a Internet"
    ping -c 1 https://theegg.ai/
    echo "Total de líneas en el fichero de passwords: " $a
    echo "Examinando sistema de ficheros"
    df -h | grep -v loop | grep -v tmpfs
    echo "Examinando la instalación de software: "
    awk -W version 2> /dev/null | head -1
    sed --version | head -1
    grep --version | head -1
    java -version
    python --version

Una vez generado el fichero, lo guardamos con la terminación .sh  en este caso, "informe.sh"

Para todo script, es necesario darle permisos de ejecución
Otorgar permisos de ejecución y ejecutarlos indicando la ruta:

    "usuario@nombreMaquina:~$ chmod +x extrae.sh"    
    "usuario@nombreMaquina:~$ ./extrae.sh"    

![](ejecutable.png)
