<template>
  <div v-if="filteredSelection.length">
    <list-item v-for="place in filteredSelection" :key="place.name"
    >
      {{place.name}}, <span class="faint">{{place.district}}</span>
      <span v-if="place.responses > 1">{{place.responses}}</span>
    </list-item>
  </div>
</template>

<script>
import ListItem from './list-item.vue';


export default {
  name: 'AnswerList',
  components: {
    ListItem
  },
  props: {
    selection: Object
  },
  computed: {
    filteredSelection() {
      return Object.values(this.selection).filter(p => p !== undefined).map(
        p => ({name: p.name, district: p.district, responses: this.countRespondents(p.name)})
      );
    }
  },
  methods: {
    countRespondents(placeName) {
      return this.$root.respondentQuery.count('WHERE location = $1', placeName);
    }
  }
};
</script>

<style scoped>
div {
  color: white;
}

.faint {
  color: darkgray;
}
</style>
