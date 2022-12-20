<template>
  <div class="w-full h-screen bg-gray-900 overflow-auto">
    <NavbarVue></NavbarVue>
    <div class="mt-20 flex justify-center">
      <div class="w-10/12 h-full bg-sky-700 p-5 rounded-xl">
        <div class="bg-gray-500 p-3 md:flex md:justify-between rounded-lg">
          <input v-model="add_title" type="text" class="mb-3 md:mb-0 p-3 w-auto max-w-full text-3xl placeholder-black rounded-lg"
            placeholder="Title..." />
          <input v-model="add_content" type="text" class="mb-3 md:mb-0 p-3 w-auto max-w-full text-3xl placeholder-black rounded-lg"
            placeholder="Content..." />
          <DefaultButton @click="addTodo" class="">ADD Todo</DefaultButton>
        </div>
        <div v-for="todo in todos" :key="todo" class="w-full mt-3 bg-blue-900 p-2 md:flex md:justify-between rounded-lg">
          <h3 class="text-3xl text-white">
            Title: <span class=" underline">{{ todo.title }}</span>&nbsp;&nbsp;&nbsp;
          </h3>
          <p class="text-3xl text-white">
            Content: <span class=" underline">{{ todo.content }}</span>
          </p>
          <DefaultButton @click="deleteTodo(todo.todo_id)" class=" bg-red-500 hover:bg-red-700">Delete</DefaultButton>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Url } from '@/api_url'
import DefaultButton from '@/components/DefaultButton.vue'
import NavbarVue from '@/components/Navbar.vue'

export default {
  data() {
    return {
      req_url: (Url + '/Todo'),
      s_id: '',
      todos: [],
      add_title: '',
      add_content: '',
    }
  },

  components: {
    DefaultButton,
    NavbarVue
  },

  methods: {
    // Get Session ID
    getCookie(cname) {
      let name = cname + "=";
      let decodedCookie = decodeURIComponent(document.cookie);
      let ca = decodedCookie.split(';');
      for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
    },
    // Get Todo Data
    async getTodoData() {
      return await fetch(this.req_url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          s_id: this.s_id
        })
      })
      .then(data => data.json())
      .then((res) => { return res })
    },
    // Add Todo
    async addTodo() {
      if (this.add_title.length !== 0 || this.add_content.length !== 0) {
        await fetch(this.req_url, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            s_id: this.s_id,
            title: this.add_title,
            content: this.add_content
          })
        })
          .then(async (data) => {
            if (data.status === 200) {
              this.$swal({
                title: 'Add Todo Successfully',
                icon: 'success'
              })
              this.add_title = ''
              this.add_content = ''
              this.todos = await this.getTodoData()
            } else {
              this.$swal({
                title: 'Add Todo Error',
                icon: 'error'
              })
            }
          })
      } else {
        this.$swal({
          title: '標題與內容不可為空白！',
          icon: 'warning'
        })
      }
    },
    // Delete Todo
    async deleteTodo(todo_id) {
      console.log(todo_id)
      this.$swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then(async (result) => {
        if (result.isConfirmed) {
          await fetch(this.req_url, {
            method: 'DELETE',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              s_id: this.s_id,
              todo_id: todo_id
            })
          })
            .then(async (data) => {
              if (data.status === 200) {
                this.$swal(
                  'Deleted!',
                  'Your todo has been deleted.',
                  'success'
                )
                this.todos = await this.getTodoData()
              } else {
                this.$swal({
                  title: 'Delete Todo Error',
                  icon: 'error'
                })
              }
            })
        }
      })
    },
  },

  async mounted() {
    this.s_id = this.getCookie('s_id')
    this.todos = await this.getTodoData()
    if (this.getCookie('s_id') == '') {
      this.$swal({
        title: '登入時間以超時，請重新登入',
        icon: 'warning'
      }).then(() => {
        window.location.href = '/'
      })
    }
  },
}
</script>