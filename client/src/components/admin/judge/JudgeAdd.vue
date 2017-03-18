<template lang="html">
  <div class="column is-half">
    <h4 class="title is-4">Шүүгч нэмэх</h4>
    <div class="has-text-right">
      <a class="button is-dark is-small" @click="save()">
        Хадгалах
      </a>
      <router-link
        :to="{name: 'judge'}"
        class="button is-dark is-small">
        Буцах
      </router-link>
    </div>

    <form-input label="Овог">
      <input slot="element" autofocus
        name="lastname"
        v-model="lastname"
        v-validate:lastname.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('lastname')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Нэр">
      <input slot="element"
        name="firstname"
        v-model="firstname"
        v-validate:firstname.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('firstname')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Спортын төрөл">
      <div class="select is-small" slot="element">
        <select
          v-model="sportTypeId"
          name="sportType"
          v-validate:sportType.initial="'required'">
          <option v-for="option in sportTypes" :value="option.id">{{option.name}}</option>
        </select>
      </div>
      <span slot="error" v-show="errors.has('sportType')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Зэрэг цол">
      <div class="select is-small" slot="element">
        <select
          v-model="judgeLevelId"
          name="judgeLevel"
          v-validate:judgeLevel.initial="'required'">
          <option v-for="option in judgeLevels" :value="option.id">{{option.name}}</option>
        </select>
      </div>
      <span slot="error" v-show="errors.has('judgeLevel')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Харьяа клуб">
      <div class="select is-small" slot="element">
        <select
          v-model="clubId"
          name="club"
          v-validate:club.initial="'required'">
          <option v-for="option in clubs" :value="option.id">{{option.name}}</option>
        </select>
      </div>
      <span slot="error" v-show="errors.has('club')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Утас">
      <input slot="element"
        name="phone"
        v-model="phone"
        v-validate:phone.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('phone')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
  </div>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import FormInput from '@/shared-components/form-helper/FormInput'

export default {
  components: {
    FormInput,
  },
  created() {
    this.readSportTypes()
    this.readJudgeLevels()
    this.readClubs()
  },
  data() {
    return {
      lastname: '',
      firstname: '',
      phone: '',
      sportTypeId: 1,
      judgeLevelId: 1,
      clubId: 1,
    }
  },
  computed: {
    ...mapState({
      sportTypes: ({ sportType }) => sportType.sportTypes,
      judgeLevels: ({ judgeLevel }) => judgeLevel.judgeLevels,
      clubs: ({ club }) => club.clubs,
    }),
  },
  methods: {
    ...mapActions('judge', [
      'create',
    ]),
    ...mapActions({
      readSportTypes: 'sportType/read',
      readJudgeLevels: 'judgeLevel/read',
      readClubs: 'club/read',
    }),
    save() {
      this.$validator.validateAll().then(() => {
        this.create({
          lastname: this.lastname,
          firstname: this.firstname,
          phone: this.phone,
          sportTypeId: this.sportTypeId,
          judgeLevelId: this.judgeLevelId,
          clubId: this.clubId,
        })
      }).catch(() => {})
    },
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
  .mt20 {
    margin-top: 20px;
  }
</style>
