<template>
  <circle
    :class="{parentClicked, highlighted, both: clicked && highlighted, clicked: clicked && !parentClicked && !highlighted, pin: true}"
    :cx="coords[0]"
    :cy="coords[1]"
    :r="radius"
    @click="click"
    @mouseover="hover = true"
    @mouseout="hover = false"
  ></circle>
</template>

<script>
import * as oneOff from '../modules/oneOffHelpers.js';

export default {
  name: 'Pin',
  props: {
    coords: Array,
    place: Object,
    parentClicked: Boolean,
    highlightedPlaces: Set,
    nSelected: Number,
    multiplier: {
      type: Number,
      default: 1.5
    },
    MIN_RAD: {
      type: Number,
      default: 3
    },
    MAX_RAD: {
      type: Number,
      default: 15
    }
  },
  data() {
    return {
      defaultRadius: oneOff.countLocationNormalized(
        this.place.name, this.$root.respondentQuery, this.MIN_RAD, this.MAX_RAD
      ),
      hover: false,
      clicked: false,
      selected: false,
      multiplier2: 1
    };
  },
  computed: {
    radius() {
      if (this.hover) {
        return this.defaultRadius * this.multiplier * this.multiplier2;
      }
      return this.defaultRadius * this.multiplier2;
    },
    highlighted() {
      if (this.highlightable && this.highlightedPlaces.has(this.place.name)) {
        this.multiplier2 = 1.5;
        return true;
      }
      this.multiplier2 = 1;
      return false;
    },
    highlightable() {
      return this.nSelected == 0 || this.selected;
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
      this.$emit(this.clicked ? 'select-pin' : 'unselect-pin', this);
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
  fill-opacity: 0.6;
  stroke-width: 1px;
}

.pin.highlighted {
  fill: #006868;
  stroke: #00ffff;
}

.pin.both {
  stroke: white;
}
</style>
