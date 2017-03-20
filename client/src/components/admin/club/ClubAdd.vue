<template lang="html">
  <div class="column is-half">
    <h4 class="title is-4">Клуб нэмэх</h4>
    <div class="has-text-right">
      <a class="button is-dark is-small" @click="save()">
        Хадгалах
      </a>
      <router-link
        :to="{name: 'club'}"
        class="button is-dark is-small">
        Буцах
      </router-link>
    </div>

    <form-input label="Үүсгэн байгуулагч">
      <input slot="element" autofocus
        name="founder"
        v-model="founder"
        v-validate:founder.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('founder')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Байгуулагдсан огноо">
      <input slot="element"
        name="createdDate"
        v-model="createdDate"
        v-validate:createdDate.initial="'required'"
        class="input is-small" type="date">

      <span slot="error" v-show="errors.has('createdDate')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Нэр">
      <input slot="element"
        name="name"
        v-model="name"
        v-validate:name.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('name')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="И-Мэйл">
      <input slot="element"
        name="email"
        v-model="email"
        v-validate:email.initial="'required|email'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('email')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Вэбсайт">
      <input slot="element"
        name="website"
        v-model="website"
        v-validate:website.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('website')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Хаяг">
      <textarea slot="element"
        name="address"
        v-model="address"
        v-validate:address.initial="'required'"
        class="textarea is-small">
      </textarea>

      <span slot="error" v-show="errors.has('address')" class="help is-danger">
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
    <p class="content has-text-centered mt20">ЗОХИОН БАЙГУУЛАГЧ</p>
    <form-input label="Нэр">
      <input slot="element"
        name="organiserName"
        v-model="organiserName"
        v-validate:organiserName.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('organiserName')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="Утас">
      <input slot="element"
        name="organiserPhone"
        v-model="organiserPhone"
        v-validate:organiserPhone.initial="'required'"
        class="input is-small" type="text">

      <span slot="error" v-show="errors.has('organiserPhone')" class="help is-danger">
        Зөв бөглөнө үү!
      </span>
    </form-input>
    <form-input label="И-Мэйл">
      <input slot="element"
        name="organiserEmail"
        v-model="organiserEmail"
        v-validate:organiserEmail.initial="'required|email'"
        class="input is-small" type="email">

      <span slot="error" v-show="errors.has('organiserEmail')" class="help is-danger">
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
  data() {
    return {
      founder: '',
      createdDate: '',
      name: '',
      email: '',
      website: '',
      address: '',
      phone: '',
      organiserName: '',
      organiserEmail: '',
      organiserPhone: '',
    }
  },
  methods: {
    ...mapActions('club', [
      'create',
    ]),
    save() {
      this.$validator.validateAll().then(() => {
        this.create({
            founder: this.founder,
            createdDate: this.createdDate,
            name: this.name,
            email: this.email,
            website: this.website,
            address: this.address,
            phone: this.phone,
            organiserName: this.organiserName,
            organiserEmail: this.organiserEmail,
            organiserPhone: this.organiserPhone,
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
