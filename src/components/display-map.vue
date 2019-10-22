<template>
  <g id="map">
    <region v-for="(p, index) in paths" :key="p.district + index"
      :district="p.district"
      :d="p.d"
      :projection="projection"
      @raise="raise(index)"
    ></region>
  </g>
</template>

<script>
import Region from './region.vue';

import { geoPath, GeoProjection } from 'd3';
import * as utils from '../scripts/utils.js';

export default {
  name: 'DisplayMap',
  components: {
    Region
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
  },
  methods: {
    raise(index) {
      const temp = this.paths[this.paths.length - 1];
      this.paths[this.paths.length - 1] = this.paths[index];
      this.$set(this.paths, index, temp);
    }
  }
};
</script>

<style scoped>
</style>
