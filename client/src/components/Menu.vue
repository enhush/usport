<template lang="html">
  <aside class="menu">
    <div class="card">
      <div class="card-image has-text-centered">
        <i class="fa fa-area-chart"></i>
      </div>
      <div class="card-content">
        МУҮХ-ны бүртгэлийн систем
      </div>
    </div>
    <ul class="menu-list" v-if="isAdmin">
      <li>
        <router-link
          :to="{name: 'club'}"
          :class="{ 'is-active': isClub }">
          Клуб
        </router-link>
      </li>
      <li>
        <a @click="toggle('judge')">Шүүгчид</a>
        <ul v-show="toggles['judge']">
          <li>
            <router-link
              :to="{name: 'judge'}"
              :class="{ 'is-active': isJudge}">
              -Бүртгэл
            </router-link>
          </li>
          <li>
            <router-link
              :to="{name: 'judge-request'}"
              :class="{ 'is-active': isJudgeRequest}">
              -Хүсэлт
            </router-link>
          </li>
        </ul>
      </li>
      <li>
        <a>Тамирчид</a>
      </li>
    </ul>
    <ul class="menu-list" v-if="!isAdmin">
      <li>
        <router-link
          :to="{name: 'profile'}"
          :class="{ 'is-active': isProfile}">
          Хувийн мэдээлэл
        </router-link>
      </li>
    </ul>
    <hr class="is-marginless">
    <ul class="menu-list">
      <li><a>Тэмцээн</a></li>
      <li><a>Авиралт</a></li>
      <li v-if="!isAdmin"><a>Зэрэг цол</a></li>
    </ul>
    <hr class="is-marginless">
    <ul class="menu-list" v-if="isAdmin">
      <li><a>Авиралтын зам</a></li>
      <li><a>Арга хэмжээ</a></li>
      <li><a>Спортын төрөл</a></li>
      <li><a>Авиралтын замын зэрэглэл</a></li>
    </ul>
    <hr class="is-marginless" v-if="isAdmin">
    <ul class="menu-list">
      <li><a>Нууц үг солих</a></li>
      <li>
        <a @click="logout()">
          Гарах
        </a>
      </li>
    </ul>
  </aside>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  created () {
    this.toggles['judge'] = this.isJudge
  },
  data () {
    return {
      toggles: {
        judge: false
      }
    }
  },
  methods: {
    ...mapActions([
      'logout'
    ]),
    toggle (name) {
      switch (name) {
        case 'judge':
          this.toggles[name] = !this.toggles[name] || this.isJudge || this.isJudgeRequest
          break
        default:
          break
      }
    }
  },
  computed: {
    ...mapGetters([
      'isAdmin'
    ]),
    isClub () {
      return this.$route.matched.some(
        record => record.name === 'club' ||
                  record.name === 'club-add')
    },
    isJudge () {
      return this.$route.matched.some(
        record => record.name === 'judge' ||
                  record.name === 'judge-add')
    },
    isJudgeRequest () {
      return this.$route.matched.some(
        record => record.name === 'judge-request' ||
                  record.name === 'judge-request-add')
    },
    isProfile () {
      return this.$route.matched.some(
        record => record.name === 'profile')
    }
  }
}
</script>

<style lang="css" scoped>
.card {
  padding: 10px 0;
  box-shadow: none;
  background-color: #FAFAFA;
}
</style>
