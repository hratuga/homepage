<script setup>
// eslint-disable-next-line vue/no-setup-props-destructure
const { name, role, mail, img } = defineProps({
  name: String,
  role: String,
  mail: String,
  img: String,
})
</script>

<template>
  <v-card
    height="100%"
    width="100%"
  >
    <div class="d-flex flex-no-wrap justify-space-between">
      <div>
        <v-card-title class="text-h5">
          {{ name }}
        </v-card-title>
        <v-card-subtitle>
          {{ role }}
        </v-card-subtitle>
        <v-card-text>
          <v-icon
            class="me-2"
            icon="mdi-email"
          />
          <span class="text-medium-emphasis">
            {{ mail }}
          </span>
        </v-card-text>
      </div>
      <v-avatar
        v-if="img"
        class="me-3 mb-3 mt-auto"
        size="80"
      >
        <v-img :src="img" />
      </v-avatar>
    </div>
  </v-card>
</template>

<style scoped>

</style>
