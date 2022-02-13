<template>
  <div class="flex items-center mt-5">
    <div class="flex items-center rounded-md md:items-stretch mx-auto">
      <button type="button"
              class="flex items-center justify-center rounded-l-md border text-xl border-gray-300 bg-white py-2 pl-3 pr-4 text-gray-400 hover:text-gray-500 focus:relative md:w-9 md:px-2 md:hover:bg-gray-50">
        <span class="sr-only">Previous year</span>
        <chevron-left-icon class="h-5 w-5" aria-hidden="true" @click="changeYear(-1)"/>
      </button>
      <button type="button"
              class="border-t border-b border-gray-300 bg-white px-3.5 text-xl font-medium text-gray-700 hover:bg-gray-50 hover:text-gray-900 focus:relative md:block md:px-2 py-1">
        {{ year }}
      </button>
      <span class="relative -mx-px h-5 w-px bg-gray-300 md:hidden"/>
      <button type="button"
              class="flex items-center justify-center rounded-r-md border text-xl border-gray-300 bg-white py-2 pl-4 pr-3 text-gray-400 hover:text-gray-500 focus:relative md:w-9 md:px-2 md:hover:bg-gray-50">
        <span class="sr-only">Next year</span>
        <chevron-right-icon class="h-5 w-5" aria-hidden="true" @click="changeYear(1)"/>
      </button>
    </div>
  </div>
  <table
      v-for="(eventsMonth, monthIndex) in eventsYear"
      class=" m-20 w-1/2 mx-auto divide-y divide-gray-200 table-auto border"
  >
    <thead class="bg-gray-50 border-b">
    <tr class="border-t-4" :class="getMonthColor(monthIndex)">
      <th scope="col" colspan="2"
          class="text-center font-bold px-6 py-3 text-left border-r tracking-wider"
      >
        {{ getMonthName(monthIndex) }} {{ year }}
      </th>
    </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200 border-b text-center">
    <tr v-for="event in eventsMonth" :key="event"
        class="transition duration-300 ease-in-out hover:bg-gray-100 cursor-pointer"
    >
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
import {ChevronLeftIcon, ChevronRightIcon} from '@heroicons/vue/solid'
import axios from "axios";

export default {
  name: "CalendarList",
  components: {ChevronLeftIcon, ChevronRightIcon},
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
    getMonthColor(monthIndex) {
      const months = ['border-indigo-500', 'border-blue-500', 'border-cyan-500', 'border-emerald-500',
        'border-lime-500', 'border-yellow-500', 'border-orange-500', 'border-red-500', 'border-rose-500',
        'border-pink-500', 'border-fuchsia-500', 'border-violet-500'];
      return months[monthIndex];
    },
    async changeYear(change) {
      this.year += change;
      await this.loadEvents();
    },
    async loadEvents() {
      const {data} = await axios.get(`${import.meta.env.VITE_APP_API}/basic/event`);
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
