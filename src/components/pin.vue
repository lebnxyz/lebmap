<template>
  <circle
    :class="{parentClicked, clicked: clicked && !parentClicked, pin: true}"
    :cx="coords[0]"
    :cy="coords[1]"
    :r="radius"
    @click="click"
    @mouseover="hover = true"
    @mouseout="hover = false"
  ></circle>
</template>

<script>
import * as oneOff from '../scripts/oneOffHelpers.js';

export default {
  name: 'Pin',
  props: {
    coords: Array,
    place: Object,
    parentClicked: Boolean,
    multiplier: {
      type: Number,
      default: 1.5
    },
    MIN_RAD: {
      type: Number,
      default: 4
    },
    MAX_RAD: {
      type: Number,
      default: 10
    }
  },
  data() {
    return {
      defaultRadius: oneOff.countLocationNormalized(
        this.place.name, this.$root.respondentQuery, this.MIN_RAD, this.MAX_RAD
      ),
      hover: false,
      clicked: false
    };
  },
  computed: {
    radius() {
      if (this.hover) {
        return this.defaultRadius * this.multiplier;
      }
      return this.defaultRadius;
    }
  },
  watch: {
    parentClicked(val) {
      if (val) {
        this.clicked = false;
      }
    }
  },
  methods: {
    click() {
      if (this.parentClicked) {
        return;
      }
      this.clicked = !this.clicked;
      if (this.clicked) {
        // TODO: emit stuff
      }
    }
  }
};
</script>

<style scoped>
.pin {
  stroke-width: 1px;
  fill: white;
  stroke: black;
  cursor: pointer;
  transition: 0.05s;
}

.pin.clicked {
  fill: #9aff9a;
  stroke: #151;
  stroke-width: 2px;
}

.pin.parentClicked {
  fill-opacity: 0.8;
  stroke-width: 2px;
}
</style>
