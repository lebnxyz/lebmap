<template>
  <g id="pins">
    <SVGPin v-for="p in pins" :key="p.place.name" :coords="p.coords" :place="p.place"></SVGPin>
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
    const arr = [];
    Object.values(this.locations).forEach(
      place => arr.push({
        coords: this.projection(place.location),
        place: place
      })
    );
    return {
      pins: arr
    };
  }
}
</script>

<style>

</style>
