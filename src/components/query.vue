<template>
  <div class="fullwidth">
    <div class="fullwidth flex-container vertical">
      <form class="fullwidth flex-container vertical" @submit.prevent="queryRespondents">
        <input type="text" v-model="query">
        <button type="submit">Search</button>
      </form>
    </div>
    <div class="flex-container vertical">
      <div>
        <button type="button" @click="add(' & ')">AND</button>
        <button type="button" @click="add(' | ')">OR</button>
        <button type="button" @click="add(' !')">NOT</button>
        <button type="button" @click="add(' (')">(</button>
        <button type="button" @click="add(') ')">)</button>
      </div>
    </div>
    <question-list :questionValues="$root.questionValues"
        :option-clicked-func="function(option) { this.$emit('add-question', this.answerInfo, option); }"
        :show-indices="true"
        @add-question="addQuestion"
    ></question-list>
  </div>
</template>

<script>
import QuestionList from './question-list.vue';

export default {
  name: 'Query',
  components: {
    QuestionList
  },
  data() {
    return {
      query: ''
    };
  },
  methods: {
    queryRespondents() {
      this.$emit('query-respondents', this.query);
    },
    addQuestion({number: answerID}, {number: optionNo}) {
      this.query += `${answerID}:${optionNo}`;
    },
    add(char) {
      this.query += char;
    }
  }
}
</script>

<style scoped>
.fullwidth {
  width: 100%;
}

.vertical {
  flex-direction: row;
}

.horizontal {
  flex-direction: column;
}

.flex-container {
  padding-bottom: 1em;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

form {
  padding: 1em;
  padding-bottom: 0;
  margin-bottom: 0;
}

button {
  color: white;
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  font-size: medium;
  text-transform: uppercase;
  border-radius: 10px;
  padding: 1em;
  box-shadow: none;
  border: 0px;
  border: 0;
  cursor: pointer;
  background-color: #333;
  transition: background-color 300ms;
}

button:hover {
  background-color: #666;
}

form button {
  flex: 1;
  padding: 1em;
  margin-right: 1em;
}

form input {
  font-family: 'Montserrat', sans-serif;
  font-size: medium;
  font-weight: 600;
  flex: 7;
  padding: 1em;
  border-radius: 10px;
  box-shadow: none;
  border: 0;
  background-color: white;
}
</style>