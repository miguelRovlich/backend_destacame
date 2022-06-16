# Bus tur app

## Project setup, para instalar dependencias del backend


### Activar el entorno virtual

```
venv\scripts\activate
```
### instalar paquetes requeridos
```
pip install -r requirements.txt
```
### crear migraciones
```
python manage.py makemigrations 
```
### correr migraciones

```
python manage.py migrate
```

### correr servidor de desarrollo

```
python manage.py runserver
```

### para poder correr las migraciones es necesario configurar el settings.py

`
DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre de la BD donde correr las migraciones',
        'USER': 'usuario registrado en tu sistema',
        'PASSWORD': 'password del sistema',
        'HOST': 'localhost',
        'PORT': '5432'
        }
    }
`

## Project setup front, para instalar dependencias
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```
### El backend debe estar corriendo para que el programa corra correctamente

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
