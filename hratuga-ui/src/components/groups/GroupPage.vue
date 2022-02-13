<template>
  <div class="relative py-16 bg-white overflow-hidden">
    <div class="hidden lg:block lg:absolute lg:inset-y-0 lg:h-full lg:w-full">
      <div class="relative h-full text-lg max-w-prose mx-auto" aria-hidden="true">
      </div>
    </div>
    <div class="relative px-4 sm:px-6 lg:px-8">
      <div class="text-lg max-w-prose mx-auto space-y-10">
        <h1>
          <span
              class="mt-2 block text-3xl text-center leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
            {{ group?.name }}
          </span>
        </h1>
        <p class="mt-8 text-xl text-gray-500 leading-8">
          {{ group?.description }}
        </p>
        <figure>
          <img class="w-full rounded-lg object-scale-down"
               src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&w=1310&h=873&q=80&facepad=3"
               alt=""/>
        </figure>
        <p class="mt-8 text-xl text-center text-black leading-8" v-if="group?.isSearching">
          Wir freuen uns über neue Mitglieder! Komm doch gerne vorbei!
        </p>
        <table class="table-fixed divide-y divide-gray-200 w-full text-center">
          <thead class="border-b bg-blue-600">
          <tr>
          <th scope="col" class="py-3 pl-3">Gruppenführung</th>
          <th scope="col" class="py-3">Gruppenstunde</th>
          </tr>
          </thead>
          <tbody class="bg-blue-300">
          <tr class="border-b">
            <td class="px-6 py-4 whitespace-nowrap">{{ group?.groupLeader }}</td>
            <td>
              {{ `${group?.weekday}, ${group?.timeStart} bis ${group?.timeEnd}` }}
            </td>
          </tr>
          </tbody>
        </table>
        <div class="text-orange" v-html="group?.text"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GroupPage",
  data: () => ({
    group: null,
  }),
  created() {
    this.loadGroup();
  },
  computed: {
    groupTechName() {
      return this.$route.params.groupTechName;
    },
  },
  methods: {
    async loadGroup() {
      const { data } = await axios.get(`${import.meta.env.VITE_APP_API}/basic/group`);
      // todo replace filter with http request with argument ?techName=techName
      this.group = data.filter(g => g.techName === this.groupTechName)[0];
    },
  },
}
</script>
