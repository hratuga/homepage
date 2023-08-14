<script setup>
import TableWithColorBorder from '@/components/TableWithColorBorder.vue';

const dates = [
  {
    head: [{
      title: 'Name',
      colspan: 1,
    }, {
      title: 'Datum'
    }],
    body: [
      {
        id: '4',
        data: ['Fahrt 1', 'Datum 1'],
      },
      {
        id: '5',
        data: ['Fahrt 2', 'Datum 2'],
      },
      {
        id: '6',
        data: ['whatever', 'nix'],
      },
    ],
    headline: 'Januar',
    color: 'magenta',
  },
  {
    head: [{
      title: 'Name',
    }, {
      title: 'Datum'
    }],
    body: [
      {
        id: '1',
        data: ['adsf', 'dsfgadsgads'],
      },
      {
        id: '2',
        data: ['3afa3f3', '3aaffa'],
      },
      {
        id: '3',
        data: ['whateveeer', 'nix22'],
      },
    ],
    headline: 'Februar',
    color: 'green',
  },
]
</script>

<template>
  <v-container>
    <v-row
      v-for="data in dates"
      :key="data.head.title"
      justify="center"
      class="text-center"
    >
      <v-col>
        <TableWithColorBorder
          :color="data.color"
          :items="data.body"
          :header="data.head"
          :no-mobile-header="[0,1]"
          :headline="data.headline"
          @row-click="(row) => console.log(row)"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
