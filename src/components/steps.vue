<template>
  <v-stepper
    v-model="current_step"
    vertical
    non-linear
  >
    <v-stepper-step
      :complete="current_step > 1"
      editable
      step="1"
    >
      Upload Video
      
    </v-stepper-step>

    <v-stepper-content step="1">
      
      
      <slot></slot>


    </v-stepper-content>

    <v-stepper-step
      :complete="current_step > 2"
      step="2"
    >
      Process Video 
    </v-stepper-step>

    <v-stepper-content step="2">
      <v-card
        color="grey lighten-1"
        class="mb-12"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="current_step = 3"
      >
        Process
      </v-btn>
      <v-btn text>
        Cancel
      </v-btn>
    </v-stepper-content>

    <v-stepper-step
      :complete="current_step > 3"
      step="3"
    >
      Download Video
    </v-stepper-step>

    <v-stepper-content step="3">
      <v-card
        color="grey lighten-1"
        class="mb-12"
        height="200px"
      ></v-card>
      
      <v-btn
        color="primary"
        @click="current_step = 4"
      >
        Download MP4
      </v-btn>

      <v-btn
        color="primary"
        @click="current_step = 4"
      >
        Download Images
      </v-btn>

      ...
      <v-btn
        color="secondary"
        @click="current_step = 4"
      >
        Upload Another Video
      </v-btn>

      <v-btn text>
        Cancel
      </v-btn>
    </v-stepper-content>

    
  </v-stepper>
</template>

<script>
  
  //import Uploader from './uploader.vue';

  export default {
    data () {
      return {
        current_step: 1,
        width: 300,
      }
    },

    components: {
      //Uploader,
    }
  }
</script>




