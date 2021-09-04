<script>
export default {
  name: "VueUploadImages", // vue component name
  data() {
    return {
      error: "",
      files: [],
      dropped: 0,
      Imgs: [],
      files_info: [],
    };
  },
  props: {
    max: Number,
    uploadMsg: String,
    maxError: String,
    fileError: String,
    clearAll: String,
  },
  methods: {
    dragOver() {
      this.dropped = 2;
    },
    dragLeave() {
      this.dropped = 0;
    },
    drop(e) {
      let status = true;
      let files = Array.from(e.dataTransfer.files)
      if (e && files) {
        files.forEach((file) => {
          if (file.type.startsWith("video") === false && file.type.startsWith("image") === false) status = false;
        });
        if (status == true) {
          if (
            this.$props.max &&
            files.length + this.files.length > this.$props.max
          ) {
            this.error = this.$props.maxError
              ? this.$props.maxError
              : `Maximum files is` + this.$props.max;
          } else {
            this.files.push(...files);
            this.previewImgs();
          }
        } else {
          this.error = this.$props.fileError
            ? this.$props.fileError
            : `Unsupported file type`;
        }
      }
      this.dropped = 0;
    },
    append() {
      this.$refs.uploadInput.click();
    },
    readAsDataURL(file) {
      return new Promise(function (resolve, reject) {
        let fr = new FileReader();
        fr.onload = function () {
          resolve(fr.result);
        };
        fr.onerror = function () {
          reject(fr);
        };
        fr.readAsDataURL(file);
      });
    },
    deleteImg(index) {
      this.Imgs.splice(index, 1);
      this.files.splice(index, 1);
      this.files_info.splice(index, 1);
      this.$emit("changed", this.files);
      this.$emit("info_changed", this.files_info);
      this.$refs.uploadInput.value = null;
    },

    previewImgs(event) {
      if (
        this.$props.max &&
        event &&
        event.currentTarget.files.length + this.files.length > this.$props.max
      ) {
        this.error = this.$props.maxError
          ? this.$props.maxError
          : `Maximum files is` + this.$props.max;
        return;
      }
      
      if (this.dropped == 0) this.files.push(...event.currentTarget.files);
      
      this.error = "";
      this.$emit("changed", this.files);
      this.$emit("info_changed", this.files_info);
      
      let readers = [];
      if (!this.files.length) return;

      for (let i = 0; i < this.files.length; i++) {
        readers.push(this.readAsDataURL(this.files[i]));
      }
      
      Promise.all(readers).then( (values) => {

        this.Imgs = values;

        for ( const idx in values ) {
            
            const file = this.files[idx];

            var file_info = {"type" : file.type, "name" : file.name , "complete" : false };

            if ( file.type.startsWith("image") ) {

                const dataURL = values[idx];
                const img = new Image();
                img.src = dataURL;
                img.decode() // TODO: shouldnt this be await or .then() ?
                  .then(() => {
                    
                    //file_info["width"] = img.width;
                    //file_info["height"] = img.height;
                    //file_info["complete"] = true;
                    this.files_info[idx]['width'] = img.width;
                    this.files_info[idx]['height'] = img.height;
                    this.files_info[idx]['complete'] = true;
                    console.log( " image: " + img.width + " h: " + img.height );
                    //this.files_info.push(file_info);
                    this.$emit("info_changed", this.files_info);
                });
                
                
            } else {

                file_info["complete"] = true;

            }

            this.files_info.push(file_info);

        }

        this.$emit("info_changed", this.files_info);

        //this.$emit("changed", this.files);


      });
    },
    reset() {
      this.$refs.uploadInput.value = null;
      this.Imgs = [];
      this.files = [];
      this.files_info = [];
      this.$emit("changed", this.files);
      this.$emit("info_changed", this.files_info);
    },
  },
};
</script>

