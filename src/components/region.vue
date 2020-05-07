<template>
  <g
    v-if="district !== undefined"
    @mouseenter="mouseenter"
  >
    <path
      :class="{clicked, region: true}"
      :id="id"
      :d="d"
      @mousedown="toggle"
    ></path>
    <pins
      :locations="locations"
      :projection="projection"
      :clicked="clicked"
      :highlighted-places="highlightedPlaces"
      :n-selected="nSelected"
      @select-pin="selectPin"
      @unselect-pin="unselectPin"
    ></pins>
  </g>
</template>

<script>
import Pins from './pins.vue';

import * as utils from '../modules/utils.js';

export default {
  name: 'Region',
  components: {
    Pins
  },
  props: {
    d: null,  // geopath
    district: String,
    projection: null,  // geoprojection
    highlightedPlaces: Set,
    nSelected: Number
  },
  data() {
    return {
      id: utils.toID('path', this.district),
      locations: this.$root.locationsByDistrict['$' + this.district],
      hover: false,
      clicked: false,
      currentlyTogglable: true
    };
  },
  computed: {
    mouseDown() {
      return this.$root.mouseDown;
    }
  },
  watch: {
    mouseDown(oldVal, newVal) {
      if (!newVal) {
        this.currentlyTogglable = true;
      }
    }
  },
  methods: {
    mouseenter() {
      if (this.mouseDown && this.currentlyTogglable) {
        this.toggle();
        this.currentlyTogglable = false;
      }
    },
    toggle() {
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
