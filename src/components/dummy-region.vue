<template>
<path class="region" :d="d"></path>
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
    projection: GeoProjection
  },
  data() {
    return {
      id: utils.toID('path', this.district),
      isHovered: false
    };
  }
};
</script>

<style scoped>
.region {
  fill: black;
  stroke: gray;
  stroke-width: 1px;
  stroke-linejoin: round;
  stroke-linecap: round;
}

</style>
