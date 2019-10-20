<template>
  <path :id="id" :d="d"></path>
</template>

<script>
import { GeoPath } from 'd3';

import * as utils from '../scripts/utils.js';

export default {
  name: 'SVGRegion',
  props: {
    id: String,
    district: String
  },
  data() {
    return {
      id: utils.toID('path', d.properties.DISTRICT)
    }
  }
}
</script>

<style>

</style>
