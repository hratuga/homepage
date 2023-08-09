<script setup>
const props = defineProps({
  content: {
    type: Array,
    default() {
      return [];
    },
  },
});
</script>

<template>
  <v-row
    v-for="({ title, text, img}, idx) in props.content"
    :key="idx + title"
    class="d-flex align-center justify-center mb-lg-5"
    :class="{ 'mb-10': idx !== props.content.length - 1 }"
  >
    <v-col
      cols="12"
      lg="6"
      order="1"
      :order-lg="2 - idx % 2"
    >
      <v-img
        :src="img"
        max-width="100%"
        class="rounded-lg elevation-6"
        cover
      />
    </v-col>
    <v-col
      cols="12"
      lg="6"
      order="2"
      :order-lg="1 + idx % 2"
    >
      <div class="text-h5 font-weight-black">
        {{ title }}
      </div>
      <p
        v-for="textContent in text"
        :key="textContent"
        class="mb-3"
      >
        {{ textContent }}
      </p>
      <slot
        v-if="idx === props.content.length - 1"
        name="appendToLast"
      />
    </v-col>
  </v-row>
</template>

<style scoped>

</style>
