import Vue from 'vue'
import Toasted from 'vue-toasted';
import App from './components/App'
import router from './router'
import VeeValidate from 'vee-validate'
import store from './store'

Vue.use(Toasted)
Vue.use(VeeValidate)

store.dispatch('checkAuth')

Vue.config.productionTip = false

new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router,
  store,
})
