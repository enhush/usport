import axios from 'axios'

export default {
  login(data) {
    return axios.post('/api/v1/auth/login', data)
  },
  getMe() {
    return axios.get(`/api/v1/auth/me`)
  },
}
