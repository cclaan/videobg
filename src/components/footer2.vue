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
        :key="link"
        color="grey"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
      <v-col
        class="grey lighten-4 py-4 text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Blue Berries</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      links: [
        "hello",
        "darkness",
        "my",
        "old",
        "friend"
      ],
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>