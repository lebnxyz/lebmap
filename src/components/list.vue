<template>
  <div v-if="filteredSelection.length">
    <list-item v-for="item in filteredSelection" :key="item[key]">
      <slot v-bind:item="item"></slot>
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
    selection: Object,
    key: String
  },
  computed: {
    filteredSelection() {
      return Object.values(this.selection).filter(i => i !== undefined);
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
