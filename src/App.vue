<template>
  <v-app>

    <!-- <v-toolbar dense dark color="teal" class="pa-0"> -->
        <v-toolbar class="pa-0 lighten-1" color="white" flat>

            

      <!-- <v-btn icon>
        <v-icon>mdi-magnify</v-icon>

      </v-btn>

            <v-toolbar-title>
                
            Free Background Eraser.com</v-toolbar-title>

            <v-spacer></v-spacer> -->

      <v-row>
        
        <v-col cols="2" class="my-auto">
          <v-progress-circular
          indeterminate
          size="20"
          class="mr-4"
          v-if="load_state == 0"
            ></v-progress-circular>

        <strong class="ml-1" style="color: gray;">{{ loading_message }}</strong>
        

        </v-col>

        <v-col class="d-flex justify-space-around">
          
          <!-- <v-toolbar-title class="white--text"></v-toolbar-title> -->

          <div style="position:relative;" class="text-center">

<!--        <v-img
              alt="Free Background Eraser.com logo"
              style="display: inline-block;"
              class="my-auto mt-6"
              src="android-chrome-192x192.png"
              width="35"
            />
-->
            
            <img src="android-chrome-192x192.png" width="32px;" style="position: absolute; left: -48px; top:0px;" />
            <h2 style='display: inline-block; color: gray;'>Free Background Eraser</h2>
            <span style="color: gray;">.com</span>
            


          </div>


        </v-col>
        
        <v-col cols="2" class="d-flex justify-end my-auto">
        
        </v-col>

    </v-row>
    </v-toolbar>

<!-- 
    <v-app-bar
      app
      color="purple lighten-1"
      dark
    >

 <v-progress-circular
      indeterminate
      size="20"
      v-if="load_state == 0"
    ></v-progress-circular>

    <div class="text-center ml-4">
        <strong>{{ loading_message }}</strong>
    </div>        

    <v-spacer></v-spacer>

    <v-img
          alt="Free Background Eraser.com logo"
          class="shrink mr-2"
          contain
          centered
          src="android-chrome-192x192.png"
          transition="scale-transition"
          width="35"
        />
        <h2>Free Background Eraser</h2>.com

      <v-spacer></v-spacer>




    </v-app-bar>  -->


    <v-main class="grey lighten-4">

      <!-- <HelloWorld/> -->
      <v-container >
        
        <v-row class="mt-2">
<!--           <v-col
            cols="12"
            sm="2"
          >
          <Sidebar/>

          </v-col> -->

<!-- 
          <v-col
            cols="12"
            sm="3"
          >
          

          </v-col>
 -->
          <v-col
            cols="12"
            sm="12"
          >

<!--             <v-sheet
              min-height="70vh"
              color="white"
              elevation="4"
              rounded
              >
 -->
              <!-- <h1> Load: {{ load_state }} </h1> -->

              


              
    
              <!-- <img id="output-image" style='border: 1px solid #ffcc00;'/> -->
              
              <canvas width="450" style="border:1px solid; display: none;" ></canvas>
              

              <!-- <input type="file" id="uploader"> -->

              
              <!-- <h3> {{ process_mode }} </h3> -->



              <v-alert
              
              v-if="invalid_files_message != null"
              color="pink"
              dark
              dismissible
              type="error"
              
              transition="scale-transition"
            >
              {{ invalid_files_message }}
            </v-alert>
                      

               <!-- <v-progress-circular
              :rotate="90"
              :size="100"
              :width="15"
              :value="progress_value"
              color="teal"

            >
              {{ progress_value }} %
            </v-progress-circular> -->

            <!-- STEPS -->

            <v-stepper
                v-model="current_step"
                vertical
                non-linear
              >

