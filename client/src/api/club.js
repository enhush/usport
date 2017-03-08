import axios from 'axios'

export default {
  add(data) {
    return axios.post('/api/v1/club', data)
  },
  getList() {
    return axios.get('/api/v1/club')
  },
}
