<template>
    <div class="container">
      <h1>Detector de Incendios</h1>
  
      <div class="content">
        
        <img :src="imagePreview" alt="Vista previa de la imagen" class="preview-image"/>
  
        <input type="file" @change="previewImage" />
        <button @click="sendImageToModel">Consultar al Modelo</button>
  
        <p>Respuesta del Modelo: {{ prediction }}</p>
      </div>
    </div>
  </template>
  
  <style scoped>
  
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }
  
  .preview-image {
    max-width: 500px;
    max-height: 500px;
  }
  </style>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        imagePreview: null,
        prediction: null,
      };
    },
    methods: {
      previewImage(event) {
        const file = event.target.files[0];
        this.imagePreview = URL.createObjectURL(file);
      },
      sendImageToModel() {
        const fileInput = document.querySelector('input[type="file"]');
        if (fileInput.files.length === 0) {
          alert("Por favor, selecciona una imagen.");
          return;
        }
        const file = fileInput.files[0];
  
        const formData = new FormData();
        formData.append('file', file);
  
        axios.post('http://127.0.0.1:8000/predict', formData)
          .then(response => {
            this.prediction = response.data.is_fire ? "Incendio" : "No Incendio";
          })
          .catch(error => {
            console.error('Error al cargar la imagen:', error);
            alert("Error al cargar la imagen. Por favor, intenta de nuevo.");
          });
      },
    },
  };
  </script>