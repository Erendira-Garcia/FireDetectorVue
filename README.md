# Fire Detector

# Aplicación con Vue.JS del proyecto Detector de incendios del programa "Mil mujeres en IA" 2024


Para ejecutar la aplicación:

1  	- Tener descargado Node.js

2 	 - Colocar model.h5 en la carpeta "backend"

3	- Crear el entorno virtual de manera global:  

  	python -m venv env (env es el nombre del entorno en este caso)

4	- Activar el entorno virtual:  

  	Windows: env\Scripts\activate
  	macOS/Linux: source env/bin/activate

5	- Instalar las dependencias de manera global:  

  	pip install -r requirements.txt

6	- Cambia al directorio frontend y ejecuta:  

  	cd frontend
	npm install

7 	- Instalar `concurrently` para ejecutar el backend y el frontend simultáneamente:  

    	npm install --save-dev concurrently

8  	- Iniciar la aplicación  

	npm start

** NOTA** 

Si no responde el servidor de FastAPI con "concurrently", puedes iniciarlo directamente desde el directorio backend:

9  	-  Abre otra terminal, cambia al directorio "backend", activa el entorno virtual  y ejecuta:  

	cd backend
	env\Scripts\activate   o   source/ env/bin/activate
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

	Puedes probar en http://localhost:8000/docs que el servidor esté respondiendo 

10 	- Por último, vuelve a la terminal del frontend y ejecuta:  

	npm start





