import Vue from 'vue'
import VueRouter from 'vue-router'
import VeeValidate from 'vee-validate'

import App from '@/components/App'
import router from '@/router'
import store from '@/store'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(VeeValidate)

store.dispatch('checkAuth')

/* eslint no-new: 0 */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router,
  store
})
