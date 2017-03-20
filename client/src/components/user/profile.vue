<template lang="html">
  <div class="column">
    <div class="mb10">
      <h4 class="title is-4">Бүртгэлийн мэдээлэл</h4>
      <hr>
      <div class="columns">
        <div class="column is-one-third">
          <div class="level-item">
            <figure class="image is-96x96 is-center">
              <img v-if="image" :src="image">
              <img v-else src="http://bulma.io/images/placeholders/96x96.png">
            </figure>
          </div>
          <div class="level-item">
            <input v-if="image" type="button" @click="removeImage" value="Солих">
            <input v-else type="file" @change="fileChanged" class="is-small">
          </div>
        </div>
        <div class="column is-one-third" data-vv-scope="user">
          <form-input label="Хэрэглэгчийн нэр">
            <input slot="element" class="input is-small" type="text"
              name="username"
              v-model="username"
              v-validate:username.initial="'required'">

              <span slot="error" v-show="errors.has('user.username')" class="help is-danger">
                Зөв бөглөнө үү!
              </span>
          </form-input>
          <form-input label="Бүртгүүлсэн и-мэйл хаяг">
            <input slot="element" class="input is-small" type="email"
              v-model="email"
              name="email"
              v-validate:email.initial="'required|email'">
            <span slot="error" v-show="errors.has('user.email')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <div class="has-text-right mt10">
            <a class="button is-dark is-small" @click="update()">
              Хадгалах
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="mb10">
      <h4 class="title is-4">Дэлгэрэнгүй мэдээлэл</h4>
      <hr>
      <div class="columns">
        <div class="column">
          <form-input label="Регистрийн дугаар">
            <input slot="element" class="input is-small" type="text">
          </form-input>
          <form-input label="Ургийн овог">
            <input slot="element" class="input is-small" type="text">
          </form-input>
          <form-input label="Овог">
            <input slot="element" class="input is-small" type="text">
          </form-input>
          <form-input label="Нэр">
            <input slot="element" class="input is-small" type="text">
          </form-input>
          <form-input label="Хүйс">
            <div class="control" slot="element">
              <label class="radio">
                <input type="radio" name="member" >
                Эр
              </label>
              <label class="radio">
                <input type="radio" name="member" >
                Эм
              </label>
            </div>
          </form-input>
          <form-input label="Төрсөн өдөр">
            <input type="date" slot="element" class="input is-small">
          </form-input>
          <form-input label="Утас">
            <input type="text" slot="element" class="input is-small">
          </form-input>
        </div>
        <div class="column">
          <form-input label="Гэрийн хаяг">
            <textarea slot="element" class="textarea is-small"></textarea>
          </form-input>
          <form-input label="Имэйл хаяг">
            <input slot="element" class="input is-small">
          </form-input>
          <form-input label="Харьяа клуб">
            <div class="select is-small" slot="element">
              <select>
                <option>sdafasdf</option>
              </select>
            </div>
          </form-input>
          <form-input label="Спортын төрлүүд">
            <div class="select is-small" slot="element">
              <select>
                <option>sdafasdf</option>
              </select>
            </div>
          </form-input>
        </div>
        <div class="column">
          <p class="has-text-centered mb10">Шаардлагатай үед холбоо барих хүн</p>
          <form-input label="Нэр">
            <input slot="element" class="input is-small" type="text">
          </form-input>
          <form-input label="Утас">
            <input slot="element" class="input is-small" type="text">
          </form-input>
          <form-input label="Гэрийн хаяг">
            <textarea slot="element" class="textarea is-small" rows="5"></textarea>
          </form-input>
          <div class="has-text-right mt10">
            <a class="button is-dark is-small" @click="">
              Хадгалах
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapMutations, mapGetters } from 'vuex'
import FormInput from '@/shared-components/form-helper/FormInput'
import mixins from '@/common/mixins'

export default {
  components: {
    FormInput,
  },
  mixins: [mixins.routeGuardUser],
  data() {
    return {
      image: '',
      file: null,
      editedUsername: '',
      editedEmail: '',
    }
  },
  computed: {
    ...mapGetters({
      defaultUsername: 'username',
      defaultEmail: 'email',
    }),
    username: {
      get() {
        return this.editedUsername || this.defaultUsername
      },
      set(value) {
        this.editedUsername = value
      }
    },
    email: {
      get() {
        return this.editedEmail || this.defaultEmail
      },
      set(value) {
        this.editedEmail = value
      }
    },
  },
  methods: {
    ...mapActions([
      'updateUser'
    ]),
    update() {
      this.$validator.validateAll('user').then(() => {
        let form = new FormData()
        if (this.image) {
          form.append('image', this.file)
        }
        form.append('username', this.username)
        form.append('email', this.email)
        this.updateUser(form)

      }).catch(() => {})
    },
    fileChanged(event) {
      const files = event.target.files || event.dataTransfer.files

      if (!files.length) return

      this.createImage(files[0])
      this.file = files[0]
    },
    createImage(file) {
      const image = new Image()
      const reader = new FileReader()
      reader.onload = (event) => {
        this.image = event.target.result
      }
      reader.readAsDataURL(file)
    },
    removeImage(event) {
      this.image = ''
      this.file = null
    }
  },
}
</script>

<style scoped>
  .mlr10 {
    margin: 0 10px;
  }
  .mt10 {
    margin-top: 10px;
  }
  .mb10 {
    margin-bottom: 10px;
  }
  .mt5 {
    margin-top: 5px;
  }
  .mb5 {
    margin-bottom: 5px;
  }
</style>
