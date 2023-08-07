<template>
  <v-container class="w-75">
    <v-row
      class="text-md-h4 text-h5 mt-9"
      justify="center"
    >
      Klicke auf eine Gruppe für mehr Details
    </v-row>
    <v-row
      class="text-md-h6 text-medium-emphasis"
      justify="center"
    >
      (Alle E-Mail-Adressen enden auf
      <br v-if="xs">
      [ at ] hratuga.de)
    </v-row>
    <v-row
      justify="center"
      class="text-center"
    >
      <v-table
        v-for="({ color, groups }, idx) in tables"
        v-if="!mobile"
        :key="color + idx"
        hover
      >
        <thead>
          <tr :class="'border-t-' + color">
            <th>Gruppenname</th>
            <th v-if="color !== 'stafue'">
              Gruppenstunde
            </th>
            <th v-if="color !== 'stafue'">
              Jahrgänge
            </th>
            <th>Kontakt E-Mail</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="{ name, techName, ageRange, meeting } in groups"
            :key="techName"
            @click="router.push({ name: 'groupDetails', params: { group: techName } })"
          >
            <td>{{ name }}</td>
            <td v-if="meeting?.time?.length === 2">
              {{ meeting?.weekday }}, {{ meeting.time[0] }} Uhr bis {{ meeting.time[1] }} Uhr
            </td>
            <td v-else-if="color !== 'stafue'">
              Nach Absprache
            </td>
            <td v-if="ageRange?.length === 2">
              Jahrgänge: {{ ageRange[0] }} bis {{ ageRange[1] }}
            </td>
            <td v-else-if="color !== 'stafue'">
              --
            </td>
            <td><span v-if="color !== 'stafue'">kontakt-</span>{{ techName }}</td>
          </tr>
        </tbody>
      </v-table>
      <v-list
        v-for="({ color, groups, prefix }, idx) in tables"
        v-else
        :key="color + idx"
        :class="'border-t-' + color"
        class="mb-10"
        width="100%"
        border
        variant="plain"
      >
        <div
          v-for="({ name, techName, ageRange, meeting }, idx) in groups"
          :key="techName"
        >
          <v-list-item
            :to="{ name: 'groupDetails', params: { group: techName } }"
          >
            <v-card>
              <p class="font-weight-bold">
                <span v-if="prefix">
                  {{ prefix + ' ' }}
                </span>
                {{ name }}
              </p>
              <p v-if="meeting?.time?.length === 2">
                Gruppenstunde: {{ meeting?.weekday }}, {{ meeting.time[0] }} Uhr bis {{ meeting.time[1] }} Uhr
              </p>
              <p v-else-if="color !== 'stafue'">
                Gruppenstunde nach Absprache
              </p>
              <p v-if="ageRange?.length === 2">
                Jahrgänge: {{ ageRange[0] }} bis {{ ageRange[1] }}
              </p>
              <p>
                E-Mail:
                <span v-if="color !== 'stafue'">kontakt-</span>{{ techName }}
              </p>
            </v-card>
          </v-list-item>
          <v-divider v-if="idx < groups.length - 1" />
        </div>
      </v-list>
    </v-row>
    <p class="text-md-h6 text-center">
      Solltet ihr nicht wissen, welche Gruppe passend für euch ist oder ihr allgemeine Fragen haben,
      könnt ihr euch an kontakt [ at ] hratuga.de wenden.
    </p>
  </v-container>
</template>

<script setup>
import {useRouter} from "vue-router";
import {useDisplay} from "vuetify";

const {mobile, xs} = useDisplay();

const router = useRouter();
const tables = [
  {
    color: 'stafue',
    prefix: null,
    groups: [
      {
        name: 'Stammesführung',
        techName: 'stammesfuehrung',
        ageRange: null,
        meeting: null,
      },
    ],
  },
  {
    color: 'woelfling',
    prefix: 'Meute',
    groups: [
      {
        name: 'Seeadler',
        techName: 'seeadler',
        ageRange: [2012, 2016],
        meeting: {
          weekday: 'Montag',
          time: ['17:30', '19:00'],
        },
      },
    ],
  },
  {
    color: 'scout',
    prefix: 'Sippe',
    groups: [
      {
        name: 'Goldene Pumas',
        techName: 'goldene-pumas',
        ageRange: [2010, 2012],
        meeting: {
          weekday: 'Donnerstag',
          time: ['17:30', '19:00'],
        },
      },
      {
        name: 'Katzenbären',
        techName: 'katzenbaeren',
        ageRange: [2008, 2009],
        meeting: {
          weekday: 'Dienstag',
          time: ['17:30', '19:00'],
        },
      },
      {
        name: 'Skorpione',
        techName: 'skorpione',
        ageRange: [2007, 2009],
        meeting: {
          weekday: 'Mittwoch',
          time: ['17:30', '19:00'],
        },
      },
    ],
  },
  {
    color: 'rover',
    prefix: 'Roverrunde',
    groups: [
      {
        name: 'Turmfalken',
        techName: 'turmfalken',
        ageRange: [2004, 2005],
        meeting: {
          weekday: 'Montag',
          time: ['18:30', '22:00'],
        },
      },
      {
        name: 'Geparden',
        techName: 'geparden',
        ageRange: [2001, 2003],
        meeting: null,
      },
    ],
  },
]
</script>

<style scoped lang="scss">
@use "node_modules/vuetify/lib/components/VTable/_variables.scss" as vuetify;

$table-border-color: #E5E7EB;

.border-t-woelfling {
  border-top: medium solid orange !important;
}

.border-t-scout {
  border-top: medium solid blue !important;
}

.border-t-rover {
  border-top: medium solid red !important;
}

.border-t-stafue {
  border-top: medium solid green !important;
}

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
        }
      }
    }

    tbody tr td {
      border: thin solid $table-border-color;
    }
  }
}
</style>
