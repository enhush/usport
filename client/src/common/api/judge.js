import axios from 'axios'

export default {
  create (data) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.post('/api/v1/judge', data)
  },
  read () {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.get('/api/v1/judge')
  }
}
