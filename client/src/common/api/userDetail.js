import axios from 'axios'

export default {
  get() {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.get(`/api/v1/user-detail`)
  },

  // because of uploading data, used POST instead of PUT
  update(data) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`
    return axios.post('/api/v1/user-detail-update', data)
  },
}
