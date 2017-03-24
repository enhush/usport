<template lang="html">
  <div class="column">
    <h4 class="title is-4">Шүүгчдийн жагсаалт</h4>
    <div class="has-text-right">
      <router-link
        :to="{name: 'judge-add'}"
        class="button is-dark is-small">
        Нэмэх
      </router-link>
    </div>
    <table class="content table is-bordered is-small">
      <thead>
        <tr>
          <th>№</th>
          <th>Овог Нэр</th>
          <th>Спортын төрөл</th>
          <th>Зэрэг цол</th>
          <th>Харьяа клуб</th>
          <th>Холбоо барих</th>
          <th>Үйлдлүүд</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(judge, index) in judges">
          <td>{{index+1}}</td>
          <td>{{judge.lastname.slice(0, 3) + '. ' + judge.firstname}}</td>
          <td>{{judge.sportType.name}}</td>
          <td>{{judge.judgeLevel.name}}</td>
          <td>{{judge.club.name}}</td>
          <td>{{judge.phone}}</td>
          <td class="has-text-right">
            <i class="fa fa-window-close-o content is-small" aria-hidden="true"></i>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import mixins from '@/common/mixins'

export default {
  mixins: [mixins.routeGuardAdmin],
  created () {
    this.read()
  },
  data () {
    return {
    }
  },
  computed: {
    ...mapState('judge', {
      judges: state => state.judges
    })
  },
  methods: {
    ...mapActions('judge', [
      'read'
    ])
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
