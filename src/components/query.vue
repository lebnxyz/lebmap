<template>
  <div class="fullwidth">
    <div class="fullwidth flex-container vertical">
      <form
        class="fullwidth flex-container vertical"
        autocomplete="off"
        @submit.prevent="queryRespondents"
      >
        <input
          autofocus
          id="query"
          type="text"
          placeholder="Search for..."
          v-model="query"
          @focus="current = 'query'"
        >
        <span>/</span>
        <input
          id="outOf"
          type="text"
          placeholder="Out of..."
          v-model="outOf"
          @focus="current = 'outOf'"
        >
        <button type="submit">Search</button>
      </form>
    </div>
    <div class="flex-container vertical space-bottom">
      <div>
        <button type="button" @click="add(' & ')">AND</button>
        <button type="button" @click="add(' | ')">OR</button>
        <button type="button" @click="add(' !')">NOT</button>
        <button type="button" @click="add(' = ')">EQUALS</button>
        <button type="button" @click="add(' (')">(</button>
        <button type="button" @click="add(') ')">)</button>
      </div>
    </div>
    <question-list ref="ql" :questionValues="$root.questionValues"
        :option-clicked-func="function(option) { this.$emit('add-question', this.answerInfo, option); }"
        :show-indices="true"
        :highlight-items="false"
        @clear-state="$emit('clear-state')"
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
      query: '',
      outOf: '',
      current: null
    };
  },
  methods: {
    getCurrent() {
      return this[this.current];
    },
    setCurrent(value) {
      this[this.current] = value;
    },
    queryRespondents() {
      this.$refs.ql.backToQuestions();
      this.$emit('query-respondents', this.query, this.outOf.length ? this.outOf : null);
    },
    addQuestion({number: answerID}, {number: optionNo}) {
      this.add(` ${answerID}:${optionNo} `);
    },
    add(char) {
      if (this.current === null) {
        return;
      }
      const currentEl = document.getElementById(this.current);
      if (currentEl.value === '') {
        this.setCurrent(char.trim());
        currentEl.selectionStart = currentEl.selectionEnd = currentEl.value.length;
      } else {
        this.setCurrent([
          this.getCurrent().substring(0, currentEl.selectionStart).trim(),
          char,
          this.getCurrent().substring(currentEl.selectionEnd).trim()
        ].join('').trim());
      }
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
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

.space-bottom {
  margin-bottom: 2em;
}

form {
  margin: 1em;
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
  margin: 1em;
  margin-top: 0;
}

form input {
  font-family: 'Montserrat', sans-serif;
  font-size: medium;
  font-weight: 600;
  flex: 2;
  min-width: 0;
  padding-top: 1em;
  padding-bottom: 1em;
  padding-left: .5em;
  padding-right: .5em;
  border-radius: 10px;
  box-shadow: none;
  border: 0;
  background-color: white;
}

form span {
  font-family: 'Montserrat', sans-serif;
  font-size: large;
  font-weight: 600;
  color: white;
  text-align: center;
  margin: 1em;
}
</style>
