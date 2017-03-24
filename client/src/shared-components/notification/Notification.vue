<template>
  <div class="notification animated" :class="notification.animation">
    {{ notification.msg }}
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: ['notification'],
  data () {
    return {
      timer: null
    }
  },
  methods: {
    ...mapActions([
      'closeNotification'
    ])
  },
  created () {
    const timeout = this.notification.hasOwnProperty('timeout') ? this.notification.timeout : true
    if (timeout) {
      this.timer = setTimeout(() => {
        clearTimeout(this.timer)
        this.notification.animation = 'fadeIn'
        this.closeNotification(this.notification)
      }, 3000)
    }
  }
}
</script>
<style lang="css">
  .notification {
    background: rgba(239, 66, 34, .8);
    box-shadow: 2px 2px 10px #ccc;
    padding: 10px;
    color: #fff;
  }
</style>
