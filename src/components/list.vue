<template>
  <div v-if="filteredSelection.length">
    <list-item v-bind="$attrs" v-for="item in filteredSelection" :key="item[iterKey]" :arrow="arrows"
      @click="click(item)"
    >
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
    arrows: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    filteredSelection() {
      return this.selection.filter(i => i !== undefined);
    }
  },
  methods: {
    click(item) {
      this.$emit('item-clicked', item);
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
