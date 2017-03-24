export default (response, dispatch) => {
  try {
    const {response: {data: {message = 'Алдаа'}}} = response
    dispatch('showNotification', message, {root: true})

    const {response: {status}} = response
    if (status === 401) {
      dispatch('logout', null, {root: true})
    }
  } catch (e) {
    dispatch('showNotification', 'Алдаа', {root: true})
  }
}
