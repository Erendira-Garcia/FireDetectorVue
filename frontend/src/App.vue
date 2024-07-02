<template>

  <header>
          <img src="M1000IA.jpg" alt="La imagen no carga">
  </header>
  
      <nav class="row navbar">
          <ul class="col-sm-12 col-md-4 col-lg-4 col-xl-4">
              <i class="fa-brands fa-github"></i>
              <a href="https://github.com/Erendira-Garcia/FireDetectorAPI">GitHub</a>
          </ul>
          <div class="col-sm-12 col-md-4 col-lg-4 col-xl-4">
              <i class="fa-solid fa-infinity"></i>
              <a href="https://colab.research.google.com/drive/1zb0dXNzGgjPDQXG1srNxEc1UAtlI-Vbx">Google Colab</a>
          </div>
          <div class="col-sm-12 col-md-4 col-lg-4 col-xl-4">
              <i class="fa-solid fa-file"></i>
              <a href="https://docs.google.com/document/d/1--Z8tuRJ7FXhPctlnX8iTTOofqy37lJU/edit">Documentación</a>
          </div>
      </nav>
    <div id="app">
      <ImageUploader />
    </div>
    
      <footer class="row footer">
          <h4><strong>Grupo 2 M1000IA - 2024</strong></h4>
      </footer>
  
  </template>
  
      <footer class="row footer">
          <h4><strong>Grupo 2 M1000IA - 2024</strong></h4>
      </footer>
  
  
  <script>
  import ImageUploader from './components/ImageUploader.vue';
  
  export default {
    name: 'App',
    components: {
      ImageUploader,
    },
  };
  </script>