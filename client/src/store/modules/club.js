import * as types from '../mutation-types'
import api from '@/api'

const state = {
  clubs: [],
}

const mutations = {
  [types.SET_CLUBS](state, data) {
    state.clubs = data
  },
}

const actions = {
  clubAdd({dispatch}, payload) {
    api.club.add(payload).then(() => {
      dispatch('getClubs')
    }).catch(() => {
    })
  },
  getClubs({commit}) {
    api.club.getList().then((response) => {
      const clubs = response.data.data
      commit(types.SET_CLUBS, clubs)
    }).catch(() => {
    })
  }
}

const getters = {
}


export default {
  state,
  mutations,
  actions,
  getters,
}
