import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  sportTypes: []
}

const mutations = {
  [types.SET_SPORT_TYPES](state, data) {
    state.sportTypes = data
  },
}

const actions = {

  read({ commit, dispatch }) {
    api.sportType.read().then(({data: {data: sportTypes}}) => {
      commit(types.SET_SPORT_TYPES, sportTypes)
    }).catch(({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message, {root: true})
      if (message.includes("jwt-error")) {
        dispatch('logout', {root: true})
      }
    })
  }
}

const getters = {
}


export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
}
