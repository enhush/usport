import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  judges: [],
}

const mutations = {
  [types.SET_JUDGES](state, data) {
    state.judges = data
  },
}

const actions = {

  create({ dispatch }, payload) {
    api.judge.create(payload).then(() => {
      dispatch('showNotification', `Амжилттай`, {root: true})
      dispatch('read')
    }).catch( ({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message, {root: true})
    })
  },

  read({ commit, dispatch }) {
    api.judge.read().then(({data: {data: judges}}) => {
      commit(types.SET_JUDGES, judges)
    }).catch(({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message, {root: true})
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