<!-- 
            <div class="text-center pa-6 secondary--text">
                <h3 class="mb-4">Free background removal for images and videos</h3>
              <img src="demo.jpg" height="150" class="rounded" />
            </div> -->


            <v-row>
                
                <v-col cols="4" class="">
                    <img src="demo.jpg" height="140" class="rounded ma-4"/>
                </v-col>

                <v-col cols="4" class="my-auto text-center">
                    <span style="font-size: 170%; font-weight: bold; color: #886677;"><u>Free</u> Background Removal</span>
                    <p class="" style="font-size: 150%;  color: #886677;">for images and videos</p>
                </v-col>

                <!-- <v-col cols="3" class="my-auto text-center">
                    <strong class="ml-1"> Free background removal <br/> for images and videos</strong>
                </v-col> -->

                <v-col cols="4" class="my-auto">
                    
                    <p class="ml-6"> 
                        <v-icon color="green" class="pr-2">
                            mdi-checkbox-marked-circle
                        </v-icon>
                    Completely in browser</p>

                    <p class="ml-6">
                        <v-icon color="green" class="pr-2">
                            mdi-checkbox-marked-circle
                        </v-icon>
                    No data leaves your computer!
                    </p>
                    

                </v-col>

                <!-- <v-spacer/> -->

                


                
            </v-row>


              <v-divider></v-divider>
                <v-stepper-step
                  :complete="current_step > 1"
                  
                  step="1"
                >

                <!-- =========== STEP 1 ========== -->

                  Select Video
                  
                </v-stepper-step>

                <v-stepper-content step="1">
                  
<!--                     <div
                      v-for="file in video_files"
                      :key="file.name"
                    >
                      {{ file.name }} size: {{ Math.round(file.size / 10000) / 100 }}  MB
                    </div>
 -->

                    <Uploader ref="uploader" v-on:changed="onFilesChanged" v-on:info_changed="onFilesInfoChanged " />
                      
                      <!-- v-show="video_files.length > 0"     -->
                    <v-btn
                      
                      :disabled="video_files.length == 0"
                      color="primary"
                      class="mb-6"
                      @click="nextStep"
                    >
                      Next Step
                    </v-btn>

                </v-stepper-content>

                <v-stepper-step
                  :complete="current_step > 2"
                  step="2"
                >
                  Choose Settings
                  

                </v-stepper-step>

                <v-stepper-content step="2">
                  
                  <v-card
                    color="grey lighten-4"
                    class="mb-6 pa-4"
                    elevation="0"
                  >

                    <h4 v-if="process_mode=='images'">No Settings for images</h4>
                   <h4 v-if="process_mode=='video'">Select Background Color</h4>
                   
                   <v-color-picker
                  class="ma-5 mb-8"
                  elevation="4"
                  v-if="process_mode=='video'"
                  :swatches="swatches"
                    show-swatches
                    v-model="color_picker_rgba"
                    ></v-color-picker>

                    <!-- <v-divider></v-divider>
                    some other thing
 -->
   
                  </v-card>

                  <v-btn
                  
                  color="primary"
                  class="mb-4"
                  @click="processFiles"
                  :disabled="video_files.length == 0 || load_state >= 2 || load_state == 0"
                  :loading="load_state >= 2 || load_state == 0"
                >
                  Process
                  <v-icon
                    dark
                    right
                  >
                    mdi-checkbox-marked-circle
                  </v-icon>
                </v-btn>


<!--                   <v-btn text>
                    Cancel
                  </v-btn>
 -->
                </v-stepper-content>

                <v-stepper-step
                  :complete="load_state >= 5"
                  step="3"
                >
                <div>
                  Process {{ process_mode == null ? "Video or Images" : process_mode }}
                  <v-progress-circular
                      indeterminate
                      size="20"
                      v-if="load_state > 1 && load_state < 5"
                    ></v-progress-circular>
                </div>
                </v-stepper-step>

                <v-stepper-content step="3">

                  <v-card
                    color="grey lighten-4"
                    class="mb-4 pa-4"
                    elevation="0"
                    min-height="500"
                  >

                  <v-overlay :value="processing_overlay" absolute opacity="0.2">
                    <v-progress-circular
                      indeterminate
                      size="64"
                    ></v-progress-circular>
                  </v-overlay>

