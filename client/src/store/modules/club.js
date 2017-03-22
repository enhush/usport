import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  clubs: [],
}

const mutations = {
  [types.SET_CLUBS](state, data) {
    state.clubs = data
  },
}

const actions = {

  create({ dispatch }, payload) {
    api.club.create(payload).then(() => {
      dispatch('showNotification', `Амжилттай`, {root: true})
      dispatch('read')
    }).catch(({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message, {root: true})
      if (message.includes("jwt-error")) {
        dispatch('logout', {root: true})
      }
    })
  },

  read({ commit, dispatch }) {
    api.club.read().then(({data: {data: clubs}}) => {
      commit(types.SET_CLUBS, clubs)
    }).catch(({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message, {root: true})
      if (message.includes("jwt-error")) {
        dispatch('logout', {root: true})
      }
    })
  },
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
