<template>
  <div v-if="filteredSelection.length">
    <list-item :bold="bold" v-for="item in filteredSelection" :key="item[iterKey]">
      <slot v-bind:item="item"></slot>
    </list-item>
  </div>
</template>

<script>
import ListItem from './list-item.vue';


export default {
  name: 'List',
  components: {
    ListItem
  },
  props: {
    selection: Array,
    iterKey: String,
    bold: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    filteredSelection() {
      return this.selection.filter(i => i !== undefined);
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
