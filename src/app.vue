<template>
  <svg :width="WIDTH" :height="HEIGHT">
    <SVGMap :map-data="mapJSON" :projection="projection"></SVGMap>
    <SVGPins :locations="locations" :projection="projection"></SVGPins>
  </svg>
</template>

<script>
import SVGMap from './components/svg-map.vue';
import SVGPins from './components/pins.vue';

import * as d3 from 'd3';
import * as utils from './scripts/utils.js';

// I don't feel like there's any benefit to instead importing the filepaths
// and doing `this.foo = await d3.json(path)` on them...???
import { data as locations } from './data/map/locations.json';
import mapDataPath from './data/map/lb_2009_administrative_districts.geojson';

export default {
  components: {
    SVGMap,
    SVGPins
  },
  data() {
    return {
      WIDTH: 600,
      HEIGHT: 600,
      projection: d3.geoMercator(),  // good enough for a default
      mapJSON: {features: []},
      locations
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
