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
      dispatch('showNotification', `Шинээр ${payload.name} клуб нэмэгдэв`)
      dispatch('getClubs')
    }).catch((error) => {
      error = error.response.data
      error = ('message' in error) ? error : {message: 'Алдаа'}
      dispatch('showNotification', error.message)
    })
  },
  getClubs({commit}) {
    api.club.getList().then((response) => {
      const clubs = response.data.data
      commit(types.SET_CLUBS, clubs)
    }).catch((error) => {
      error = error.response.data
      error = ('message' in error) ? error : {message: 'Алдаа'}
      dispatch('showNotification', error.message)
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
