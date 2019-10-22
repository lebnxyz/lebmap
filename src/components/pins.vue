<template>
<svg>
  <pin v-for="p in pins" :key="p.place.name"
    :coords="p.coords"
    :place="p.place"
  ></pin>
</svg>
</template>

<script>
import Pin from './pin.vue';

import { geoPath, GeoProjection } from 'd3';

export default {
  name: 'Pins',
  components: {
    Pin
  },
  props: {
    locations: Array,
    projection: GeoProjection
  },
  data() {
    const arr = [];
    Object.values(this.locations || {}).forEach(
      place => arr.push({
        coords: this.projection(place.location),
        place: place
      })
    );
    return {
      pins: arr
    };
  }
};
</script>

<style>

</style>
