<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <!-- <v-spacer></v-spacer> -->

      <v-tabs
        centered
        class="ml-n9"
        color="grey lighten-3"
      >
        <v-tab
          v-for="link in links"
          :key="link"
        >
          {{ link }}
        </v-tab>

      </v-tabs>


      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Learn More</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main class="grey lighten-3">

      <!-- <HelloWorld/> -->
      <v-container >
        
        <v-row>
          <v-col
            cols="12"
            sm="2"
          >
          <Sidebar/>

<!--             <v-sheet
              rounded="lg"
              min-height="268"
            >
              sidebar content 
            </v-sheet>
 -->
          </v-col>

          <v-col
            cols="12"
            sm="8"
          >
            <v-sheet
              min-height="70vh"
              color="white"
              elevation="4"
              rounded
              >


              <video
                :src="video"
                controls
              />
              <br/>
            
              <v-btn
                  
                  color="primary"
                  @click="loadVideo"
                >
                  Process
                </v-btn>

              <p>{{ message }}</p>

            
            <!-- <HelloWorld/> -->
            <Steps ref="steps">

                <div
                  v-for="file in video_files"
                  :key="file.name"
                >
                  {{ file.name }} size: {{ Math.round(file.size / 10000) / 100 }}  MB
                </div>


                <Uploader ref="uploader" v-on:changed="onFilesChanged" />
                  
                  <!-- v-show="video_files.length > 0"     -->
                <v-btn
                  
                  :disabled="video_files.length == 0"
                  color="primary"
                  @click="nextStep"
                >
                  Next Step
                </v-btn>


            </Steps>

            

            
            <div class="text-center">
              <div>
                <v-btn
                  class="ma-2"
                  color="primary"
                  dark
                  @click="overlay = !overlay"
                >
                  Accept
                  <v-icon
                    dark
                    right
                  >
                    mdi-checkbox-marked-circle
                  </v-icon>
                </v-btn>

                <v-btn
                  class="ma-2"
                  color="red"
                  dark
                >
                  Decline
                  <v-icon
                    dark
                    right
                  >
                    mdi-cancel
                  </v-icon>
                </v-btn>

                <v-btn
                  class="ma-2"
                  dark
                >
                  <v-icon
                    dark
                    left
                  >
                    mdi-minus-circle
                  </v-icon>Cancel
                </v-btn>
              </div>
            </div>

            Data: {{ toggle_exclusive }}
                  <v-card
                    flat
                    class="py-12"
                  >
                    <v-card-text>
                      <v-row
                        align="center"
                        justify="center"
                      >
                        <v-col cols="12">
                          <p class="text-center">
                            Mandatory
                          </p>
                        </v-col>
                        <v-btn-toggle
                          v-model="toggle_exclusive"
                          mandatory
                        >
                          <v-btn>
                            <v-icon>mdi-format-align-left</v-icon>
                          </v-btn>
                          <v-btn>
                            <v-icon>mdi-format-align-center</v-icon>
                          </v-btn>
                          <v-btn>
                            <v-icon>mdi-format-align-right</v-icon>
                          </v-btn>
                          <v-btn>
                            <v-icon>mdi-format-align-justify</v-icon>
                          </v-btn>
                        </v-btn-toggle>
                      </v-row>
                    </v-card-text>
                  </v-card>


            <v-progress-circular
              :rotate="90"
              :size="100"
              :width="15"
              :value="progress_value"
              color="teal"

            >
              {{ progress_value }} %
            </v-progress-circular>
                    
            <br/>
            asdf  
            <br/>
            <v-divider></v-divider>
            


                    <div class="text-center">
                      <v-btn
                        dark
                        color="orange darken-2"
                        @click="snackbar = true"
                      >
                        Open Snackbar
                      </v-btn>

                      <v-snackbar
                        v-model="snackbar"
                        :timeout="snack_timeout"
                      >
                        {{ snack_text }}

                        <template v-slot:action="{ attrs }">
                          <v-btn
                            color="blue"
                            text
                            v-bind="attrs"
                            @click="snackbar = false"
                          >
                            Close
                          </v-btn>
                        </template>
                      </v-snackbar>
                    </div>



            <br/>
            asfd
            <br/>
            asfd
            <br/>
            asfd
            <br/>
            asfd
              <!--  -->
            </v-sheet>
          </v-col>

<!--           <v-col
            cols="12"
            sm="2"
          >
            <v-sheet
              rounded="lg"
              min-height="268"
            >
              blah
            </v-sheet>
          </v-col>
 -->
        </v-row>

      </v-container>
      <Footer/>




      <v-overlay :value="overlay">
        <v-progress-circular
          indeterminate
          size="64"
        ></v-progress-circular>
      </v-overlay>

    </v-main>
  </v-app>
</template>



<script>

//import HelloWorld from './components/HelloWorld';
import Footer from './components/footer.vue';
//import Toggle from './components/toggle.vue';
import Sidebar from './components/sidebar.vue';
import Steps from './components/steps.vue';

import Uploader from './components/uploader.vue';

import { createFFmpeg, fetchFile } from '@ffmpeg/ffmpeg';


export default {
  name: 'App',

  components: {
    //HelloWorld,
    Footer,
    Sidebar,
    Steps,
    Uploader,
    //Toggle,
  },

  data: () => ({
    
    links: [
        'Video BG Remover',
        'Image BG Remover',
      ],

      video_files : [],

      toggle_exclusive: undefined,

      overlay: false,

      progress_value: 10,


      snackbar: false,
      snack_text: 'My timeout is set to 2000.',
      snack_timeout: 2000,


      video: null,

      message: "hello",

  }),

  

  watch: {
      overlay (val) {
        val && setTimeout(() => {
          this.overlay = false
        }, 3000)
      },
    },

  methods : {

    async loadVideo() {

      console.log("Loading...");

      const ffmpeg = createFFmpeg({ log: true });
      await ffmpeg.load();

      console.log("done...");
      this.message = "loading..";

      const { name } = this.video_files[0];
      //message.innerHTML = 'Loading ffmpeg-core.js';
      //await ffmpeg.load();
      
      //message.innerHTML = 'Reading video';

      ffmpeg.FS('writeFile', name, await fetchFile(this.video_files[0]));

      console.log("done2...");

      //await ffmpeg.run('-i', name, '-ss', '0', '-to', '1', 'output.mp4');
      //ffmpeg -i "%1" frames/out-%03d.jpg

      
      // async function transcode() {

      //   //this.message.value = 'Loading ffmeg-core.js';
      //   await ffmpeg.load();
      //   //this.message.value = 'Start transcoding';
      //   // ffmpeg.FS('writeFile', 'test.avi', await fetchFile(file));
      //   // await ffmpeg.run('-i', 'test.avi', 'test.mp4');
      //   // this.message.value = 'Complete transcoding';
      //   // const data = ffmpeg.FS('readFile', 'test.mp4');
      //   // this.video.value = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
      //   console.log("Done ...");
        
      // }
      
      //transcode();

      // this.message = "Loading...";
      // const ffmpeg = createFFmpeg({ log: true });

      // await ffmpeg.load();

      // this.message = "Done loading";

      // ffmpeg.FS('writeFile', 'test.avi', await fetchFile(file));
      // await ffmpeg.run('-i', 'test.avi', 'test.mp4');
      // message.value = 'Complete transcoding';
      // const data = ffmpeg.FS('readFile', 'test.mp4');
      // video.value = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));

    },



    nextStep() {
      console.log("next step!!");
      this.$refs.steps.current_step = 2
    },

    onFilesChanged(files) {
      this.video_files = files
    },


  }

};
</script>
