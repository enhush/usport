import * as types from '../mutation-types'

const state = {
  notifications: []
}

const mutations = {
  [types.ADD_NOTIFICATION](state, data) {
    state.notifications.push(data)
  },
  [types.CLOSE_NOTIFICATION](state, data) {
    const index = state.notifications.indexOf(data)
    if (index > -1) {
      state.notifications.splice(index, 1)
    }
  }
}

const actions = {
  showNotification({ commit }, msg) {
    const notification = {
      type: 'error',
      animation: 'fadeIn',
      msg,
    }
    commit(types.ADD_NOTIFICATION, notification)
  },
  closeNotification({ commit }, payload) {
    setTimeout(() => {
      commit(types.CLOSE_NOTIFICATION, payload)
    }, 500)
  }
}

export default {
  state,
  mutations,
  actions,
}
