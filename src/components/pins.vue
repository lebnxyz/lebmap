<template>
  <g id="pins">
    <svg-pin v-for="p in pins" :key="p.place.name" :coords="p.coords" :place="p.place"></svg-pin>
  </g>
</template>

<script>
import SVGPin from './svg-pin.vue';

import { geoPath, GeoProjection } from 'd3';

export default {
  name: 'SVGPins',
  components: {
    SVGPin
  },
  props: {
    locations: Object,
    projection: GeoProjection
  },
  data() {
    return {
      pins: []
    }
  },
  mounted() {
    this.pins = Object.values(this.locations).forEach(
      place => ({
        coords: this.projection(place.location),
        place: place
      })
    )
  }
}
</script>

<style>

</style>
