import axios from 'axios'

export default {
  login(data) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.post('/api/v1/auth/login', data)
  },
  getMe() {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.get(`/api/v1/auth/me`)
  },
}
