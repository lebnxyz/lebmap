<template>
  <div class="location">
    <fitty
      :options="{maxSize: 20, multiLine: true}"
      :create-listener="createResizeListener"
      :destroy-listener="destroyResizeListener"
    >
      {{name}}, <span class="faint">{{district}}</span>
      <span v-if="responses > 1">{{responses}}</span>
    </fitty>
    <span class="arrow"></span>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    district: String,
    responses: Number
  },
  methods: {
    createResizeListener(func) {
      window.addEventListener('resize', func);
    },
    destroyResizeListener(func) {
      window.removeEventListener('resize', func);
    }
  }
};
</script>

<style scoped>
.location {
  font-family: 'Montserrat', sans-serif;
  font-weight: 800;
  font-size: larger;
  color: white;
  cursor: pointer;
  background-color: #1c1c1c;
  width: 50%;
  padding: 1em 0 1em 1em;
  margin-bottom: 1em;
  transition: 0.5s;
}

.location:hover {
  background-color: #555;
}

.faint {
  color: darkgray;
}

.arrow {
  float: right;
  padding-right: 10px;
}

.arrow::after {
  content: "\25B6 \FE0E";
  font-size: 20px;
}
</style>
