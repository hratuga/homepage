<template>
  <banner-image
      v-if="bannerParams"
      :image-path="bannerParams?.imagePath"
      :alt-image-text="bannerParams?.altImageText"
      :headline="bannerParams?.headline"
  />
  <router-view />
</template>

<script>
import BannerImage from "@/components/banner/BannerImage.vue";
export default {
  name: "PageContent",
  components: {BannerImage},
  computed: {
    bannerParams() {
      const bannerOptions = {
        'Home': {
          imagePath: 'src/assets/banner/Dolomieten.jpg',
          altImageText: 'Berge von Dolomieten',
          headline: 'Stamm Hratuga',
        }
      }
      const { name } = this.$route
      return bannerOptions[name]
    }
  }
}
</script>
