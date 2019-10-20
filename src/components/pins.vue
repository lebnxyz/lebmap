<template>
  <g id="pins">
    <svg-pin v-for="p in pins" :key="p" :coords="p"></svg-pin>
  </g>
</template>

<script>
import SVGPin from './svg-pin.vue';

import { geoPath, GeoProjection } from 'd3';

export default {
  name: 'Pins',
  components: {
    SVGPin
  }
  props: {
    locations: Object,
    projection: GeoProjection
  },
  data() {
    return {
      pins: []
    }
  }
  mounted() {
    this.pins = Object.values(this.locations).forEach(
      place => this.projection(place.location)
    )
  }
}
</script>

<style>

</style>
