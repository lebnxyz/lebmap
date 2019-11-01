<template>
  <div v-if="filteredSelection.length">
    <location v-for="place in filteredSelection" :key="place.name"
      :name="place.name"
      :district="place.district"
      :responses="$root.respondentQuery.count('WHERE location = $1', place.name)"
    ></location>
  </div>
  <ol v-else style="color:white;">
    <li v-for="q in $root.questions" :key="q.number" style="color:white;">
      {{q}}
    </li>
  </ol>
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
