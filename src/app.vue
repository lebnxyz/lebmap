<template>
  <svg v-if="regionPaths.length" width="600" height="600">
    <g>
      <dummy-region v-for="p in regionPaths" :key="p._o.ID_2"
        :d="p.d"
      ></dummy-region>
    </g>
    <g>
      <region v-for="(p, index) in regionPaths" :key="p.district + index"
        :district="p.district"
        :d="p.d"
        :projection="projection"
      ></region>
    </g>
  </svg>
</template>

<script>
import DummyRegion from './components/dummy-region.vue';
import Region from './components/region.vue';

import { geoMercator, geoPath, geoMercatorRaw } from 'd3';
import * as utils from './scripts/utils.js';

import mapData from './data/map/lb_2009_administrative_districts.json';

export default {
  name: 'App',
  components: {
    DummyRegion,
    Region
  },
  props: {
    defaultWidth: {
      type: Number,
      default: 600
    },
    defaultHeight: {
      type: Number,
      default: 600
    }
  },
  data() {
    return {
      mapJSON: {features: []},
      regionPaths: []
    }
  },
  computed: {
    width() {
      return this.defaultWidth;
    },
    height() {
      return this.defaultHeight;
    },
    projection() {
      if (!this.mapJSON.features.length) {
        return geoMercator();
      }
      return utils.customScaledProjection(1.1, 1, geoMercatorRaw)
        .fitSize([this.width, this.height], this.mapJSON);
    },
    path() {
      return geoPath(this.projection);
    }
  },
  mounted() {
    this.mapJSON = mapData;
    this.mapJSON.features.forEach(
      o => this.regionPaths.push({
        d: this.path(o),
        district: o.properties.DISTRICT,
        _o: o
      })
    );
  }
}
</script>

<style scoped>
</style>
