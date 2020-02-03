<template>
  <list :selection="questionValues" :bold="false" iterKey="number" v-slot="{item: question}">
    {{question.headline}}
  </list>
</template>

<script>
import List from './list.vue';

export default {
  name: 'InsightList',
  components: {
    List
  },
  props: {
    questionMap: Object
  },
  data() {
    return {
      questionValues: Object.values(this.questionMap)
    };
  }
};
</script>

<style>

</style>
