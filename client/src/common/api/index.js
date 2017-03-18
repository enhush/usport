import axios from 'axios'
import auth from './auth'
import club from './club'
import judge from './judge'
import sportType from './sportType'
import judgeLevel from './judgeLevel'


axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`

export default {
  auth,
  club,
  judge,
  sportType,
  judgeLevel,
}
