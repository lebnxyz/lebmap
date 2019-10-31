<template>
  <div>
    <location v-for="place in Object.values(selection).filter(p => p !== undefined)" :key="place.name"
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
};
</script>

<style scoped>
div {
  color: white;
}
</style>
