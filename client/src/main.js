import Vue from 'vue'
import VueRouter from 'vue-router'
import VeeValidate from 'vee-validate'

import App from '@/components/App'
import router from '@/router'
import store from '@/store'

/* global config */
Vue.config.productionTip = false

/* add plugins */
Vue.use(VueRouter)
Vue.use(VeeValidate)

/* check auth */
store.dispatch('check')

new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router,
  store,
})
