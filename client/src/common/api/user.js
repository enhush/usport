import axios from 'axios'

export default {
  login (data) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.post('/api/v1/login', data)
  },
  get () {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.get(`/api/v1/user`)
  },
  update (data) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.put('/api/v1/user', data)
  }
}
