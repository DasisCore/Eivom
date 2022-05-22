<template>
  <div style="background-color: #dcf6f9">
    <p class="display-3 fw-bold">로그인</p>
    <account-error-list v-if="authError"></account-error-list>
    <div class="d-flex justify-content-center">
      <div style="height: 300px">
        <form @submit.prevent="login(credentials)">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">@</span>
            <label for="username"></label>
            <input v-model="credentials.username" id="username" type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" style="border-right: 0px;" required />
            <span class="input-group-text" id="basic-addon1" style="background-color: white;">&#60;</span>
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">@</span>
            <label for="password"></label>
            <input v-model="credentials.password" id="password" type="text" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1" style="border-right: 0px;" required />
            <button class="input-group-text" id="basic-addon1" style="background-color: white;">&#60;</button>
          </div>
        </form>
        <router-link to="/signup" class="nav-link fw-bold text-secondary fs-1"
        active-class="active">signup</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/account/AccountErrorList.vue'
export default {
  name: 'LoginView',
  components: {
      AccountErrorList,
    },
  data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  },
}
</script>

<style scoped>

</style>