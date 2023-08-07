<template>
  <v-footer :color="barColor">
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="{ title, name } in footerNavItems"
        :key="title"
        :to="name.startsWith('//') ? name : { name }"
        :target="name.startsWith('//') ? '_blank' : null"
        color="#6B7280"
        variant="plain"
        rounded="xl"
      >
        {{ title }}
      </v-btn>
      <v-col
        class="text-center text-grey-lighten-1"
        cols="12"
      >
        &copy; {{ new Date().getFullYear() }} Stamm Hratuga
      </v-col>
    </v-row>
  </v-footer>
</template>

<script setup>
const footerNavItems = [
  {
    title: 'Heimabend-Inspirator',
    name: '//inspirator.dpbm.de',
  },
  {
    title: 'Partnerstamm in Ratingen Mitte',
    name: '//stamm-dumeklemmer.de',
  },
  {
    title: 'Ring Rhein Lippe',
    name: '//ring-rhein-lippe.de',
  },
  {
    title: 'Deutscher Pfadfinder*innenbund Mosaik',
    name: '//dpbm.de',
  },
  {
    title: 'Impressum',
    name: 'gallery',
  },
  {
    title: 'Datenschutzerklärung',
    name: 'privacy',
  },
];

const barColor = '#111827';
</script>
