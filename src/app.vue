<template>
  <svg width="WIDTH" height="HEIGHT">
    <map :map-data="mapJSON" :projection="projection"></map>
    <pins :locations="locations" :projection="projection"></pins>
  </svg>
</template>

<script>
import Map from 'components/map.vue';
import Pins from 'components/pins.vue';

import * as d3 from 'd3';
import * as utils from './scripts/utils.js';

// I don't feel like there's any benefit to instead importing the filepaths
// and doing `this.foo = await d3.json(path)` on them...???
import { data as locations } from './data/map/locations.json';
import { data as respondents } from './data/respondents.json';
import mapDataPath from './data/map/lb_2009_administrative_districts.geojson'

export default {
  components: {
    Map,
    Pins
  },
  propsData: {
    WIDTH: 600,
    HEIGHT: 600
  }
  data() {
    return {
      SVG_DIMS: [this.WIDTH, this.HEGIHT],
      projection: null,
      mapJSON: {},
      locations,
      respondents
    }
  },
  async mounted() {
    this.mapJSON = await d3.json(mapDataPath);
    this.projection = utils.customScaledProjection(1.1, 1.1, d3.geoMercatorRaw)
      .fitSize(this.SVG_DIMS, this.mapJSON);
  }
}
</script>

<style>

</style>
