<template>
  <div class="w-full h-screen bg-gray-900 flex justify-center">
    <div class="text-center">
      <h1 class="text-3xl text-white m-5">Login</h1>
      <div class="p-3 bg-sky-900 rounded-xl">
        <div class="m-3">
          <input v-model="account" class="bg-gray-900 w-full h-10 text-white rounded-md p-3 text-3xl placeholder-white" type="text" name="" id="" placeholder="Account..." />
        </div>
        <div class="m-3">
          <input v-model="password" class="bg-gray-900 w-full h-10 text-white rounded-md p-3 text-3xl placeholder-white" type="password" name="" id="" placeholder="Password..." />
        </div>
        <div class="m-3 flex justify-end">
          <router-link :to="{ name: 'register' }" class="text-white underline text-xl cursor-pointer">Here register</router-link>
        </div>
        <div class="m-3 flex justify-end">
          <button @click="login" class="bg-gray-500 p-3 text-xl hover:bg-gray-300 duration-300 rounded-md focus:ring-8 focus:bg-gray-300">Login</button>
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
      account: '',
      password: '',
      req_url: (Url + '/User')
    }
  },

  methods: {
    async login() {
      await fetch(this.req_url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          account: this.account,
          password: this.password
        })
      })
      .then( async (data) => {
        if (data.status === 200) {
          let res = await data.json()
          document.cookie = `s_id=${res['s_id']}; max-age=3600;`
          window.location.href = '/home'
        }
      })
    }
  }
}
</script>
