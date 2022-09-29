import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'

// connection to the fast API
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
