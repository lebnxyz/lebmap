<template>
  <circle :cx="coords[0]" :cy="coords[1]" :r="defaultRadius"></circle>
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
  computed: {
    defaultRadius() {
      return oneOff.countLocationNormalized(
        this.place.name, this.$root.respondentQuery, this.MIN_RAD, this.MAX_RAD
      );
    }
  }
}
</script>

<style>

</style>
