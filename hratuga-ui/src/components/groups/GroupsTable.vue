<template>
  <table
      v-for="(ageGroup, index) in groups"
      class=" m-20 w-3/4 mx-auto divide-y divide-gray-200 table-auto border"
  >
    <thead class="bg-gray-50 border-b">
    <tr class="border-t-4" :class="ageGroupColor[index]">
      <th scope="col" class="text-center px-6 py-3 text-left border-r tracking-wider">Gruppenname</th>
      <th scope="col" class="text-center px-6 py-3 text-left border-r tracking-wider">Gruppenstunde</th>
      <th scope="col" class="text-center px-6 py-3 text-left border-r tracking-wider">Kontakt E-Mail</th>
    </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200 border-b">
    <tr v-for="group in ageGroup" :key="group"
        class="transition duration-300 ease-in-out hover:bg-gray-100 cursor-pointer" @click="openGroupPage(group.techName)">
      <td class="px-6 py-4 whitespace-nowrap border-r">
        {{ group.name }}
      </td>
      <td class="px-6 py-4 whitespace-nowrap border-r">
        {{ `${group.weekday}, ${group.timeStart} bis ${group.timeEnd}` }}
      </td>
      <td class="px-6 py-4 whitespace-nowrap border-r">
        {{ `kontakt-${group.techName}` }}
      </td>
    </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  name: "GroupsTable",
  data: () => ({
    groups: null,
    ageGroupColor: ['border-t-green-600', 'border-t-orange-300', 'border-t-blue-600', 'border-t-red-600' ]
  }),
  created() {
    this.loadGroups();
  },
  methods: {
    async loadGroups() {
      const { data } = await axios.get(`${import.meta.env.VITE_APP_API}/basic/group`);
      const groupedByAgeGroup = [[], [], [], []];
      data.forEach(({ageGroup, ...rest}) => {
        groupedByAgeGroup[ageGroup].push( {...rest, ageGroup})
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

<style scoped>

</style>
