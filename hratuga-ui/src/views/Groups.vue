<template>
  <v-container class="w-75">
    <v-row
      class="text-md-h4 text-h5"
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
      <TableWithColorBorder
        v-for="({ head, body, headline, color }, idx) in data"
        :key="color + idx"
        :items="body"
        :color="color"
        :header="head"
        :headline="headline"
        :no-mobile-header="[0]"
        @row-click="handleRowClick"
      />
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
import TableWithColorBorder from "@/components/TableWithColorBorder.vue";

const {xs} = useDisplay();

const router = useRouter();

const headDefault = [{
  title: 'Gruppenname'
}, {
  title: 'Gruppenstunde'
}, {
  title: 'Jahrgänge',
}, {
  title: 'E-Mail',
}];

const groupsWoelflinge = [
  {
    name: 'Seeadler',
    techName: 'seeadler',
    ageRange: [2012, 2016],
    meeting: {
      weekday: 'Montag',
      time: ['17:00', '18:30'],
    },
  },
];

const groupsStammesfuerhung = [
  {
    name: 'Stammesführung',
    techName: 'stammesfuehrung',
    ageRange: null,
    meeting: null,
  },
];

const groupsScout = [
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
];

const groupsRover = [
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
];

const data = [
  {
    head: [headDefault[0], headDefault[3]],
    body: transformBody(groupsStammesfuerhung),
    headline: null,
    color: 'green',
  },
  {
    head: headDefault,
    body: transformBody(groupsWoelflinge),
    headline: 'Meuten',
    color: 'orange',
  },
  {
    head: headDefault,
    body: transformBody(groupsScout),
    headline: 'Sippen',
    color: 'blue',
  },
  {
    head: headDefault,
    body: transformBody(groupsRover),
    headline: 'Roverrunden',
    color: 'red',
  },
];

function transformBody(body) {
  return body.map((group) => {
    if (group.techName === 'stammesfuehrung') {
      return {
        id: group.techName,
        data: [group.name, group.techName],
      };
    }
    const groupData = {
      name: '--',
      meeting: 'Nach Absprache',
      ageRange: '--',
      mail: '',
    }
    groupData.name = group.name;
    groupData.mail = 'kontakt-' + group.techName;

    if (group?.meeting?.time?.length === 2) {
      groupData.meeting = `${group.meeting?.weekday || ''}, ${group.meeting.time[0]} Uhr bis ${group.meeting.time[1]} Uhr`;
    }
    if (group.ageRange?.length === 2) {
      groupData.ageRange = `${group.ageRange[0]} bis ${group.ageRange[1]}`;
    }
    return {
      id: group.techName,
      data: Object.values(groupData)
    };
  });
}

function handleRowClick(row) {
  router.push({ name: 'groupDetails', params: { group: row } });
}
</script>

<style scoped lang="scss">

</style>
