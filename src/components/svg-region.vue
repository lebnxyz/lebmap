<template>
  <path
    class="region"
    :id="id"
    :d="d"
    @mouseenter="raise"
  ></path>
</template>

<script>
import { GeoPath } from 'd3';

import * as utils from '../scripts/utils.js';

export default {
  name: 'SVGRegion',
  props: {
    d: GeoPath,
    district: String
  },
  data() {
    return {
      id: utils.toID('path', this.district)
    };
  },
  methods: {
    raise() {
      this.$emit('raise', this);
    }
  }
}
</script>

<style scoped>
.region {
  fill: black;
  stroke: gray;
  stroke-width: 5px;
  stroke-linejoin: round;
  stroke-linecap: round;
}

.region:hover {
  fill: lightgray;
  stroke: white;
}
</style>
