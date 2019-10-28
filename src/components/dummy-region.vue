<template>
  <path class="region" :d="d"></path>
</template>

<script>
export default {
  name: 'DummyRegion',
  props: ['d']
};
</script>

<style scoped>
.region {
  fill: black;
  stroke: gray;
  stroke-width: 1px;
  stroke-linejoin: round;
  stroke-linecap: round;
}
</style>
