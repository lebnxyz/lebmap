<template>
  <g>
    <pin v-for="p in pins" :key="p.place.name"
      :coords="p.coords"
      :place="p.place"
      :parent-clicked="clicked"
    ></pin>
  </g>
</template>

<script>
import Pin from './pin.vue';

export default {
  name: 'Pins',
  components: {
    Pin
  },
  props: {
    locations: Array,
    projection: null,  // geoprojection
    clicked: Boolean
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