<!--                   <v-progress-circular
                      indeterminate
                      size="30"
                      v-if="load_state > 1 && load_state < 5"
                    ></v-progress-circular>
 -->
                
                <div class="text-center">
                  <!-- <h3>{{ message }}</h3> -->
                  <h2 class="text-h6 primary--text">
                    {{ message }}
                    </h2>
                </div>

                  <div class="pa-4 mx-auto">

                  <v-progress-linear
                      v-model="progress_value"
                      height="20"
                      rounded
                      v-if="load_state > 2 && load_state < 5"
                      :indeterminate="load_state == 4"
                      
                    >
                      <strong>{{ progress_value }}</strong>
                    
                    </v-progress-linear>

                    </div>

                    <video id="output-video" style="display: none; max-width: 70%;" class="ma-4" controls></video>
                    <a href="#" style="display: none;" id="videolink" download="video.mp4">DOWNLOAD</a>

                  </v-card>
                  
                  <v-btn
                    color="primary"
                    class="ma-4"
                    v-if="process_mode=='video'"
                    :disabled="load_state < 5"
                    @click="downloadVideo"
                  >
                    Download MP4
                  </v-btn>

<!--                   <v-btn
                    color="primary"
                    class="ma-4"
                    @click="downloadImages"
                  >
                    Download Images
                  </v-btn> -->

                  <v-btn
                    color="secondary"
                    class="ma-4"
                    v-if="process_mode=='video'"
                    @click="uploadAnotherVideo"
                    :disabled="load_state < 5"
                  >
                    Upload Another Video
                  </v-btn>

<!--                   <v-btn text>
                    Cancel
                  </v-btn>
 -->                  


                </v-stepper-content>

                
              </v-stepper>
              

            <!-- </v-sheet> -->


                  <v-card
                    
                    class="mt-12"
                    rounded
                    
                  >



                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title><h4>Notes</h4></v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>

                    <v-list-item two-line>
                      <v-list-item-content>
                        <v-list-item-title>Experimental</v-list-item-title>
                        <v-list-item-subtitle>Currently slow and RAM hungry</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>

                    <v-list-item two-line>
                      <v-list-item-content>
                        <v-list-item-title>Max File Size</v-list-item-title>
                        <v-list-item-subtitle>
                          Limit videos to 5 - 10 mb
                        </v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-card>



          </v-col>

        </v-row>

      </v-container>

      <br/><br/><br/><br/>
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


<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.8/FileSaver.js"></script> -->

<!-- <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@3.7.0/dist/tf.min.js"></script> -->

<script>

//import HelloWorld from './components/HelloWorld';
import Footer from './components/footer2.vue';
//import Toggle from './components/toggle.vue';
//import Sidebar from './components/sidebar.vue';
//import Steps from './components/steps.vue';

import Uploader from './components/uploader.vue';

import { createFFmpeg, fetchFile } from '@ffmpeg/ffmpeg';

import * as tf from '@tensorflow/tfjs';
//import { loadGraphModel } from '@tensorflow/tfjs-converter';

//var JSZip = require("jszip");

import JSZip from 'jszip';
import { saveAs } from 'file-saver';


