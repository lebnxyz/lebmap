<template>
  <div v-if="filteredSelection.length">
    <location v-for="place in filteredSelection" :key="place.name"
      :name="place.name"
      :district="place.district"
      :responses="$root.respondentQuery.count('WHERE location = $1', place.name)"
    ></location>
  </div>
</template>

<script>
import Location from './location.vue';


export default {
  name: 'AnswerList',
  components: {
    Location
  },
  props: {
    selection: Object
  },
  computed: {
    filteredSelection() {
      return Object.values(this.selection).filter(p => p !== undefined);
    }
  }
};
</script>

<style scoped>
div {
  color: white;
}
</style>
