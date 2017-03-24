import * as types from '../mutation-types'
import api from '@/common/api'
import helper from '@/common/helper'

const state = {
  userDetail: {
    club: {},
    sportType: {}
  }
}

const mutations = {
  [types.SET_USER_DETAIL] (state, data) {
    state.userDetail = Object.assign({
      club: {},
      sportType: {}
    }, data)
  }
}

const actions = {

  async read ({ commit, dispatch }) {
    try {
      const {data: {userDetail}} = await api.userDetail.get()
      commit(types.SET_USER_DETAIL, userDetail)
    } catch (e) {
      helper.apiError(e, dispatch)
    }
  },

  async update ({ commit, dispatch }, payload) {
    try {
      const {data: {userDetail}} = await api.userDetail.update(payload)
      commit(types.SET_USER_DETAIL, userDetail)
      dispatch('showNotification', `Амжилттай`)
    } catch (e) {
      helper.apiError(e, dispatch)
    }
  }
}

const getters = {
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
