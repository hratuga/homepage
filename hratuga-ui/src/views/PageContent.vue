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
  data: () => ({
    defaultBannerOptions: {
      imagePath: 'src/assets/banner/Dolomiten.jpg',
      altImageText: 'Berge von Dolomiten',
      headline: '',
    },
  }),
  computed: {
    bannerParams() {
      const bannerOptions = {
        'Home': {
          imagePath: 'src/assets/banner/Dolomiten.jpg',
          altImageText: 'Berge von Dolomiten',
          headline: 'Stamm Hratuga',
        }
      }
      const { name } = this.$route
      return bannerOptions[name] || this.defaultBannerOptions
    }
  }
}
</script>
