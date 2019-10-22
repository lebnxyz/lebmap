<template>
  <svg v-if="mapJSON.features.length" width="600" height="600">
    <display-map :map-data="mapJSON" :projection="projection"></display-map>
    <!--pins :locations="locations" :projection="projection"></pins-->
  </svg>
</template>

<script>
import DisplayMap from './components/display-map.vue';
import Pins from './components/pins.vue';

import * as d3 from 'd3';
import * as utils from './scripts/utils.js';

import mapDataPath from './data/map/lb_2009_administrative_districts.geojson';

export default {
  components: {
    DisplayMap,
    Pins
  },
  props: {
    defaultWidth: {
      type: Number,
      default: 600
    },
    defaultHeight: {
      type: Number,
      default: 600
    }
  },
  data() {
    return {
      projection: d3.geoMercator(),  // good enough for a default
      mapJSON: {features: []}
    }
  },
  computed: {
    width() { return this.defaultWidth; },
    height() { return this.defaultHeight; }
  },
  async mounted() {
    this.mapJSON = await d3.json(mapDataPath);
    this.projection = utils.customScaledProjection(1.1, 1, d3.geoMercatorRaw)
      .fitSize([this.width, this.height], this.mapJSON);
  }
}
</script>

<style scoped>
</style>
