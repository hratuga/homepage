<template>
  <footer class="bg-black">
    <div class="max-w-7xl mx-auto py-12 px-4 overflow-hidden sm:px-6 lg:px-8">
      <nav class="-mx-5 -my-2 flex flex-wrap justify-center" aria-label="Footer">
        <div v-for="item in navigation.links" :key="item.name" class="px-5 py-2">
          <a :href="item.href" class="text-base text-gray-500 hover:text-gray-900">
            {{ item.name }}
          </a>
        </div>
      </nav>
<!--      <div class="mt-8 flex justify-center space-x-6">-->
<!--        <a v-for="item in navigation.links" :key="item.name" :href="item.href" class="text-gray-400 hover:text-gray-500">-->
<!--          <span class="sr-only">{{ item.name }}</span>-->
<!--          <component :is="item.icon" class="h-6 w-6" aria-hidden="true" />-->
<!--        </a>-->
<!--      </div>-->
      <p class="mt-8 text-center text-base text-gray-400">&copy; 2021 Stamm Hratuga</p>
    </div>
  </footer>
</template>

<script>
const navigation = {
  links: [
    {name: 'Pfadfinderstamm in Ratingen Mitte', href: '#'},
    {name: 'Ring Rhein Lippe', href: '#'},
    {name: 'Deutscher Pfadfinderbund Mosaik', href: '#'},
  ],
  aboutUs: [
    {name: 'Kontakt', href: '#'},
    {name: 'Impressum', href: '#'},
    {name: 'Datenschutzerklärung', href: '#'},
    {name: 'Github-Projekt', href: '#'},
  ],
};

export default {
  name: "FooterBar",
  setup() {
    return {
      navigation,
    }
  },
}
</script>

<style scoped>

</style>
