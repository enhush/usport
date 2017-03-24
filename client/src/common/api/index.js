import axios from 'axios'
import user from './user'
import club from './club'
import judge from './judge'
import userDetail from './userDetail'
import sportType from './sportType'
import judgeLevel from './judgeLevel'

axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`

export default {
  club,
  judge,
  sportType,
  judgeLevel,
  user,
  userDetail
}
