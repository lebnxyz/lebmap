<template>
  <g
    v-if="district !== undefined"
    @mouseover="hover = true"
    @mouseout="hover = false"
  >
    <path
      :class="{hover, clicked, region: true}"
      :id="id"
      :d="d"
      @click="click"
    ></path>
    <pins
      :locations="$root.locationsByDistrict['$' + district]"
      :projection="projection"
      :clicked="clicked"
    ></pins>
  </g>
</template>

<script>
import { GeoPath, GeoProjection } from 'd3';

import Pins from './pins.vue';

import * as utils from '../scripts/utils.js';

export default {
  name: 'Region',
  components: {
    Pins
  },
  props: {
    d: GeoPath,
    district: String,
    projection: GeoProjection
  },
  data() {
    return {
      id: utils.toID('path', this.district),
      hover: false,
      clicked: false
    };
  },
  methods: {
    click() {
      this.clicked = !this.clicked;
      if (this.clicked) {
        // TODO: emit stuff
      }
    }
  }
};
</script>

<style scoped>
.region {
  fill: black;
  fill-opacity: 0;
  stroke: gray;
  stroke-opacity: 0;
  stroke-width: 1px;
  stroke-linejoin: round;
  stroke-linecap: round;
}

.region.hover {
  fill: #444;
  fill-opacity: 1;
  stroke: white;
  stroke-opacity: 1;
}

.region.clicked {
  fill: red;
  fill-opacity: 1;
  stroke-width: 2px;
}
</style>
