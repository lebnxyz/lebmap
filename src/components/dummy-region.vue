<template>
  <path class="region" :d="d"></path>
</template>

<script>
import { GeoPath } from 'd3';

export default {
  name: 'DummyRegion',
  props: {
    d: GeoPath,
  }
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
