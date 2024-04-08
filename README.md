
---

# pyAudioFlow

***

<b>PyAudioFlow</b> es una clase que hereda de la librería PyAudio. He aplicado herencia a la clase de PyAudio, para que por medio de este proyecto se pueda agregar o simplificar procesos de la misma, y al mismo tiempo tener acceso a todas herramientas presentes y futuras de PyAudio.

---

## Documentación técnica de PyAudioFlow

***

### Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |

***

### Librerías del proyecto.
| librería  | Descripción              | Comando                           |
| :----     | :---                     | :---                              |
| pyAudio   | Permite trabajar con audio | python -m pip install pyAudio  |

---

### Realice sus pruebas, actualizaciones o modificaciones.
> Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.

> Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```

---

#### Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Realice pruebas de rutina.                    |  |
| Paso 8 | Finalice su gestión.                          | deactivate                            |

***

### Reconocimiento al trabajo de dibulgación que hizo posible este código.

| Developer | Código original | Presente en el proyecto: | Implementado en: |
|:--|:--|:--|:--|
|Oscar Fernandez| [oscarFernandez.md](https://github.com/oigonzalezp2024/pyAudioFlow/blob/main/aportes.md) | [pyAudioFlow.py](https://github.com/oigonzalezp2024/pyAudioFlow/blob/main/pyAudioFlow.py) | [demo1.py](https://github.com/oigonzalezp2024/pyAudioFlow/blob/main/demo1.py) |
