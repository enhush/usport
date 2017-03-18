import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import club from './modules/club'
import judge from './modules/judge'
import sportType from './modules/sportType'
import judgeLevel from './modules/judgeLevel'

import notification from './modules/notification'


Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    auth,
    club,
    judge,
    sportType,
    judgeLevel,
    notification,
  }
})

export default store
