<template>
  <div class="w-full">
    <h3 class="text-3xl mt-9 mb-4 text-center">Klicke auf eine Gruppe für mehr Details</h3>
    <h4 class="text-xl text-center text-gray-500">(Alle E-Mail-Adressen enden auf [ at ] hratuga.de)</h4>
    <groups-table/>
    <p class="mb-8 text-xl text-center leading-8">
      Solltet ihr nicht wissen, welche Gruppe passend für euch ist oder ihr allgemeine Fragen haben,
      könnt ihr euch an kontakt [ at ] hratuga.de wenden.
    </p>
  </div>
</template>

<script>
import GroupPage from "@/components/groups/GroupPage.vue";
import axios from 'axios';
import GroupsTable from "@/components/groups/GroupsTable.vue";

export default {
  name: "GroupOverview",
  components: {GroupsTable, GroupPage},
  data: () => ({
    groups: null,
    ageGroupColor: ['border-t-green-600', 'border-t-orange-300', 'border-t-blue-600', 'border-t-red-600']
  }),
  created() {
    this.loadGroups();
  },
  methods: {
    async loadGroups() {
      const {data} = await axios.get(`${import.meta.env.VITE_APP_API}/basic/group`);
      const groupedByAgeGroup = [[], [], [], []];
      data.forEach(({ageGroup, ...rest}) => {
        groupedByAgeGroup[ageGroup].push({...rest, ageGroup})
      })
      console.log(groupedByAgeGroup);
      this.groups = groupedByAgeGroup;
    },
    openGroupPage(groupTechName) {
      this.$router.push({name: 'GroupPage', params: {groupTechName}})
    },
  }
}
</script>
