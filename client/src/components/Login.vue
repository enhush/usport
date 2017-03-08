<template>

  <div class="container">
    <section class="hero has-text-centered">
      <div class="hero-body">
        <h1 class="title">
          Монголын Уулчдын Холбоо
        </h1>
        <h2 class="subtitle">
          Систем
        </h2>
      </div>
    </section>
    <div class="columns is-centered is-mobile mt25">
      <div class="column is-one-third">
        <form class="columns is-gapless" @submit.prevent="beforeLogin()">
          <p class="column">
            <input autofocus
              @input="setInvalid(false)"
              class="input is-small"
              type="email"
              placeholder="И-мэйл"
              name="email"
              v-model="email"
              v-validate:email.initial="'required|email'">

            <span v-show="errors.has('email')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
            <span v-show="invalid" class="help is-danger">
              Нэр эсвэл нууц үг буруу байна!
            </span>
          </p>
          <p class="column">
            <input
              @input="setInvalid(false)"
              class="input is-small"
              type="password"
              placeholder="Нууц үг"
              name="password"
              v-model="password"
              v-validate:password.initial="'required'">

            <span v-show="errors.has('password')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </p>
          <p class="column is-2">
            <button class="button is-dark is-small is-fullwidth">Нэвтрэх</button>
          </p>
        </form>
      </div>
    </div>
  </div>

</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import * as types from '@/store/mutation-types'

export default {
  data() {
    return {
      email: '',
      password: '',
    }
  },
  computed: {
    ...mapState({
      invalid: ({ auth }) => auth.invalid,
    }),
  },
  methods: {
    ...mapMutations({
      setInvalid: types.SET_INVALID
    }),
    ...mapActions([
      'login'
    ]),
    beforeLogin() {
      this.$validator.validateAll().then(() => {
        this.login({
          data: {
            email: this.email,
            password: this.password,
          },
          router: this.$router,
        })
      }).catch(() => {})
    },
  }
}
</script>

<style scoped>
  .mt25 {
    margin-top: 25px;
  }
</style>
