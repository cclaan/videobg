<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      

    >
      
<!--       <div class="d-flex align-center">
      </div>


      <div class="align-center text-center">
          <p>{{ message }}</p>
      </div>
 -->
    <v-spacer></v-spacer>

    <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          centered
          src="logo.png"
          transition="scale-transition"
          width="40"
        />
        <h3>Video Background Remover</h3>

      <v-spacer></v-spacer>

<!--       <v-tabs
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
 -->

<!--       <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Learn More</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
 -->      
    </v-app-bar>

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

                    <Uploader ref="uploader" v-on:changed="onFilesChanged" />
                      
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

                   <h4>Select Background Color</h4>
                   
                   <v-color-picker
                  class="ma-5 mb-8"
                  elevation="4"
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
                  @click="processVideo"
                  :disabled="video_files.length == 0 || load_state > 1"
                  :loading="load_state > 1"
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
                <v-text>
                  Process Video
                  <v-progress-circular
                      indeterminate
                      size="20"
                      v-if="load_state > 1 && load_state < 5"
                    ></v-progress-circular>
                </v-text>
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


      snackbar: false,
      snack_text: 'My timeout is set to 2000.',
      snack_timeout: 2000,

      current_step: 1,
      load_state : 0,

      video: null,

      message: "hello",

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
        this.ffmpeg = createFFmpeg({ log: true });
        await this.ffmpeg.load();


        this.message = "Loading TF model...";
        this.tf_model = await tf.loadGraphModel('./model/model.json');
        
        this.message = "Ready!";

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

        await ffmpeg.run('-framerate', '30', '-pattern_type', 'glob', '-i', 'frames/*.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', 'out.mp4');
        const data = ffmpeg.FS('readFile', 'out.mp4');

        const video = document.getElementById('output-video');
        video.src = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
        video.style.display = "block";

        const video_download = document.getElementById('videolink');
        video_download.href = video.src;
        video_download.download = "video.mp4";

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

        const img_blog = this.dataURItoBlob(imgAsDataURL);
        await ffmpeg.FS('writeFile', img_path_out, img_blog);

        //console.log("Wrote file: " + img_path_out );

        rgba.dispose();

    },  


    nextStep() {
      console.log("next step!!");
      //this.$refs.steps.current_step = 2
      this.current_step = 2
    },

    onFilesChanged(files) {
      this.video_files = files
    },

    onColorChanged(c) {
        console.log("Color:" + c);
    }


  }

};
</script>
