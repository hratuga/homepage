<template>
  <footer class="bg-gray-900" aria-labelledby="footer-heading">
    <h2 id="footer-heading" class="sr-only">Footer</h2>
    <div class="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
      <div class="xl:grid xl:grid-cols-5 xl:gap-8">
        <div class="grid grid-cols-1 gap-8 xl:col-span-5">
          <div class="md:grid md:grid-cols-3 md:gap-8">
            <div>
              <h3 class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Weiterführende Links </h3>
              <ul role="list" class="mt-4 space-y-4">
                <li v-for="item in navigation.links" :key="item.name">
                  <a :href="item.href" class="text-base text-gray-500 hover:text-white">
                    {{ item.name }}
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <div class="flex flex-wrap justify-center text-center">
                <img
                    src="@/assets/logo.png"
                    class="p-1 max-w-sm h-48"
                    alt="Hratuga Stammeslogo"
                />
              </div>
            </div>
            <div class="mx-auto">
              <h3 class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Über uns</h3>
              <ul role="list" class="mt-4 space-y-4">
                <li v-for="item in navigation.aboutUs" :key="item.name">
                  <a :href="item.href" class="text-base text-gray-500 hover:text-white">
                    {{ item.name }}
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
          <div class="mt-5 border-t border-gray-200">
            <p class="mt-2 text-base text-gray-400 xl:text-center">&copy; {{ new Date().getFullYear() }} Stamm Hratuga</p>
          </div>
    </div>
<!--    <div class="max-w-7xl w-3/4 mx-auto py-6 px-4 sm:px-6 lg:py-8 lg:px-8">-->
<!--      <div class="grid-cols-3">-->
<!--          <div class="md:grid col-start-1 col-span-1">-->
<!--            <h3 class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Weiterführende Links </h3>-->
<!--            <ul role="list" class="mt-4 space-y-4">-->
<!--              <li v-for="item in navigation.links" :key="item.name">-->
<!--                <a :href="item.href" class="text-base text-gray-500 hover:text-white">-->
<!--                  {{ item.name }}-->
<!--                </a>-->
<!--              </li>-->
<!--            </ul>-->
<!--          </div>-->
<!--          <div class="col-start-2 col-span-1">-->
<!--            <div class="flex flex-wrap justify-center">-->
<!--              <img-->
<!--                  src="@/assets/logo.png"-->
<!--                  class="p-1 max-w-sm h-48"-->
<!--                  alt="Hratuga Stammeslogo"-->
<!--              />-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="col-start-3 col-span-1">-->
<!--            <h3 class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Über uns</h3>-->
<!--            <ul role="list" class="mt-4 space-y-4">-->
<!--              <li v-for="item in navigation.aboutUs" :key="item.name">-->
<!--                <a :href="item.href" class="text-base text-gray-500 hover:text-white">-->
<!--                  {{ item.name }}-->
<!--                </a>-->
<!--              </li>-->
<!--            </ul>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div class="mt-12 border-t border-gray-200 pt-8">-->
<!--      <p class="text-base text-gray-400 xl:text-center">&copy; {{ new Date().getFullYear() }} Stamm Hratuga</p>-->
<!--    </div>-->
<!--    </div>-->
  </footer>
</template>

<script>
const navigation = {
  links: [
    {name: 'Pfadfinderstamm in Ratingen Mitte', href: 'https://stamm-dumeklemmer.de/'},
    {name: 'Ring Rhein Lippe', href: 'https://ring-rhein-lippe.de/'},
    {name: 'Deutscher Pfadfinderbund Mosaik', href: 'https://dpbm.de/'},
    {name: 'Heimabend-Inspirator', href: 'https://www.inspirator.dpbm.de/'},
  ],
  aboutUs: [
    {name: 'Kontakt', href: '/gruppen'},
    {name: 'Impressum', href: '/impressum'},
    {name: 'Datenschutzerklärung', href: '/datenschutz'},
    {name: 'Github-Projekt', href: 'https://github.com/hratuga/homepage'},
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
