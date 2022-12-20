<template>
  <div class=" absolute top-0 w-full bg-slate-700 text-gray-100 py-3.5 px-6 shadow md:flex justify-between items-center">

    <div class="flex items-center cursor-pointer">

      <span class="text-white text-xl mr-1">
        <font-awesome-icon icon="fa-solid fa-wind" />
      </span>

      <h1 class="text-xl">Designer</h1>

    </div>

    <span @click="MenuToggle()" class="absolute text-2xl top-3 right-5 md:hidden">
      <font-awesome-icon v-if="open" icon="fa-solid fa-xmark" />
      <font-awesome-icon v-else icon="fa-solid fa-bars" />
    </span>

    <ul
      class="md:flex md:items-center md:px-0 px-3 md:pb-0 md:static absolute md:bg-navyBlue bg-slate-700 md:w-auto m-full top-14 w-full h-auto duration-500 ease-in"
      :class="[open ? 'left-0' : 'left-[-100%]']">
      <router-link @click="MenuClose()" v-for="link in Links" :key="link" :to="link.link">
        <li class="md:mx-4 md:my-0 my-6 hover:text-silver cursor-pointer">
          <a class="text-xl">{{ link.name }}</a>
        </li>
      </router-link>
    </ul>

  </div>
</template>

<script>

export default {

  data() {
    return {
      open: false,
      Links: [
        { name: 'Home', link: '/home' },
        { name: 'LogOut', link: '/logout' },
      ],
    }
  },

  methods: {
    MenuToggle() {
      this.open = !this.open;
    },
    MenuClose() {
      this.open = false;
    },
  }

}
</script>