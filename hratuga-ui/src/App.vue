<template>
  <navigation />
  <router-view />
  <footer-bar />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import Navigation from "@/components/navigation/Navigation.vue";
import FooterBar from "@/components/footer/FooterBar.vue"
</script>
