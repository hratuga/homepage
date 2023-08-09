<script setup>
import {computed, ref} from "vue";
import Allgemein from "@/components/foerderverein/Allgemein.vue";
import { useDisplay } from "vuetify";
import Vorstand from "@/components/foerderverein/Vorstand.vue";
import MitgliedWerden from "@/components/foerderverein/MitgliedWerden.vue";
import Dokumente from "@/components/foerderverein/Dokumente.vue";
import Impressum from "@/components/foerderverein/Impressum.vue";

const tab = ref(1);
const { mdAndUp } = useDisplay();

function scrollDown(v) {
  if (mdAndUp) {
    document.getElementById('SubHead' + v).scrollIntoView({behavior: 'smooth', block: 'center'});
  }
}
</script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col>
        <v-tabs
          v-model="tab"
          density="compact"
          selected-class="text-black"
          bg-color="grey"
          :grow="mdAndUp"
          :direction="!mdAndUp ? 'vertical' : 'horizontal'"
          @update:model-value="v => scrollDown(v)"
        >
          <v-tab :value="1">
            Allgemeines
          </v-tab>
          <v-tab :value="2">
            Vorstand
          </v-tab>
          <v-tab :value="3">
            Mitglied werden
          </v-tab>
          <v-tab :value="4">
            Dokumente
          </v-tab>
          <v-tab :value="5">
            Impressum
          </v-tab>
        </v-tabs>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-if="mdAndUp">
        <v-window v-model="tab">
          <v-window-item :value="1">
            <Allgemein />
          </v-window-item>
          <v-window-item :value="2">
            <Vorstand />
          </v-window-item>
          <v-window-item :value="3">
            <MitgliedWerden />
          </v-window-item>
          <v-window-item :value="4">
            <Dokumente />
          </v-window-item>
          <v-window-item :value="5">
            <Impressum />
          </v-window-item>
        </v-window>
      </v-col>
      <v-col v-else>
        <div
          id="SubHead1"
          class="text-h4 mt-4"
        >
          Informationen
        </div>
        <Allgemein />
        <div
          id="SubHead2"
          class="text-h4 mt-4"
        >
          Vorstand
        </div>
        <Vorstand />
        <div
          id="SubHead3"
          class="text-h4 mt-4"
        >
          Mitglied Werden
        </div>
        <MitgliedWerden />
        <div
          id="SubHead4"
          class="text-h4 mt-4"
        >
          Dokumente
        </div>
        <Dokumente />
        <div
          id="SubHead5"
          class="text-h4 mt-4"
        >
          Impressum
        </div>
        <Impressum />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
