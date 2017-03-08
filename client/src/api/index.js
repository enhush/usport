import axios from 'axios'
import auth from '@/api/auth'
import club from '@/api/club'

axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`

export default {
  auth,
  club,
}
