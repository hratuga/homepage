<template>
  <v-navigation-drawer
    v-model="drawer"
    :color="barColor"
    class="text-white"
  >
    <v-list
      density="compact"
      nav
    >
      <v-list-item
        v-for="(title, name) in sidebarNavItems"
        :key="name"
        :to="{ name }"
        density="compact"
      >
        {{ title }}
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-app-bar
    density="compact"
    class="text-white"
    :color="barColor"
  >
    <v-app-bar-nav-icon @click="drawer = !drawer" />

    <v-app-bar-title>Pfadfinderstamm Hratuga</v-app-bar-title>
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
  downloads: 'Downloads',
  foerderverein: 'Förderverein',
};
const barColor = '#111827';
</script>
