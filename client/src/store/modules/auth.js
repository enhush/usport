import * as types from '../mutation-types'
import api from '@/common/api'

const state = {
  authenticated: false,
  invalid: false,
  user: {
    username: '',
    email: '',
    role: 0,
  },
}

const mutations = {
  [types.SET_AUTH] (state, data) {
    state.authenticated = data
  },
  [types.SET_USER] (state, data) {
    state.user = Object.assign({}, data)
  },
  [types.SET_INVALID] (state, data) {
    state.invalid = data
  },
}

const actions = {
  login({ commit, dispatch }, {data, router}) {

    api.auth.login(data).then(response => {
      const token = response.data.token
      const user = response.data.user

      localStorage.setItem('token', token)

      commit(types.SET_AUTH, true)
      commit(types.SET_USER, user)

      router.replace({name: 'club'})
    }).catch(() => {
      commit(types.SET_AUTH, false)
      commit(types.SET_INVALID, true)
    })
  },
  checkAuth({ commit }) {
    const auth = localStorage.getItem('token') ? true : false
    commit(types.SET_AUTH, auth)
    if (auth) {
      api.auth.getMe().then((data) => {
        commit(types.SET_USER, data.data.user)
      }).catch(() => {
        alert('Алдаа')
      })
    }
  },
}

const getters = {
}


export default {
  state,
  mutations,
  actions,
  getters,
}
