<template>
  <v-footer color="black">
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="{ title, name } in footerNavItems"
        :key="title"
        :to="name.startsWith('//') ? name : { name }"
        :target="name.startsWith('//') ? '_blank' : null"
        color="white"
        variant="text"
        class="mx-2"
        rounded="xl"
      >
        {{ title }}
      </v-btn>
      <v-col
        class="text-center"
        cols="12"
      >
        &copy; {{ new Date().getFullYear() }} — <strong>Stamm Hratuga</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script setup>
const footerNavItems = [
  {
    title: 'Wikituga',
    name: '//wiki.hratuga.de',
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
</script>
