<template>
  <path :id="id" :d="d"></path>
</template>

<script>
import { GeoPath } from 'd3';

import * as utils from '../scripts/utils.js';

export default {
  name: 'SVGRegion',
  props: {
    d: GeoPath,
    district: String
  },
  data() {
    return {
      id: utils.toID('path', this.district)
    }
  }
}
</script>

<style>

</style>
