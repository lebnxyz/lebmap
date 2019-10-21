<template>
  <g id="map">
    <SVGRegion v-for="p in paths" :key="p._o.ID_2" :district="p.district" :d="p.d"></SVGRegion>
  </g>
</template>

<script>
import SVGRegion from './svg-region.vue';

import { geoPath, GeoProjection } from 'd3';
import * as utils from '../scripts/utils.js';

export default {
  name: 'SVGMap',
  components: {
    SVGRegion
  },
  props: {
    mapData: Object,
    projection: GeoProjection
  },
  computed: {
    paths() {
      const arr = [];
      this.mapData.features.forEach(
        o => console.log(o) || arr.push({
          d: this.path(o),
          district: o.properties.DISTRICT,
          _o: o
        })
      );
      return arr;
    },
    path() {
      window.path = geoPath(this.projection);
      return geoPath(this.projection);
    }
  },
  mounted() {}
}
</script>

<style>

</style>
