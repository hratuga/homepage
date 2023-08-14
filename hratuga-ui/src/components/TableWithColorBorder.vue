<script setup>
import {useDisplay} from "vuetify";
import {computed} from "vue";

const {mobile} = useDisplay();

defineEmits(['rowClick'])

const props = defineProps({
  color: {
    type: String,
    default: 'red',
  },
  hover: {
    type: Boolean,
    default: true,
  },
  header: {
    type: Array,
    required: true,
  },
  items: {
    type: Array,
    required: true,
  },
  noMobileHeader: {
    type: Array,
    default() { return [] },
  },
  headline: {
    type: String,
    default: null,
  },
});

const headerWithPadding = computed(() => {
  const headT = [];
  props.header.forEach((item) => {
    headT.push(item);
    headT.push(...Array((item.colspan - 1) || 0).fill({ title: null }));
  });
  return headT;
});

const borderTop = computed(() => {
  return `border-top: medium solid ${props.color} !important;`;
});

const colSpanMax = computed(() => {
  return props.header.reduce((colSum, { colspan=1 }) => colSum + colspan, 0);
});
</script>

<template>
  <v-table
    v-if="!mobile"
    :hover="props.hover"
  >
    <thead>
      <tr
        v-if="props.headline"
        :style="borderTop"
      >
        <th :colspan="colSpanMax">
          {{ props.headline }}
        </th>
      </tr>
      <tr :style="!props.headline ? borderTop : ''">
        <th
          v-for="({ title, colspan = 1 }, headIdx) in props.header"
          :key="'head' + title + headIdx"
          :colspan="colspan"
        >
          {{ title }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(row, rowIdx) in props.items"
        :key="'row-' + rowIdx"
        @click="$emit('rowClick', row.id)"
      >
        <td
          v-for="(col, colIdx) in row.data"
          :key="'col-' + colIdx"
        >
          {{ col }}
        </td>
      </tr>
    </tbody>
  </v-table>
  <v-list
    v-else
    :style="borderTop"
    class="mb-10"
    width="100%"
    border
    variant="plain"
  >
    <v-list-subheader
      v-if="props.headline"
      class="text-center justify-center"
    >
      <span class="text-h6">
        {{ props.headline }}
      </span>
    </v-list-subheader>
    <v-divider />
    <div
      v-for="(row, rowIdx) in props.items"
      :key="'row-' + rowIdx"
    >
      <v-list-item @click="$emit('rowClick', row.id)">
        <v-card>
          <p
            v-for="({ title }, colIdx) in headerWithPadding"
            :key="'col-' + colIdx"
            :class="{ 'font-weight-bold': colIdx === 0 }"
          >
            <span
              v-if="title !== null && !props.noMobileHeader.includes(colIdx)"
            >
              {{ title + ':' }}
            </span>
            <span>{{ ' ' }}</span>
            <span>
              {{ row.data[colIdx] }}
            </span>
          </p>
        </v-card>
      </v-list-item>
      <v-divider v-if="rowIdx < props.items.length - 1" />
    </div>
  </v-list>
</template>

<style scoped lang="scss">
$table-border-color: #E5E7EB;

div.v-row:not(:last-of-type) {
  margin-bottom: 25px !important;
}

div.v-table {
  width: 75% !important;
  margin-bottom: 50px !important;

  table {
    thead {
      tr {
        th {
          font-weight: bold;
          text-align: center;
          border: thin solid $table-border-color;
          border-top: inherit;
          color: black;
          background-color: rgb(249, 250, 251);
        }
      }
    }

    tbody tr td {
      border: thin solid $table-border-color;
    }
  }
}
</style>
