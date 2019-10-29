<template>
  <g>
    <pin v-for="p in pins" :key="p.place.name"
      :coords="projection(p.coords)"
      :place="p.place"
      :parent-clicked="clicked"
      v-on="$listeners"
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
    const pins = [];
    Object.values(this.locations || {}).forEach(
      place => pins.push({
        coords: place.location,
        place: place
      })
    );
    return {pins};
  }
};
</script>

<style>

</style>
