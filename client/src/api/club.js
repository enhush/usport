import axios from 'axios'

export default {
  add(data) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.post('/api/v1/club', data)
  },
  getList() {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.get('/api/v1/club')
  },
}
