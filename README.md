
Trabajo Integrador — Virtualización con VirtualBox
Arquitectura y Sistemas Operativos (AYSO)

---

Descripción

Este repositorio contiene los archivos correspondientes al Trabajo Integrador de la materia Arquitectura y Sistemas Operativos. El trabajo aborda el tema de virtualización mediante Oracle VirtualBox, incluyendo la instalación de un sistema operativo Linux (Ubuntu 24.04 LTS) dentro de una máquina virtual y el desarrollo de un programa en Python para calcular el promedio de notas de un alumno.

---
Integrantes

| Valzura Lourdes | valzuralourdes@gmail.com |
|---|---|
| Villanueva Felipe | felipe.villanuevaa254@gmail.com |

Materia: Arquitectura y Sistemas Operativos  
Docente: Carcaño Nicolás 
Fecha de entrega: 25/06/2026

---

Contenido del repositorio

```
 TPI-Virtualizacion-AYSO
 ├──  TPI_Virtualizacion_AYSO.pdf     
 ├──  promedio.py                     
 ├──  capturas/                       
 │    ├── 01_vm_escritorio.png           
 │    ├── 02_python_version.png          
 │    ├── 03_codigo_nano.png             
 │    └── 04_ejecucion_programa.png     
 └──  README.md                      
```

---

Cómo ejecutar el programa

Requisitos
- Python 3.x instalado (viene incluido en Ubuntu 24.04 LTS)

Pasos

1. Cloná o descargá este repositorio
2. Abrí una terminal y navegá hasta la carpeta del proyecto:
```bash
cd TPI-Virtualizacion-AYSO
```
Ejecutá el programa:
```bash
python3 promedio.py
```
4. Ingresá las 3 notas cuando el programa lo solicite (valores entre 0 y 10)

### Ejemplo de ejecución

```
=== Calculadora de Promedios ===
Ingrese 3 notas del alumno:

Nota 1: 7
Nota 2: 8
Nota 3: 5

--- Resultado ---
Notas ingresadas: [7.0, 8.0, 5.0]
Promedio: 6.67
Estado: APROBADO ✓
```

---

Tecnologías utilizadas

- Oracle VirtualBox 7.x* — Hipervisor tipo 2
- Ubuntu 24.04 LTS — Sistema operativo invitado (Linux)
- Python 3 — Lenguaje de programación
- Windows 10/11 — Sistema operativo anfitrión (host)

---

Bibliografía

- Documentación oficial de VirtualBox: https://www.virtualbox.org/manual/
- Ubuntu Desktop Guide: https://ubuntu.com/tutorials
- Documentación oficial de Python 3: https://docs.python.org/3/
