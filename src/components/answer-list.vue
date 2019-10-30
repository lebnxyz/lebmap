<template>
  <div>
    {{selection}}
  </div>
</template>

<script>
export default {
  name: 'AnswerList',
  props: {
    selection: Object
  },
};
</script>

<style scoped>
div {
  color: white;
}
</style>
