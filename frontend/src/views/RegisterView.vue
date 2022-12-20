<template>
  <div class="w-full h-screen bg-gray-900 flex justify-center">
    <div class="text-center">
      <h1 class="text-3xl text-white m-5">Register</h1>
      <div class="p-3 bg-sky-900 rounded-xl">
        <div class="m-3">
          <input v-model="account" class="bg-gray-900 w-full h-10 text-white rounded-md p-3 text-3xl placeholder-white" type="text" name="" id="" placeholder="Account..." />
        </div>
        <div class="m-3">
          <input v-model="password" class="bg-gray-900 w-full h-10 text-white rounded-md p-3 text-3xl placeholder-white" type="password" name="" id="" placeholder="Password..." />
        </div>
        <div class="m-3 flex justify-end">
          <router-link :to="{ name: 'login' }" class="text-white underline text-xl cursor-pointer">Here login</router-link>
        </div>
        <div class="m-3 flex justify-end">
          <button @click="submit" class="bg-gray-500 p-3 text-xl hover:bg-gray-300 duration-300 rounded-md focus:ring-8 focus:bg-gray-300">Register</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Url } from '@/api_url'

export default {
  data() {
    return {
      req_url: (Url + '/User'),
      account: '',
      password: '',
    }
  },

  methods: {
    async submit() {
      if (this.account.length !== 0 || this.password.length !== 0) {
        await fetch(this.req_url, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            account: this.account,
            password: this.password
          })
        })
        .then((data) => {
          if (data.status === 200) {
            this.$swal({
              title: 'Register Successfully.',
              icon: 'success'
            }).then(() => {
              window.location.href = '/'
            })
          }
        })
      } else {
        this.$swal({
          title: '帳號密碼不可為空白！',
          icon: 'warning'
        })
        return
      }
    }
  },

  mounted() {
    console.log(this.req_url)
  }
}
</script>