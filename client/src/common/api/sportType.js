import axios from 'axios'

export default {
  read () {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.get('/api/v1/sportType')
  }
}
