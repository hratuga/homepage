<template>
  <table
      v-for="(eventsMonth, monthIndex) in eventsYear"
      class=" m-20 w-3/4 mx-auto divide-y divide-gray-200 table-auto border"
  >
    <thead class="bg-gray-50 border-b">
    <tr class="border-t-4">
      <th scope="col" colspan="2" class="text-center font-bold px-6 py-3 text-left border-r tracking-wider"> {{ getMonthName(monthIndex) }} {{ year }} </th>
    </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200 border-b text-center">
    <tr v-for="event in eventsMonth" :key="event"
        class="transition duration-300 ease-in-out hover:bg-gray-100 cursor-pointer">
      <td class="px-6 py-4 whitespace-nowrap font-bold border-r">
        {{ event.title }}
      </td>
      <td class="px-6 py-4 whitespace-nowrap border-r">
        {{ `${new Date(event.startDate).toLocaleDateString()} - ${new Date(event.endDate).toLocaleDateString()}` }}
      </td>
    </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  name: "CalendarList",
  data: () => ({
    eventsYear: null,
    year: new Date().getFullYear(),
  }),
  created() {
    this.loadEvents();
  },
  methods: {
    getMonthName(monthIndex) {
      const months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni',
            'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];
      return months[monthIndex];
    },
    async loadEvents() {
      const { data } = await axios.get(`${import.meta.env.VITE_APP_API}/basic/event`);
      const groupedByMonth = Array.from(Array(12), () => []);
      // todo replace forEach with http request with params
      data
          .forEach(({startDate, ...rest}) => {
            const month = new Date(startDate).getMonth();
            groupedByMonth[month].push({...rest, startDate})
      });
      this.eventsYear = groupedByMonth;
    },
  }
}
</script>
