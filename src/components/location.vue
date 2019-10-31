<template>
  <div class="location">
    {{name}}, <span class="faint">{{district}}</span>
    <span v-if="responses > 1">{{responses}}</span>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    district: String,
    responses: Number
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
  background-color: #222;
  width: 50%;
  margin-bottom: 1em;
  transition: 0.5s;
}

.faint {
  color: darkgray;
}
</style>