<template>
  <div
    class="container pa-6 mb-6"
    @dragover.prevent="dragOver"
    @dragleave.prevent="dragLeave"
    @drop.prevent="drop($event)"
  >
    <div class="drop" v-show="dropped == 2"></div>
    <!-- Error Message -->
    <div v-show="error" class="error">
      {{ error }}
    </div>

    <!-- To inform user how to upload image -->
    <div v-show="Imgs.length == 0" class="beforeUpload">
      <input
        type="file"
        style="z-index: 1"
        accept="video/*,image/*"
        ref="uploadInput"
        @change="previewImgs"
        multiple
      />
      <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
        <title>Upload Image</title>
        <g id="Upload_Image" data-name="Upload Image">
          <g id="_Group_" data-name="&lt;Group&gt;">
            <g id="_Group_2" data-name="&lt;Group&gt;">
              <g id="_Group_3" data-name="&lt;Group&gt;">
                <circle
                  id="_Path_"
                  data-name="&lt;Path&gt;"
                  cx="18.5"
                  cy="16.5"
                  r="5"
                  style="
                    fill: none;
                    stroke: #bbb;
                    stroke-linecap: round;
                    stroke-linejoin: round;
                  "
                />
              </g>
              <polyline
                id="_Path_2"
                data-name="&lt;Path&gt;"
                points="16.5 15.5 18.5 13.5 20.5 15.5"
                style="
                  fill: none;
                  stroke: #bbb;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                "
              />
              <line
                id="_Path_3"
                data-name="&lt;Path&gt;"
                x1="18.5"
                y1="13.5"
                x2="18.5"
                y2="19.5"
                style="
                  fill: none;
                  stroke: #bbb;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                "
              />
            </g>
            <g id="_Group_4" data-name="&lt;Group&gt;">
              <polyline
                id="_Path_4"
                data-name="&lt;Path&gt;"
                points="0.6 15.42 6 10.02 8.98 13"
                style="
                  fill: none;
                  stroke: #bbb;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                "
              />
              <polyline
                id="_Path_5"
                data-name="&lt;Path&gt;"
                points="17.16 11.68 12.5 7.02 7.77 11.79"
                style="
                  fill: none;
                  stroke: #bbb;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                "
              />
              <circle
                id="_Path_6"
                data-name="&lt;Path&gt;"
                cx="8"
                cy="6.02"
                r="1.5"
                style="
                  fill: none;
                  stroke: #bbb;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                "
              />
              <path
                id="_Path_7"
                data-name="&lt;Path&gt;"
                d="M19.5,11.6V4A1.5,1.5,0,0,0,18,2.5H2A1.5,1.5,0,0,0,.5,4V15A1.5,1.5,0,0,0,2,16.5H13.5"
                style="
                  fill: none;
                  stroke: #bbb;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                "
              />
            </g>
          </g>
        </g>
      </svg>

      <p class="mainMessage">
        Drop a single video or multiple images here
      </p>
      <p class="subMessage">Images should be of the same dimensions</p>

          <v-btn
              color="primary"
            >
              Select Video / Images
            </v-btn>

    </div>
    <div class="imgsPreview" v-show="Imgs.length > 0">
      
<!--       <button type="button" class="clearButton" @click="reset">
        {{ clearAll ? clearAll : "Clear All" }}
      </button>
 -->
      <div class="imageHolder" v-for="(img, i) in Imgs" :key="i">

        <img v-if="files[i].type.startsWith('image')" :src="img" />
        <img v-if="files[i].type.startsWith('video')" src="video-thumb.png" />

        
        <span class="videoname">{{ files[i].name }}</span>
        <span class="delete" style="color: white" @click="deleteImg(--i)">
          <svg
            class="icon"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
            />
          </svg>
        </span>
        <!-- <div class="plus" @click="append" v-if="++i == Imgs.length">+</div> -->
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  background: #f2f7fa;
  
  border-radius: 10px;
  padding: 30px;
  position: relative;
}
.drop {
  width: 100%;
  height: 100%;
  top: 0;
  border-radius: 10px;
  position: absolute;
  background-color: #f4f6ff;
  left: 0;
  border: 3px dashed #a3a8b1;
}
.error {
  text-align: center;
  color: red;
  font-size: 15px;
}
.beforeUpload {
  position: relative;
  text-align: center;
}
.beforeUpload input {
  width: 100%;
  margin: auto;
  height: 100%;
  opacity: 0;
  position: absolute;
  background: red;
  display: block;
}
.beforeUpload input:hover {
  cursor: pointer;
}
.beforeUpload .icon {
  width: 150px;
  margin: auto;
  display: block;
}
.imgsPreview .imageHolder {
  width: 150px;
  height: 150px;
  background: #fff;
  position: relative;
  border-radius: 10px;
  border: 1px solid #ddd;
  margin: 5px 5px;
  display: inline-block;
}
.imgsPreview .imageHolder img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}
.videoname {
  background: #eee;
  opacity: 0.95;
  position: absolute;
  width: 150px;
  height: 20px;
  font-size: 12px;
  color: #888;
  font-weight: bold;
  border-radius: 4px;
  padding: 2px;
  text-align: center;
  right: 0px;
  bottom: 0px;
}
.imgsPreview .imageHolder .delete {
  position: absolute;
  top: 4px;
  right: 4px;
  width: 29px;
  height: 29px;
  color: #fff;
  background: red;
  border-radius: 50%;
}
.imgsPreview .imageHolder .delete:hover {
  cursor: pointer;
}
.imgsPreview .imageHolder .delete .icon {
  width: 66%;
  height: 66%;
  display: block;
  margin: 4px auto;
}
.imgsPreview .imageHolder .plus {
  color: #2d3748;
  background: #07fafc;
  border-radius: 50%;
  font-size: 21pt;
  height: 36px;
  width: 36px;
  text-align: center;
  border: 1px dashed;
  line-height: 23px;
  position: absolute;
  right: -42px;
  bottom: 43%;
}
.mainMessage {
  color: #888;
  font-weight: bold;
  margin-bottom: 3px;
}
.subMessage {
  /*font-style: italic;*/
  color: #888;
}

.plus:hover {
  cursor: pointer;
}
.clearButton {
  color: #2d3748;
  position: absolute;
  top: 7px;
  right: 7px;
  background: none;
  border: none;
  cursor: pointer;
}
</style>