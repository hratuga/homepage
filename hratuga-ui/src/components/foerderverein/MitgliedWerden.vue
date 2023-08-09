<script setup>
import TextWithImage from "@/components/TextWithImage.vue";
const content = [
  {
    title: 'Wie kann ich die Pfadfinderarbeit unterstützen?',
    text: [
      'Eine Unterstützung der Pfadfinderarbeit ist finanziell auch durch eine Einzelspende ohne eine (feste) Mitgliedschaft möglich.',
      'Daneben ist es natürlich auch gerne gesehen, wenn Sie zu uns kommen und dauerhaft Mitglied im Förderverein werden.',
      'Die Mitglieder zahlen einen jährlichen Mitgliedsbeitrag, der als Mindestbeitrag nur Euro 12,- beträgt. Jede “Aufrundung” des Mindestbetrages ist gerne gesehen und hilft uns bei der Unterstützung der Pfadfinderarbeit in Ratingen.',
      'Als gemeinnütziger Verein ist der Förderverein berechtigt, Spendenbescheinigungen (auch über den Mitgliedsbeitrag) auszustellen.',
      'Die Mitglieder sowie alle Spender erhalten zum Jahresende unaufgefordert eine Spendenbescheinigung zum Einreichen beim Finanzamt.',
      'Gerne senden wir Ihnen weitere Informationen über den Förderverein oder die Pfadfinder in Ratingen zu.',
      'Diese Information ist auch auf der Seite Download zu bekommen.',
    ],
    img: 'https://hratuga.de/static/img/spende.d8ba888.jpg',
  },
];
</script>

<template>
  <v-container>
    <TextWithImage :content="content" />
  </v-container>
</template>

<style scoped>

</style>
