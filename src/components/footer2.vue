<template>
  <v-footer
    color="grey lighten-4"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link[0]"
        color="grey"
        text
        :href="link[1]"
        rounded
        target="_blank"
        class="my-2"
      >
        {{ link[0] }}
      </v-btn>
      
      <v-col
        class="grey lighten-4 py-4 text-center"
        cols="12"
      >

      <p style="color: #888;">
        Built with <a href='https://github.com/ffmpegwasm'>ffmpeg wasm </a> and <a href='https://www.tensorflow.org/js'>tensorflow.js</a> and <a href='https://github.com/PeterL1n/RobustVideoMatting'>Robust Video Matting</a>
      </p>

      <p style="color: #888;">
        Have feedback or feature ideas? Send an email to <a :href="`mailto:`+email">{{email}}</a>
      </p>

      <p style="color: #888;">
        App Version - {{ version_number }}
      </p>
      <p style="color: #888;">
        {{ new Date().getFullYear() }} — <strong>Fun Labs</strong>
      </p>

      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      email: "cc@laan.com",
      links: [
        //["homepage", "https://labs.laan.com"],
        //["twitter", "https://twitter.com/laanlabs"]
      ],

      // icons: [
      //   'mdi-facebook',
      //   'mdi-twitter',
      //   'mdi-linkedin',
      //   'mdi-instagram',
      // ],

    }),

    props: {
      version_number: Number,
    }
  }
</script>