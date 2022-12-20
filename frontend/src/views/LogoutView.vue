<template>
  <div class="w-full h-screen bg-gray-900 flex justify-center">
  </div>
</template>

<script>
export default {
  mounted() {
    document.cookie = "s_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;"
    window.location.href = '/'
  }
}
</script>