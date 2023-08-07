<script setup>
import { useRoute } from "vue-router";

const route = useRoute();
const { group } = route.params;
</script>

<template>
  <v-container class="mt-5">
    <v-row
      justify="center"
      class="mb-5"
    >
      <div class="text-h3">
        Turmfalken {{ group }}
      </div>
    </v-row>
    <v-row
      justify="center"
      class="mb-5"
    >
      <v-img
        src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&w=1310&h=873&q=80&facepad=3"
        max-width="50%"
      />
    </v-row>
    <v-row
      justify="center"
      class="mb-5"
    >
      Wir freuen uns über neue Mitglieder! Komm doch gerne vorbei!
    </v-row>
    <v-row
      justify="center"
      class="mb-5"
    >
      <v-table>
        <thead>
          <tr>
            <th>
              Gruppeführung
            </th>
            <th>
              Gruppenstunde
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              Patrik
            </td>
            <td>
              Montag oder so
            </td>
          </tr>
        </tbody>
      </v-table>
    </v-row>
  </v-container>
</template>

<style scoped>
thead {
  background-color: rgb(37, 99, 235);
}
tbody {
  background-color: dodgerblue;
}
</style>
