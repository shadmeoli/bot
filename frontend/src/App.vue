<template>
  <v-app>
    <v-app-bar
      app
      color="red"
      dark
    >

    <v-btn text v-on:click="getMessage()">
      <v-icon>mdi-food</v-icon>
    </v-btn>

      <v-spacer></v-spacer>

    
        <span class="mr-2">Get serverd</span>
        <v-icon>mdi-coffee</v-icon>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',

  data() {
    return {
      msg: '',
    };
  },

  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },

  created() {
    this.getMessage();
  }
};
</script>
