import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import club from './modules/club'
import notification from './modules/notification'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    auth,
    club,
    notification,
  }
})

export default store
