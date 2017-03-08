<template lang="html">
  <div class="column">
    <h4 class="title is-4">Клубын жагсаалт</h4>
    <div class="has-text-right">
      <router-link
        :to="{name: 'club-add'}"
        class="button is-dark is-small">
        Нэмэх
      </router-link>
    </div>
    <table class="content table is-bordered is-small">
      <thead>
        <tr>
          <th>№</th>
          <th>Нэр</th>
          <th>Байгуулагдсан хугацаа</th>
          <th>Зохион байгуулагч</th>
          <th>Холбоо барих</th>
          <th>Үйлдлүүд</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(club, index) in clubs">
          <td>{{index+1}}</td>
          <td>{{club.name}}</td>
          <td>{{club.createdDate}}</td>
          <td>{{club.organiserName}}</td>
          <td>{{club.phone}}</td>
          <td class="has-text-right">
            <i class="fa fa-window-close-o content is-small" aria-hidden="true"></i>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'

export default {
  created() {
    this.getClubs()
  },
  computed: {
    ...mapState({
      clubs: ({ club }) => club.clubs,
    }),
  },
  methods: {
    ...mapActions([
      'getClubs'
    ]),
  }
}
</script>

<style scoped>
  .p10 {
    padding: 10px;
  }
  .mb5 {
    margin-bottom: 5px;
  }
</style>
