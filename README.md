# Sistema de Gestión de Eventos Culturales - Fundación CultuVivo

## Descripción del Proyecto
El **Sistema de Gestión de Eventos Culturales de la Fundación CultuVivo** busca optimizar la organización, registro y control de eventos culturales, garantizando una experiencia fluida tanto para asistentes como para artistas y administradores.

---

## Equipo de Trabajo (Grupo G-3)
* **Institución:** Campuslands (Salón de Tecnología - Ruta San Gil-Cajasan)
* **Estudiantes:**
  * Castro Manrique Juan Pablo
  * Chaparro Macías Diana Milena
  * Jaimes Bernal Miguel Ángel
  * Ortiz Ortiz Nikol Sarith
* **Año:** 2026

---

## Situación Problema
La Fundación CultuVivo requiere una solución tecnológica para gestionar eficazmente sus eventos culturales, automatizando el registro de asistentes, el control de aforos y las reservas bajo un esquema organizado y escalable.

---

## Requerimientos del Sistema

### Requerimientos Funcionales
* **RF01 - Registro de Asistente:** Permite a los asistentes inscribirse proporcionando identificación, nombre completo, correo electrónico y tipo de boleto (General, VIP o Preferencial).
* **RF02 - Control de Estados de Reserva:** Asigna y actualiza el estado de cada reserva entre: *Confirmado*, *En espera* y *Cancelado*.
* **RF03 - Consulta de Inscripciones:** Permite a los asistentes consultar sus boletos e inscripciones activas mediante su número de identificación.
* **RF04 - Registro de Eventos:** Permite al Administrador crear nuevos eventos ingresando nombre, fecha/hora, lugar y capacidad máxima.
* **RF05 - Modificación de Eventos:** Permite al Administrador actualizar la información general y el límite de aforo de un evento registrado.

### Requerimientos No Funcionales
* **RNF01 - Usabilidad:** Interfaz de consola (CLI) clara e intuitiva, estructurada con menús interactivos por rol.
* **RNF02 - Portabilidad:** Desarrollado en **Python 3**, ejecutable multiplataforma (Windows, Linux, macOS) sin librerías complejas externas.
* **RNF03 - Rendimiento:** Las operaciones de consulta y cálculo de aforo responden en menos de 1 segundo.
* **RNF04 - Mantenibilidad:** Código estructurado mediante **Programación Orientada a Objetos (POO)** con clases independientes.
* **RNF05 - Robustez y Validaciones:** Control de excepciones para prevenir fallos por entradas inválidas (fechas incorrectas, números negativos o IDs duplicados).

---

## Metodología Scrum
El proyecto se desarrolla utilizando el marco de trabajo ágil **Scrum**, adaptado a un Sprint de 1 semana para entregar un Producto Mínimo Viable (MVP) funcional en Python.

* **Roles:**
  * **Product Owner:** Juan Pablo Castro
  * **Scrum Master:** Miguel Ángel Jaimes
  * **Equipo de Desarrollo:** Nikol Ortiz y Diana Chaparro
* **Ceremonias:** Sprint Planning, Daily Stand-Up, Sprint Review y Sprint Retrospective.
* **Definición de Hecho (DoD):** El código corre sin errores en Python, cumple la funcionalidad solicitada, fue revisado en equipo y cuenta con el visto bueno del Product Owner.

---

## Documentación del Proyecto
Puedes consultar la documentación detallada y completa del proyecto en el siguiente enlace de Google Docs:
Ver Documentación Completa en Google Docs (https://docs.google.com/document/d/1vLT76U7hV-WeYndam1eT_B7kz3nQoAUrcZyi1TGqrO4/edit?usp=sharing)
