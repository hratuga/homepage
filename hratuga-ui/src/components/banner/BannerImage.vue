<template>
  <div class="relative h-96 overflow-hidden">
    <div class="absolute z-30 flex w-full h-full">
      <div class="relative z-30 px-6 py-8 text-white md:py-10 w-full m-auto">
        <h1 class="text-5xl font-semibold lg:font-bold w-full h-full text-center align-middle inline-block tracking-wide">
          {{ headline || '' }}
        </h1>
      </div>
    </div>
    <div class="absolute top-0 right-0 block w-full h-full">
      <img class="object-cover min-w-full h-full"
           :src="imagePath"
           :alt="altImageText"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "BannerImage",
  props: {
    imagePath: String,
    headline: String,
    altImageText: String,
  }
}
</script>
