import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import club from './modules/club'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    auth,
    club,
  }
})

export default store
