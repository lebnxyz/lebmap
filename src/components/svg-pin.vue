<template>
  <circle cx="x" cy="y" r="8"></circle>
</template>

<script>
export default {
  name: "SVGPin",
  props: {
    coords: Array
  },
  data() {
    return {
      x: this.coords[0],
      y: this.coords[1]
    }
  }
}
</script>

<style>

</style>
