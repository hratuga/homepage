<script setup>
import TextWithImage from "@/components/TextWithImage.vue";

const content = [
  {
    title: 'Förderverein in Ratingen seit 1997',
    text: [
        'Der Förderverein des Pfadfinderhorstes Angerländer e.V. hat das Ziel, die Pfadfinderarbeit in Ratingen nachhaltig zu unterstützen.',
        'Er hat vordringlich den Zweck, die Arbeit der im Horst Angerländer zusammengeschlossenen Pfadfinderstämme des Deutschen Pfadfinderbundes Mosaik ideell und materiell zu unterstützen.',
        'Daneben soll das Verständnis für die Pfadfinderarbeit in der Öffentlichkeit geweckt und verstärkt werden.',
    ],
    img: 'https://hratuga.de/static/img/2018-09-Horstlager-41.9c0682d.jpg',
  },
  {
    title: 'Dies soll insbesonders durch folgende Maßnahmen geschehen',
    text: [
        'a) durch Errichtung, Unterhaltung und zur Verfügungstellung geeigneter Pfadfinderheime;',
        'b) durch Beratung und Hilfe der Stämme bei der Jugendarbeit, der Durchführung eventueller Fahrten sowie bei der Verwaltung und Finanzierung größerer Vorhaben;',
        'c) durch Werbung und Aufklärung über die Pfadfinderarbeit in der Öffentlichkeit',
    ],
    img: 'https://hratuga.de/static/img/2018-09-Horstlager-6.ac0807c.jpg',
  },
]
</script>

<template>
  <v-container>
    <TextWithImage :content="content" />

    <v-row justify="center">
      <v-col
        lg="2"
        sm="3"
      >
        <v-img
          src="@/assets/logos/hratuga.png"
        />
      </v-col>
      <v-col
        lg="2"
        sm="3"
      >
        <v-img
          src="@/assets/logos/angerlaender.png"
        />
      </v-col>
      <v-col
        lg="2"
        sm="3"
      >
        <v-img
          id="asd"
          src="@/assets/logos/dumeklemmer.png"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
