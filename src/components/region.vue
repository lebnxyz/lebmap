<template>
<g
  @mouseover="isHovered = true"
  @mouseout="isHovered = false"
>
  <path
    :class="{region: true, hover: isHovered}"
    :id="id"
    :d="d"
  ></path>
  <pins :locations="$root.locationsByDistrict['$' + district]" :projection="projection"></pins>
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
      isHovered: false
    };
  },
  methods: {
    raise() {
      this.$emit('raise');
    }
  }
};
</script>

<style scoped>
.region {
  fill: black;
  stroke: gray;
  stroke-width: 5px;
  stroke-linejoin: round;
  stroke-linecap: round;
}

.region.hover {
  fill: #d3d3d3;
}
</style>
