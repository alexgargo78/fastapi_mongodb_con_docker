## 🍽️ API REST – Reservas de Restaurante (FastAPI + MongoDB + Docker)

📌 Descripción

Esta práctica consiste en el desarrollo de una API REST para la gestión de reservas de restaurante, utilizando:

        FastAPI como framework backend.

        MongoDB como base de datos NoSQL.

        Docker Compose para orquestar ambos servicios.

La API permite realizar las operaciones CRUD básicas:

        📄 Listar todas las reservas.

        ➕ Crear una nueva reserva.

        ❌ Eliminar una reserva por su identificador.

Además, se impide crear dos reservas en el mismo restaurante con la misma fecha y hora mediante un índice único en la base de datos.

## ⚙️ Tecnologías utilizadas

| Tecnología                  | Descripción                                           |
| --------------------------- | ----------------------------------------------------- |
| **Python 3.11**             | Lenguaje principal del proyecto                       |
| **FastAPI**                 | Framework para crear APIs REST                        |
| **Uvicorn**                 | Servidor ASGI para ejecutar FastAPI                   |
| **MongoDB 7.0**             | Base de datos NoSQL para almacenar las reservas       |
| **Motor**                   | Cliente asíncrono para conectar FastAPI con MongoDB   |
| **Docker / Docker Compose** | Contenedores para desplegar la API y la base de datos |

## 🧩 Estructura del proyecto

FASTAPI_MONGODB_CON_DOCKER/
├── api/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore



## 📚 Proyecto académico

💡 Proyecto realizado para la asignatura **"Desarrollo de aplicaciones web en el entorno servidor"**  
📜 Dentro del **Certificado de Desarrollo de Aplicaciones con Tecnología Web (IFCD2010)**  
🏫 Impartido por el **CPIFP Alan Turing**  
👨‍🏫 Profesor: **Luis José Sánchez González**

---


## Galería:

Principal

![Principal](./API_Reserva_Restaurante._Principal.png)



Listar Reservas 

![Listar](./API_Reserva_Restaurante_Listar_Reserva.png)


Crear Reserva

![Crear](./API_Reserva_Restaurante_Crear%20Reserva.png)


Borrar Reserva

![Borrar](./API_Reserva_Restaurante_Borrar%20Reservaimage.png)


