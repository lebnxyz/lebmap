<template>
  <circle cx="x" cy="y" r="defaultRadius"></circle>
</template>

<script>
import * as oneOff from '../scripts/oneOffHelpers.js';

export default {
  name: 'SVGPin',
  props: {
    coords: Array,
    place: Object,
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
      x: this.coords[0],
      y: this.coords[1],
      defaultRadius: oneOff.countLocationNormalized(
        this.place.name, this.$root.respondentQuery, this.MIN_RAD, this.MAX_RAD
      )
    }
  }
}
</script>

<style>

</style>
