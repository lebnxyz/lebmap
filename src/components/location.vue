<template>
  <list-item>
    {{name}}, <span class="faint">{{district}}</span>
    <span v-if="responses > 1">{{responses}}</span>
  </list-item>
</template>

<script>
import ListItem from './list-item.vue';

export default {
  props: {
    name: String,
    district: String,
    responses: Number
  },
  components: {
    ListItem
  },
  methods: {
    createResizeListener(func) {
      window.addEventListener('resize', func);
    },
    destroyResizeListener(func) {
      window.removeEventListener('resize', func);
    }
  }
};
</script>

<style scoped>
.faint {
  color: darkgray;
}
</style>
