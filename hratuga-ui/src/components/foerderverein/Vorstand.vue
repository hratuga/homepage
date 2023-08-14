<script setup>
import PersonContactCard from "@/components/PersonContactCard.vue";

const people = [
  {
    name: 'Jan Langguth',
    role: 'Vorsitzender',
    mail: 'jan@stamm-dumeklemmer.de',
  },
  {
    name: 'Lea Heinze',
    role: 'Stellv. Vorsitzende',
    mail: 'lea@stamm-dumeklemmer.de',
  },
  {
    name: 'Nadine Beringer',
    role: 'Kassenwärtin',
    mail: 'nadine@stamm-dumeklemmer.de',
  },
  {
    name: 'Stefan Stechemesser',
    role: 'Schriftführer',
    mail: 'stefan@stamm-dumeklemmer.de',
  },
]
</script>

<template>
  <v-container>
    <v-row>
      <v-col
        v-for="person in people"
        :key="person.mail"
        lg="3"
        md="6"
        sm="6"
        xs="12"
      >
        <PersonContactCard v-bind="person" />
      </v-col>
    </v-row>
    <v-row>
      <v-col class="text-h6 text-center">
        Desweiteren sind die Stammesführer der beiden Ratinger Stämme im erweiterten Vorstand.
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
