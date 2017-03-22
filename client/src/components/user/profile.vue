<template lang="html">
  <div class="column">
    <div class="mb10">
      <h4 class="title is-4">Бүртгэлийн мэдээлэл</h4>
      <hr>
      <div class="columns">

        <div class="column is-one-third" data-vv-scope="basic">

          <form-input label="Хэрэглэгчийн нэр">
            <input slot="element" class="input is-small" type="text"
              name="username"
              v-model="username"
              v-validate:username.initial="'required'">

              <span slot="error" v-show="errors.has('basic.username')" class="help is-danger">
                Зөв бөглөнө үү!
              </span>
          </form-input>
          <form-input label="Бүртгүүлсэн и-мэйл хаяг">
            <input slot="element" class="input is-small" type="email"
              v-model="email"
              name="email"
              v-validate:email.initial="'required|email'">
            <span slot="error" v-show="errors.has('basic.email')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <div class="has-text-right mt10">
            <a class="button is-dark is-small" @click="updateBasic()">
              Хадгалах
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="mb10">
      <h4 class="title is-4">Дэлгэрэнгүй мэдээлэл</h4>
      <hr>
      <div class="columns" data-vv-scope="detail">
        <div class="column">
          <div class="level-item">
            <figure class="image is-96x96">
              <img v-if="_image && _image !== 'changed'" :src="_image">
              <img v-else src="http://bulma.io/images/placeholders/96x96.png">
            </figure>
          </div>

          <div class="level-item mb10">
            <input v-if="_image && _image !== 'changed'" type="button" @click="removeImage" value="Солих">
            <input v-else type="file" @change="fileChanged" class="is-small">
          </div>

          <form-input label="Регистрийн дугаар">
            <input slot="element"
              name="register"
              v-model="register"
              v-validate:register.initial="'required'"
              class="input is-small"
              type="text">

            <span slot="error" v-show="errors.has('detail.register')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Ургийн овог">
            <input slot="element"
              name="familyname"
              v-model="familyname"
              v-validate:familyname.initial="'required'"
              class="input is-small"
              type="text">

            <span slot="error" v-show="errors.has('detail.familyname')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Овог">
            <input slot="element"
              name="lastname"
              v-model="lastname"
              v-validate:lastname.initial="'required'"
              class="input is-small"
              type="text">

            <span slot="error" v-show="errors.has('detail.lastname')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Нэр">
            <input slot="element"
              name="firstname"
              v-model="firstname"
              v-validate:firstname.initial="'required'"
              class="input is-small"
              type="text">

            <span slot="error" v-show="errors.has('detail.firstname')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Хүйс">
            <div class="control" slot="element">
              <label class="radio">
                <input type="radio" name="sex" value="false" v-model="sex">
                Эм
              </label>
              <label class="radio">
                <input type="radio" name="sex" value="true" v-model="sex">
                Эр
              </label>
            </div>
          </form-input>
        </div>
        <div class="column">
          <form-input label="Төрсөн өдөр">
            <input slot="element"
            name="birthday"
            v-model="birthday"
            v-validate:birthday.initial="'required'"
            class="input is-small"
            type="date">

            <span slot="error" v-show="errors.has('detail.birthday')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Утас">
            <input slot="element"
            name="phone"
            v-model="phone"
            v-validate:phone.initial="'required'"
            class="input is-small"
            type="text">
            <span slot="error" v-show="errors.has('detail.phone')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Гэрийн хаяг">
            <textarea slot="element"
              name="address"
              v-model="address"
              v-validate:address.initial="'required'"
              class="textarea is-small"></textarea>
            <span slot="error" v-show="errors.has('detail.address')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Имэйл хаяг">
            <input slot="element"
              name="detailEmail"
              v-model="detailEmail"
              v-validate:detailEmail.initial="'required'"
              class="input is-small"
              type="text">
            <span slot="error" v-show="errors.has('detail.detailEmail')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Харьяа клуб">
            <div class="select is-small" slot="element">
              <select
                v-model="clubId"
                name="clubId"
                v-validate:clubId.initial="'required'">
                <option v-for="option in clubs" :value="option.id">
                  {{option.name}}
                </option>
              </select>
            </div>
            <span slot="error" v-show="errors.has('detail.clubId')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Спортын төрлүүд">
            <div class="select is-small" slot="element">
              <select
                v-model="sportTypeId"
                name="sportType"
                v-validate:sportType.initial="'required'">
                <option v-for="option in sportTypes" :value="option.id">{{option.name}}</option>
              </select>
            </div>
            <span slot="error" v-show="errors.has('detail.sportTypeId')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
        </div>
        <div class="column">
          <p class="has-text-centered mb10">Шаардлагатай үед холбоо барих хүн</p>
          <form-input label="Нэр">
            <input slot="element"
              name="contactName"
              v-model="contactName"
              v-validate:contactName.initial="'required'"
              class="input is-small"
              type="text">

            <span slot="error" v-show="errors.has('detail.contactName')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Утас">
            <input slot="element"
              name="contactPhone"
              v-model="contactPhone"
              v-validate:contactPhone.initial="'required'"
              class="input is-small"
              type="text">
            <span slot="error" v-show="errors.has('detail.contactPhone')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <form-input label="Гэрийн хаяг">
            <textarea slot="element"
              name="contactAddress"
              v-model="contactAddress"
              v-validate:contactAddress.initial="'required'"
              class="textarea is-small" rows="5"></textarea>
            <span slot="error" v-show="errors.has('detail.contactAddress')" class="help is-danger">
              Зөв бөглөнө үү!
            </span>
          </form-input>
          <div class="has-text-right mt10">
            <a class="button is-dark is-small" @click="reset()">
              Эхний төлөв
            </a>
            <a class="button is-dark is-small" @click="updateDetail()">
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
  created() {
    this.readUserDetail()
    this.readClubs()
    this.readSportTypes()
  },
  data() {
    return {
      file: null,
      image: '',
      _username: '',
      _email: '',

      _register: '',
      _familyname: '',
      _lastname: '',
      _firstname: '',
      _sex: '',
      _birthday: '',
      _phone: '',
      _address: '',
      _detailEmail: '',
      _clubId: '',
      _sportTypeId: '',
      _contactName: '',
      _contactPhone: '',
      _contactAddress: '',
    }
  },
  computed: {
    ...mapState({
      defaultUserDetail: ({ userDetail }) => userDetail.userDetail,
      sportTypes: ({ sportType }) => sportType.sportTypes,
      clubs: ({ club }) => club.clubs,
    }),
    ...mapGetters({
      defaultUsername: 'username',
      defaultEmail: 'email',
    }),
    _image() {
      return this.image || this.defaultUserDetail.image
    },
    username: {
      get() {
        return this._username || this.defaultUsername
      },
      set(value) {
        this._username = value
      }
    },
    email: {
      get() {
        return this._email || this.defaultEmail
      },
      set(value) {
        this._email = value
      }
    },
    register: {
      get() {
        return this._register || this.defaultUserDetail.register
      },
      set(value) {
        this._register = value
      }
    },
    familyname: {
      get() {
        return this._familyname || this.defaultUserDetail.familyname
      },
      set(value) {
        this._familyname = value
      }
    },
    lastname: {
      get() {
        return this._lastname || this.defaultUserDetail.lastname
      },
      set(value) {
        this._lastname = value
      }
    },
    firstname: {
      get() {
        return this._firstname || this.defaultUserDetail.firstname
      },
      set(value) {
        this._firstname = value
      }
    },
    sex: {
      get() {
        return this._sex || this.defaultUserDetail.sex
      },
      set(value) {
        this._sex = value
      }
    },
    birthday: {
      get() {
        return this._birthday || this.defaultUserDetail.birthday
      },
      set(value) {
        this._birthday = value
      }
    },
    phone: {
      get() {
        return this._phone || this.defaultUserDetail.phone
      },
      set(value) {
        this._phone = value
      }
    },
    address: {
      get() {
        return this._address || this.defaultUserDetail.address
      },
      set(value) {
        this._address = value
      }
    },
    detailEmail: {
      get() {
        return this._detailEmail || this.defaultUserDetail.email
      },
      set(value) {
        this._detailEmail = value
      }
    },
    clubId: {
      get() {
        return this._clubId || this.defaultUserDetail.club.id
      },
      set(value) {
        this._clubId = value
      }
    },
    sportTypeId: {
      get() {
        return this._sportTypeId || this.defaultUserDetail.sportType.id
      },
      set(value) {
        this._sportTypeId = value
      }
    },
    contactName: {
      get() {
        return this._contactName || this.defaultUserDetail.contactName
      },
      set(value) {
        this._contactName = value
      }
    },
    contactPhone: {
      get() {
        return this._contactPhone || this.defaultUserDetail.contactPhone
      },
      set(value) {
        this._contactPhone = value
      }
    },
    contactAddress: {
      get() {
        return this._contactAddress || this.defaultUserDetail.contactAddress
      },
      set(value) {
        this._contactAddress = value
      }
    },
  },
  methods: {
    ...mapActions({
      updateUserBasic: 'update',
      readSportTypes: 'sportType/read',
      readClubs: 'club/read',
    }),
    ...mapActions('userDetail', {
      readUserDetail: 'read',
      updateUserDetail: 'update',
    }),
    reset() {
      this.file = null
      this.image = ''
      this._username = ''
      this._email = ''

      this._register = ''
      this._familyname = ''
      this._lastname = ''
      this._firstname = ''
      this._sex = ''
      this._birthday = ''
      this._phone = ''
      this._address = ''
      this._detailEmail = ''
      this._clubId = ''
      this._sportTypeId = ''
      this._contactName = ''
      this._contactPhone = ''
      this._contactAddress = ''
    },
    updateBasic() {
      this.$validator.validateAll('basic').then(() => {
        this.updateUserBasic({
          username: this.username,
          email: this.email,
        })

      }).catch(() => {})
    },
    updateDetail() {
      this.$validator.validateAll('detail').then(() => {
        let form = new FormData()

        if (this.image) {
          form.append('image', this.file)
        }
        form.append('register', this.register)
        form.append('familyname', this.familyname)
        form.append('lastname', this.lastname)
        form.append('firstname', this.firstname)
        form.append('sex', this.sex)
        form.append('birthday', this.birthday)
        form.append('phone', this.phone)
        form.append('address', this.address)
        form.append('email', this.email)
        form.append('clubId', this.clubId)
        form.append('sportTypeId', this.sportTypeId)
        form.append('contactName', this.contactName)
        form.append('contactPhone', this.contactPhone)
        form.append('contactAddress', this.contactAddress)

        this.updateUserDetail(form)

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
      this.image = 'changed'
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
