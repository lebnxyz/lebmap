<template>
<g id="map">
  <g>
    <dummy-region v-for="p in paths" :key="p._o.ID_2"
      :d="p.d"
      :projection="projection"
    ></dummy-region>
  </g>
  <g>
    <region v-for="(p, index) in paths" :key="p.district + index"
      :district="p.district"
      :d="p.d"
      :projection="projection"
    ></region>
  </g>
</g>
</template>

<script>
import Region from './region.vue';
import DummyRegion from './dummy-region.vue';

import { geoPath, GeoProjection } from 'd3';
import * as utils from '../scripts/utils.js';

export default {
  name: 'DisplayMap',
  components: {
    Region,
    DummyRegion
  },
  props: {
    mapData: Object,
    projection: GeoProjection
  },
  data() {
    const arr = [], path = geoPath(this.projection);
    this.mapData.features.forEach(
      o => arr.push({
        d: path(o),
        district: o.properties.DISTRICT,
        _o: o
      })
    );
    return {
      paths: arr,
      path: path
    };
  }
};
</script>

<style scoped>
</style>
