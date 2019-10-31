<template>
  <g v-if="district !== undefined">
    <path
      :class="{clicked, region: true}"
      :id="id"
      :d="d"
      @click="click"
    ></path>
    <pins
      :locations="locations"
      :projection="projection"
      :clicked="clicked"
      @select-pin="selectPin"
      @unselect-pin="unselectPin"
    ></pins>
  </g>
</template>

<script>
import Pins from './pins.vue';

import * as utils from '../scripts/utils.js';

export default {
  name: 'Region',
  components: {
    Pins
  },
  props: {
    d: null,  // geopath
    district: String,
    projection: null  // geoprojection
  },
  data() {
    return {
      id: utils.toID('path', this.district),
      locations: this.$root.locationsByDistrict['$' + this.district],
      hover: false,
      clicked: false
    };
  },
  methods: {
    click() {
      this.clicked = !this.clicked;
      this.$emit(this.clicked ? 'select' : 'unselect', this.$children[0].$children);
    },
    selectPin(pin) {
      this.$emit('select', [pin]);
    },
    unselectPin(pin) {
      this.$emit('unselect', [pin]);
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

.region:hover {
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