export default {
  name: 'App',

  
  components: {
    //HelloWorld,
    Footer,
    //Sidebar,
    //Steps,
    Uploader,
    //Toggle,
  },

  data: () => ({

    ffmpeg : null,
    tf_model : null,
    
    links: [
        'Video BG Remover',
        'Image BG Remover',
      ],

      video_files : [],

      toggle_exclusive: undefined,

      overlay: false,

      processing_overlay: false,

      progress_value: "",

      num_warmup: 5,


      snackbar: false,
      snack_text: 'My timeout is set to 2000.',
      snack_timeout: 2000,

      current_step: 1,
      load_state : 0,
      process_mode : null,

      invalid_files_message : null,

      video: null,

      message: "hello",
      loading_message: "Loading...",

      bg_color : [0.0, 1.0, 0.0],

      color_picker_rgba: { r: 0, g: 255, b: 0, a: 1 },

      swatches: [
        ['#FF0000', '#AA0000', '#550000'],
        ['#FFFF00', '#AAAA00', '#555500'],
        ['#00FF00', '#00AA00', '#005500'],
        ['#00FFFF', '#00AAAA', '#005555'],
        ['#0000FF', '#0000AA', '#000055'],
      ],

  }),

  

  watch: {
      overlay (val) {
        val && setTimeout(() => {
          this.overlay = false
        }, 3000)
      },
    },

    created: function() {
        console.log("creted?");
    },

    mounted: function() {
        console.log("Moutnd? ");
        this.setup();
    },

  methods : {

    async setup() {

        // Load FFMPEG and TF.js 

        this.message = "Loading FFMPEG...";
        this.loading_message = "Loading FFMPEG...";
        this.ffmpeg = createFFmpeg({ log: true });
        await this.ffmpeg.load();

        console.log("ffmpeg loaded ------------- ");

        this.message = "Loading TF model...";
        this.loading_message = "Loading TF Model...";
        this.tf_model = await tf.loadGraphModel('./model/model.json');
        
        console.log("tf model loaded ------------- ");

        this.message = "Ready!";
        this.loading_message = "Ready";

        this.load_state = 1;



    },

    downloadVideo() {

        const video_download = document.getElementById('videolink');
        video_download.click();

    },

    downloadImages() {

    },

    uploadAnotherVideo() {

        location.reload();

        // this.current_step = 1;
        // this.load_state = 1;
        // this.video_files = [];
        // this.$refs.uploader.files = [];
        // this.$refs.uploader.dropped = 0;
        // this.$refs.uploader.Imgs = [];

        // const video = document.getElementById('output-video');
        // video.style.display = "none";
    },

    async processFiles() {

        if ( this.process_mode == 'video' ) {
            await this.processVideo();
        } else if ( this.process_mode == 'images' ) {
            await this.processImages();
        }
        
    },

    checkFilesMode() {

        // Check that we have a valid set of files to work on 
        // Valid sets:
        //  1. Group of images of same dims 
        //  2. Single video 

        

        const files_info = this.$refs.uploader.files_info;

        for ( const i in files_info ) {
            if ( files_info[i]['complete'] == false ) {
                console.log('incomplete');
                return;
            }
        }

        console.log(" about to check these files... " + files_info.length );

        // height: 1024
        // name: "face-ring.jpg"
        // type: "image/jpeg"
        // width: 1024
        // image
        // video

        const types = new Set();
        const dims = new Set();

        for ( const i in files_info ) {
            
            const info = files_info[i];
            types.add( info["type"].slice(0, 5) );

            if ( info["type"].startsWith('image') ) {

                var dim_str = "" + info["width"].toFixed(0) + "x" + info["height"].toFixed(0);

                //dims.add( [info["width"], info["height"] ] );
                dims.add( dim_str );

                console.log("Image: size: " + info["width"] + " x " + info["height"] );
            }

        }

        console.log("  dims: " + Array.from(dims).join(', ') + " len: " + dims.size );
        console.log("  types: " + Array.from(types).join(', ') );

        if ( files_info.length == 0  ) {

            console.log(" NO FILES ---------");
            this.process_mode = null;
            this.invalid_files_message = null;

        } else if ( types.has('video') && files_info.length == 1 ) {
            
            this.process_mode = 'video';
            this.invalid_files_message = null;

        } else if ( types.has('image') && dims.size == 1 && types.size == 1 ) {

            this.process_mode = 'images';
            this.invalid_files_message = null;

        } else {

            //console.log("else ---- " + dims.size + " , " + ty);

            this.process_mode = null;

            const STANDARD_MESSAGE = "Please upload either a single video, or multiple images of the same dimensions";

            // Determine error to show
            if ( types.has('video') && types.has('image') ) {
                this.invalid_files_message = STANDARD_MESSAGE + " Don't mix videos and images";
            } else if ( types.has('image') && dims.size > 1 ) {
                this.invalid_files_message = STANDARD_MESSAGE + " All images should be the same dimensions, got: " + Array.from(dims).join(', ');
            } else {
                this.invalid_files_message = STANDARD_MESSAGE;
            }

        }

    },

    readFileAsync(file) {
        return new Promise((resolve, reject) => {

            let reader = new FileReader();

            reader.onload = () => {
                resolve(reader.result);
            };

            reader.onerror = reject;

            reader.readAsDataURL(file);
        })
    },

    async processImages() {

        this.load_state = 2;

        this.current_step = 3;

        this.processing_overlay = true;

        this.bg_color = [ this.color_picker_rgba['r'] / 255.0,  this.color_picker_rgba['g'] / 255.0, this.color_picker_rgba['b'] / 255.0 ];

        console.log( " process images: " + this.video_files );

        var zip = new JSZip();

        const model = this.tf_model;

        var image_files = this.video_files;

        const num_warmup = this.num_warmup;
        for ( var w = 0; w < num_warmup; w++) {
            image_files.splice(0, 0, image_files[0]);
        }

        // Set initial recurrent state
        let [r1i, r2i, r3i, r4i] = [tf.tensor(0.), tf.tensor(0.), tf.tensor(0.), tf.tensor(0.)];

        // Set downsample ratio
        const downsample_ratio = tf.tensor(0.5);

        const canvas = document.querySelector('canvas');
    
        this.message = 'Reading Images...';

        //var image_files_out = [];
        for ( const idx in image_files ) {

            const img_file = image_files[idx];

            console.log(" reading image file: " + img_file.name );

            var progress = (idx / (image_files.length-1) ) * 100.0;

            this.progress_value = progress.toFixed(0) + "%";

            await tf.nextFrame();

            let dataURL = await this.readFileAsync(img_file);

            const frame_img = new Image();
            frame_img.src = dataURL;
            await frame_img.decode();

            const img = tf.browser.fromPixels( frame_img );
            const src = tf.tidy(() => img.expandDims(0).div(255)); // normalize input

            const [fgr, pha, r1o, r2o, r3o, r4o] = await model.executeAsync(
                {src, r1i, r2i, r3i, r4i, downsample_ratio}, // provide inputs
                ['fgr', 'pha', 'r1o', 'r2o', 'r3o', 'r4o']   // select outputs
            );

            
            //this.drawMatte(fgr.clone(), pha.clone(), canvas, img_path, ffmpeg);
            
            const img_name = img_file.name;

            const dont_save = idx < num_warmup;
            //this.drawMatte(fgr.clone(), pha.clone(), canvas, img_path, ffmpeg, this.bg_color);
            await this.drawAndZip(fgr.clone(), pha.clone(), canvas, img_name, zip, dont_save);

            //this.drawMatte(null, pha.clone(), canvas, img_path, ffmpeg);
            canvas.style.background = 'rgb(0, 0, 0)';

            // Dispose old tensors.
            tf.dispose([img, src, fgr, pha, r1i, r2i, r3i, r4i]);

            // Update recurrent states.
            [r1i, r2i, r3i, r4i] = [r1o, r2o, r3o, r4o];

            // set to 'processing' state after first frame, since that takes a while
            if ( idx == 0 ) {
                this.message = 'Processing frames...';
                this.load_state = 3;
                this.processing_overlay = false;
            }

        } // end for image_files 


        this.progress_value = "Creating Zip...";
        this.message = 'Creating Zip...';
        this.load_state = 4; 

        zip.generateAsync({type:"blob"})
        .then(function (blob) {
            saveAs(blob, "images.zip");
        });

        this.message = 'Complete';
        this.progress_value = "Complete";

        this.load_state = 5; // Done

    },

    async processVideo() {

        this.load_state = 2;

        // setTimeout( function() { 
        //     this.blah();
        // }, 600 );

        //setTimeout(() => { this.current_step = 3; }, 800 );


        this.current_step = 3;

        this.processing_overlay = true;

        this.bg_color = [ this.color_picker_rgba['r'] / 255.0,  this.color_picker_rgba['g'] / 255.0, this.color_picker_rgba['b'] / 255.0 ];

        console.log("Loading...");

        const ffmpeg = this.ffmpeg;
        const model = this.tf_model;

        const files = this.video_files;

        var video_name = files[0].name;

        console.log(" Processing video: " + video_name );

        // Set initial recurrent state
        let [r1i, r2i, r3i, r4i] = [tf.tensor(0.), tf.tensor(0.), tf.tensor(0.), tf.tensor(0.)];

        // Set downsample ratio
        const downsample_ratio = tf.tensor(0.5);

        const canvas = document.querySelector('canvas');

    
        this.message = 'Reading video';

        ffmpeg.FS('writeFile', video_name, await fetchFile(files[0]));

        //await ffmpeg.run('-i', video_name, '-ss', '0', '-to', '1', 'output.mp4');
        //ffmpeg -i "%1" frames/out-%03d.jpg

        await ffmpeg.FS('mkdir', 'frames')

        let fmt = ".png";

        await ffmpeg.run('-i', video_name, 'frames/out-%03d' + fmt);

        this.message = 'Initializing...';

        // const data = ffmpeg.FS('readFile', 'frames/out-001.jpg');
        // const image = document.getElementById('output-image');
        // image.src = URL.createObjectURL(new Blob([data.buffer], { type: 'image/jpeg' }));

        var images = ffmpeg.FS("readdir", "frames");
        images = images.filter(img_path => img_path.endsWith(fmt));

        console.log("Got images" + images.length );

        //var idx = 0;

        //this.load_state = 3;

        for ( const idx in images ) {

            var img_path = images[idx];

            var progress = (idx / (images.length-1) ) * 100.0;

            var progress_str = "";

            for ( var i = 0; i < progress; i ++ ) {
                progress_str = progress_str + "|";
            }

            //progress_elem.innerHTML = progress.toFixed(0) + "% Complete";;
            //this.progress_value = Math.round(progress).toString() +;
            this.progress_value = progress.toFixed(0) + "%";

            //message.innerHTML = progress_str

            if ( img_path.endsWith(fmt) ) {

                img_path = "frames/" + img_path;

                //console.log(img_path);

                await tf.nextFrame();


                const data = ffmpeg.FS('readFile', img_path);
                //const image = document.getElementById('output-image');
                //image.src = URL.createObjectURL(new Blob([data.buffer], { type: 'image/jpeg' }));

                const frame_img = new Image();
                //frame_img.src = URL.createObjectURL(new Blob([data.buffer], { type: 'image/jpeg' }));
                frame_img.src = URL.createObjectURL(new Blob([data.buffer], { type: 'image/png' }));
                await frame_img.decode();

                // (async () => {
                //   const img = new Image();
                //   img.src = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png";
                //   await img.decode();
                //   // img is ready to use
                //   console.log( `width: ${ img.width }, height: ${ img.height }` );
                // })();

                //const imageBuffer = fs.readFileSync(path);
                //const tfimage = tfnode.node.decodeImage(imageBuffer);
                //const img = tfnode.node.decodeImage( await fetchFile(img_path) );
                //const imageData = new ImageData(await fetchFile(img_path) , );
                const img = tf.browser.fromPixels( frame_img );

                //const img = await webcam.capture();
                const src = tf.tidy(() => img.expandDims(0).div(255)); // normalize input

                const [fgr, pha, r1o, r2o, r3o, r4o] = await model.executeAsync(
                    {src, r1i, r2i, r3i, r4i, downsample_ratio}, // provide inputs
                    ['fgr', 'pha', 'r1o', 'r2o', 'r3o', 'r4o']   // select outputs
                );

                // r1i = r1o;
                // r2i = r2o;
                // r3i = r3o;
                // r4i = r4o; // not sure, @cc added this , the recurrent values should update right? 

                //this.drawMatte(fgr.clone(), pha.clone(), canvas, img_path, ffmpeg);
                this.drawMatte(fgr.clone(), pha.clone(), canvas, img_path, ffmpeg, this.bg_color);
                //this.drawMatte(null, pha.clone(), canvas, img_path, ffmpeg);
                canvas.style.background = 'rgb(0, 0, 0)';

                //canvas.style.background = 'rgb(0, 255, 0)'; 
                //canvas.style.background = 'rgb(120, 255, 155)'; 

                // Dispose old tensors.
                tf.dispose([img, src, fgr, pha, r1i, r2i, r3i, r4i]);

                // Update recurrent states.
                [r1i, r2i, r3i, r4i] = [r1o, r2o, r3o, r4o];

                // set to 'processing' state after first frame, since that takes a while
                if ( idx == 0 ) {
                    this.message = 'Processing frames...';
                    this.load_state = 3;
                    this.processing_overlay = false;
                }


          }

        }

        this.progress_value = "Creating Video...";
        this.message = 'Creating video...';
        this.load_state = 4; 

        
        const ext = "mp4";
        const codec = ext == "mp4" ? 'libx264' : 'libvpx';
        const video_out_name = "video." + ext;
        
        // By default the CRF value can be from 4–63, and 10 is a good starting point. Lower values mean better quality.
        // ffmpeg -i input.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output.webm

        await ffmpeg.run('-framerate', '30', '-pattern_type', 'glob', '-i', 'frames/*.png', '-c:v', codec, '-pix_fmt', 'yuv420p', video_out_name);

        const data = ffmpeg.FS('readFile', video_out_name);

        const video = document.getElementById('output-video');
        //video.src = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
        video.src = URL.createObjectURL(new Blob([data.buffer], { type: 'video/'+ext }));
        video.style.display = "block";

        const video_download = document.getElementById('videolink');
        video_download.href = video.src;
        video_download.download = video_out_name;

        this.message = '';

        this.load_state = 5; // Done

      
        


















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


    dataURItoBlob(dataURI) {
      // convert base64 to raw binary data held in a string
      // doesn't handle URLEncoded DataURIs - see SO answer #6850276 for code that does this
      var byteString = atob(dataURI.split(',')[1]);

      // separate out the mime component
      //var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0]

      // write the bytes of the string to an ArrayBuffer
      var ab = new ArrayBuffer(byteString.length);

      // create a view into the buffer
      var ia = new Uint8Array(ab);

      // set the bytes of the buffer to the correct values
      for (var i = 0; i < byteString.length; i++) {
          ia[i] = byteString.charCodeAt(i);
      }

      return ia;

      // write the ArrayBuffer to a blob, and you're done
      //var blob = new Blob([ab], {type: mimeString});
      //return blob;

    },

    async drawAndZip(fgr, alpha_matte, canvas, img_name, zip, dont_save) {

        const rgba = tf.tidy(() => {
          const rgb = fgr.squeeze(0).mul(255).cast('int32');
          const a = alpha_matte.squeeze(0).mul(255).cast('int32');
          return tf.concat([rgb, a], -1);
        });

        fgr && fgr.dispose();
        alpha_matte && alpha_matte.dispose();

        const [height, width] = rgba.shape.slice(0, 2);
        const pixelData = new Uint8ClampedArray(await rgba.data());
        const imageData = new ImageData(pixelData, width, height);

        canvas.width = width;
        canvas.height = height;

        canvas.getContext('2d').putImageData(imageData, 0, 0);

        //var img_png = new png.PNG({width: width, height: height});
        //img_png.data = Buffer.from(pixelData);
        //img_png.pack().pipe(fs.createWriteStream('tick.png'))
        // This does not work -- encodes the base64 string as a file and not a real PNG
        //await ffmpeg.FS('writeFile', img_path_out, img_png.pack());

        const imgAsDataURL = canvas.toDataURL("image/png", 1);
        const img_blob = this.dataURItoBlob(imgAsDataURL);

        if ( img_name.endsWith('.jpg') ) {
            img_name = img_name.replace(".jpg", ".png");
        }

        

        // TODO: call canvas.blob directly ? 
        if ( dont_save == false ) {
            console.log( " ====> Zipping image: " + img_name);
            zip.file(img_name, img_blob);
        } else {
            console.log( " ====> SKIPPING warmup image: " + img_name);
        }
        
        // screen.toBlob(function (blob) {
        //     zip.file("hello.png", blob);
        // });

        //await ffmpeg.FS('writeFile', img_path_out, img_blob);
        //console.log("Wrote file: " + img_path_out );

        rgba.dispose();

    },


    async drawMatte(fgr, alpha_matte, canvas, img_path_out, ffmpeg, bg_color) {

        // const rgba = tf.tidy(() => {
          
        //   const rgb = (fgr !== null) ?
        //       fgr.squeeze(0).mul(255).cast('int32') :
        //       tf.fill([alpha_matte.shape[1], alpha_matte.shape[2], 3], 255, 'int32');
          
        //   const a = (alpha_matte !== null) ?
        //       alpha_matte.squeeze(0).mul(255).cast('int32') :
        //       tf.fill([fgr.shape[1], fgr.shape[2], 1], 255, 'int32');

        //   return tf.concat([rgb, a], -1);

        // });
        console.log(bg_color);

        // real alpha channel == matte 
        // const rgba = tf.tidy(() => {
        //   const rgb = fgr.squeeze(0).mul(255).cast('int32');
        //   const a = alpha_matte.squeeze(0).mul(255).cast('int32');
        //   return tf.concat([rgb, a], -1);
        // });

        // blends the foreground with a bg color based on alpha matte -
        // alpha channel is 255 
        const rgba = tf.tidy(() => {
            
            const matte = alpha_matte.squeeze(0);
            
            var bg = tf.fill([fgr.shape[1], fgr.shape[2], 3], 255, 'float32');
            
            bg = bg.mul([bg_color[0], bg_color[1], bg_color[2]]);

            bg = bg.mul( matte.mul(-1.0).add(1.0) );

            var rgb = fgr.squeeze(0).mul(255).mul(matte);
            rgb = rgb.add( bg );

            rgb = rgb.cast('int32');

            const a = tf.fill([fgr.shape[1], fgr.shape[2], 1], 255, 'int32');

            return tf.concat([rgb, a], -1);

        });

        fgr && fgr.dispose();
        alpha_matte && alpha_matte.dispose();

        const [height, width] = rgba.shape.slice(0, 2);
        const pixelData = new Uint8ClampedArray(await rgba.data());
        const imageData = new ImageData(pixelData, width, height);

        canvas.width = width;
        canvas.height = height;

        canvas.getContext('2d').putImageData(imageData, 0, 0);

        //var img_png = new png.PNG({width: width, height: height});
        //img_png.data = Buffer.from(pixelData);
        //img_png.pack().pipe(fs.createWriteStream('tick.png'))
        // This does not work -- encodes the base64 string as a file and not a real PNG
        //await ffmpeg.FS('writeFile', img_path_out, img_png.pack());

        const imgAsDataURL = canvas.toDataURL("image/png", 1);

        //console.log(" ---> Got png buffer: " + imgAsDataURL.length );

        const img_blob = this.dataURItoBlob(imgAsDataURL);
        await ffmpeg.FS('writeFile', img_path_out, img_blob);

        //console.log("Wrote file: " + img_path_out );

        rgba.dispose();

    },  


    nextStep() {
      console.log("next step!!");
      //this.$refs.steps.current_step = 2
      this.current_step = 2
    },

    onFilesChanged(files) {
        //console.log("files changed! " + files );
        this.video_files = files;
        
    },
    onFilesInfoChanged() {
        //console.log('info changed');
        this.checkFilesMode();
    },
 
    onColorChanged(c) {
        console.log("Color:" + c);
    }


  }

};
</script>
