<template>
  <v-main>
    <AppBanner />
    <router-view />
  </v-main>
</template>
<script setup>
import AppBanner from "@/components/app/AppBanner.vue";
</script>
