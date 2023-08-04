<template>
  <v-app id="hratuga-homepage">
    <AppBarNavigation />
    <AppMain />
    <AppFooter />
  </v-app>
</template>

<script setup>
import AppFooter from "@/components/app/AppFooter.vue";
import AppBarNavigation from "@/components/app/AppBarNavigation.vue";
import AppMain from "@/components/app/AppMain.vue";
</script>
