<template>
  <div class="">
    <router-view></router-view>
    <notification-list></notification-list>
  </div>
</template>

<script>
import 'animate.css'
import 'font-awesome.css'
import 'bulma.css'
import NotificationList from '@/shared-components/notification/NotificationList'

export default {
  components: {
    NotificationList,
  },
  name: 'appRoot',
}

</script>

<style>

</style>
