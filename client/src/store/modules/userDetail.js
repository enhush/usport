import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  userDetail: {
    club: {},
    sportType: {},
  }
}

const mutations = {
  [types.SET_USER_DETAIL] (state, data) {
    state.userDetail = Object.assign({
      club: {},
      sportType: {}
    }, data)
  },
}

const actions = {

  read({ commit, dispatch }) {
    api.userDetail.get().then(({data: {userDetail}}) => {
      commit(types.SET_USER_DETAIL, userDetail)
    }).catch(() => {
      dispatch('logout', {root: true})
    })

  },

  update({ commit, dispatch }, payload) {
    api.userDetail.update(payload).then(({data: {userDetail}}) => {
      dispatch('showNotification', `Амжилттай`, {root: true})
      commit(types.SET_USER_DETAIL, userDetail)
    }).catch(({response: {data: {message = 'Алдаа'}}}) => {
      dispatch('showNotification', message, {root: true})
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
