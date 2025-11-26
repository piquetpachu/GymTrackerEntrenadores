Aquí lo tenés en **Markdown limpio**, listo para pegar en tu `README.md`:

---

````md
# 📘 GymTracker Entrenadores – Rama *clientes*

La rama **clientes** forma parte del sistema GymTracker, una aplicación en **Django** enfocada en la gestión de clientes, entrenadores y rutinas. Esta rama contiene la lógica, modelos, formularios y vistas relacionadas exclusivamente con los clientes.

---

## ✔️ Requerimientos

- Python 3.10 o superior  
- pip  
- Git  
- (Opcional) Entorno virtual con `venv`

---

## 🚀 Cómo iniciar el proyecto en otra PC

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/piquetpachu/GymTrackerEntrenadores.git
cd GymTrackerEntrenadores
git checkout clientes
````

---

### 2️⃣ Crear entorno virtual (opcional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Aplicar migraciones

```bash
python manage.py migrate
```

---

### 5️⃣ Crear superusuario

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Iniciar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```
http://127.0.0.1:8000/
```

---

