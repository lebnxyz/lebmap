<template>
  <g id="map">
    <svg-region v-for="p in paths" :key="p" :id="p.id" :d="p.d"></svg-region>
  </g>
</template>

<script>
import SVGRegion from './region.vue';

import { geoPath, geoProjection } from 'd3';
import * as utils from '../scripts/utils.js';

export default {
  name: 'Map',
  components: {
    SVGRegion
  },
  props: {
    mapData: Object,
    projection: geoProjection
  },
  data() {
    return {
      path: geoPath(this.projection),
      paths: []
    }
  },
  mounted() {
    this.paths = this.mapData.features.forEach(
      d => ({d: path(d), district: d.properties.DISTRICT})
    )
  }
}
</script>

<style>

</style>
