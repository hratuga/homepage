<template>
  <navigation />
  <page-content />
  <footer-bar />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import Navigation from "@/components/navigation/Navigation.vue";
import FooterBar from "@/components/footer/FooterBar.vue"
import PageContent from "@/views/PageContent.vue";
</script>
