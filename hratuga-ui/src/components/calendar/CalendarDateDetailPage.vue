<template>
  <div class="flex justify-center">
    <div class="block p-6 rounded-lg shadow-lg bg-white max-w-sm">
      <arrow-left-icon class="h-7 w-7 mb-3 cursor-pointer" aria-hidden="true" @click="this.$router.push({ name: 'Calendar' })"/>
      <h5 class="text-gray-900 text-3xl leading-tight font-medium mb-2">Card title</h5>
      <p class="text-gray-700 text-lg mb-4">
        Some quick example text to build on the card title and make up the bulk of the card's
        content.
      </p>
      <button type="button" class=" inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Button</button>
    </div>
  </div>
</template>

<script>
import { ArrowLeftIcon } from '@heroicons/vue/solid'

export default {
  name: "CalendarDateDetailPage",
  components: { ArrowLeftIcon },
  event: {
    "id": 2,
    "createdAt": null,
    "updatedAt": "2022-02-13T02:09:42.011967Z",
    "title": "Aktionen",
    "organizer": "Stamm",
    "responsiblePerson": "Hratuga",
    "description": "<django_quill.fields.FieldQuill object at 0x7efe71a5a160>",
    "startDate": "2022-12-01T10:00:00Z",
    "endDate": "2022-12-15T20:00:00Z",
    "deadlineDate": "2022-11-01T00:00:00Z",
    "startPlace": "Heim",
    "endPlace": "Heim",
    "costs": 1000000.0,
    "isPublic": true,
    "inHeim": true,
    "groups": [
      3,
      4,
      5,
      6,
      7
    ]
  },
}
</script>
