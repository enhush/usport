<template>
  <div class="container is-flex">
    <main-menu></main-menu>
    <router-view></router-view>
  </div>
</template>

<script>
import Menu from '@/components/Menu'

export default {
  components: {
    mainMenu: Menu
  }
}
</script>

<style scoped>

</style>
