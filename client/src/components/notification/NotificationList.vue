<template lang="html">
  <div class="notification-list">
    <template v-for="notification in notifications">
      <notification :notification="notification"></notification>
    </template>
  </div>
</template>

<script>
import Notification from './Notification'
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState({
      notifications: ({ notification }) => notification.notifications,
    }),
  },
  components: {
    Notification,
  },
}
</script>

<style>
.notification-list {
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 6000;
}
</style>
