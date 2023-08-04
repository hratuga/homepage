<template>
  <v-navigation-drawer
    v-model="drawer"
    color="black"
  >
    <v-list
      density="compact"
      nav
    >
      <v-list-item
        v-for="(title, name) in sidebarNavItems"
        :key="name"
        :to="{ name }"
      >
        {{ title }}
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-app-bar color="black">
    <v-app-bar-nav-icon @click="drawer = !drawer" />

    <v-toolbar-title>Pfadfinderstamm Hratuga</v-toolbar-title>
  </v-app-bar>
</template>

<script setup>
import { ref } from 'vue';

const drawer = ref(false);
const sidebarNavItems = {
  home: 'Unser Stamm',
  scouts: 'Pfadfinder?',
  groups: 'Gruppen',
  dates: 'Termine',
  gallery: 'Fotos',
  download: 'Downloads',
  foerderverein: 'Förderverein',
};
</script>
