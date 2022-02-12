<template>
  <header class="bg-gray-900">
    <nav class="mx-auto px-4 sm:px-6 lg:px-8" aria-label="Top">
      <div class="w-full py-6 flex items-center justify-between border-b border-cyan-500 lg:border-none">
        <div class="flex items-center">
          <div class="hidden ml-10 lg:block">
            <router-link v-for="link in navigation" :key="link.name"
                         :to="link.to"
                         class="text-base font-medium text-white hover:bg-black p-4 border-2 border-transparent"
                         active-class="border-b-red-600 border-t-transparent border-x-transparent bg-black">
              {{ link.name }}
            </router-link>
          </div>
        </div>
        <div class="ml-10 space-x-4">
          <a href="#" class="inline-block bg-indigo-500 py-2 px-4 border border-transparent rounded-md text-base font-medium text-white hover:bg-opacity-75">Sign in</a>
          <a href="#" class="inline-block bg-white py-2 px-4 border border-transparent rounded-md text-base font-medium text-indigo-600 hover:bg-indigo-50">Sign up</a>
        </div>
      </div>
      <div class="py-4 flex flex-wrap justify-center space-x-6 lg:hidden">
        <router-link v-for="link in navigation" :key="link.name" :to="link.to" class="text-base font-medium text-white hover:text-indigo-50">
          {{ link.name }}
        </router-link>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Navigation",
  setup() {
    return {
      navigation: [
        {name: 'Home', to: '/'},
        {name: 'Pfadfinder?', to: '/was-ist-pfadfinder'},
        {name: 'Unsere Gruppen', to: '/gruppen'}
      ],
    }
  },
}
</script>

<style scoped>

</style>
