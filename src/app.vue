<template>
  <svg v-if="mapJSON.features.length" :width="WIDTH" :height="HEIGHT">
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
  data() {
    return {
      WIDTH: 600,
      HEIGHT: 600,
      projection: d3.geoMercator(),  // good enough for a default
      mapJSON: {features: []}
    }
  },
  async mounted() {
    this.mapJSON = await d3.json(mapDataPath);
    this.projection = utils.customScaledProjection(1.1, 1, d3.geoMercatorRaw)
      .fitSize([this.WIDTH, this.HEIGHT], this.mapJSON);
  }
}
</script>

<style>

</style>
