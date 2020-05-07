<template>
  <div v-if="filteredSelection.length">
    <list-item v-bind="$attrs" v-for="(item, index) in filteredSelection" :key="item[iterKey]"
      :arrow="arrows"
      :data-list-idx="index"
      @click="click(item, index)"
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
    highlightItems: Boolean,
    arrows: {
      type: Boolean,
      default: true
    },
  },
  computed: {
    filteredSelection() {
      return this.selection.filter(i => i !== undefined);
    }
  },
  methods: {
    click(item, index) {
      if (this.highlightItems) {
        [...this.$el.querySelectorAll('.selected')].map(el => el.classList.toggle('selected', false));
        this.$el.querySelector(`[data-list-idx="${index}"]`).classList.toggle('selected', true);
      }
      this.$emit('item-clicked', item);
    }
  }
};
</script>

<style scoped>
div {
  color: white;
}
</style>
