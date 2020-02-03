<template>
  <div>
    <template v-if="!clicked">
      <list :selection="questionValues" iterKey="number" v-slot="{item: question}"
        @item-clicked="viewQuestion"
      >
        {{question.headline}}
      </list>
    </template>
    <template v-else-if="!subClicked">
      <button @click="backToQuestions">Back to questions</button>
      <br/>
      <dl>
        <dt>Question</dt>
        <dd>{{qInfo.question}}</dd>
        <dt>Environments</dt>
        <dd>
          <list :selection="answerValues" iterKey="number" v-slot="{item: answer}"
            @item-clicked="viewAnswer"
          >
            {{answer.environment}}
          </list>
        </dd>
      </dl>
    </template>
    <template v-else>
      <button @click="backToQuestionInfo">Back to question info</button>
      <dl>
        <dt>Feature</dt>
        <dd>{{qInfo.headline}}</dd>
        <dt>Option chosen</dt>
        <dd>{{answerInfo.english}}: {{answerInfo.arabic}} &lrm;<i>({{answerInfo.transliteration}})</i></dd>
        <dt>Environment</dt>
        <dd>{{answerInfo.environment}}</dd>
        <dt>Options</dt>
        <dd>
          <list :selection="optionValues" iterKey="number" v-slot="{item: option}"
            @item-clicked="showRespondents"
          >
            <i>{{option.value}}</i>.<template v-if="option.indicates.length > 0"> This answer indicates:</template>
            <div v-for="item in option.indicates" :key="item" style="border: 1px solid white; padding: 5px;">{{item}}</div>
          </list>
        </dd>
      </dl>
    </template>
  </div>
</template>

<script>
import List from './list.vue';

export default {
  name: 'QuestionList',
  components: {
    List
  },
  props: {
    questionMap: Object
  },
  data() {
    return {
      questionValues: Object.values(this.questionMap),
      clicked: false,
      subClicked: false,
      qInfo: null,
      answerInfo: null
    };
  },
  computed: {
    answerValues() {
      if (this.qInfo === null) {
        return [];
      }
      return Object.values(this.qInfo.answers);
    },
    optionValues() {
      if (this.answerInfo === null) {
        return [];
      }
      return Object.values(this.answerInfo.options);
    }
  },
  methods: {
    viewQuestion(question) {
      this.clicked = true;
      this.qInfo = question;
    },
    viewAnswer(answer) {
      this.subClicked = true;
      this.answerInfo = answer;
    },
    showRespondents(option) {
      this.$emit('show-respondents', option);
    },
    backToQuestions() {
      this.clicked = false;
      this.subClicked = false;
      this.qInfo = null;
    },
    backToQuestionInfo() {
      this.subClicked = false;
    }
  }
};
</script>

<style scoped>
dl {
  color: white;
  font-family: sans-serif;
}
dt {
  font-weight: bold;
}
</style>
