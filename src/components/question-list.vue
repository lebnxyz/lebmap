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
        <dt>Flaws</dt>
        <dd>
          <ul>
            <li v-for="item of qInfo.flaws" :key="item">{{item}}</li>
          </ul>
        </dd>
        <template v-if="answerValues.length > 1">
          <dt>Environments</dt>
          <dd>
            <list :selection="answerValues" iterKey="number" v-slot="{item: answer}"
              @item-clicked="viewAnswer"
            >
              {{answer.environment}}
            </list>
          </dd>
        </template>
        <template v-else>
          <dt>Options</dt>
          <dd>
            <list :selection="optionValues" iterKey="number" v-slot="{item: option}"
              @item-clicked="showRespondents"
            >
              <i>{{option.value}}</i><template v-if="option.indicates.length > 0">. This answer indicates:</template>
              <div v-for="item in option.indicates" :key="item" style="border: 1px solid white; padding: 5px;">
                {{item}}
              </div>
            </list>
          </dd>
        </template>
      </dl>
    </template>
    <template v-else>
      <button @click="backToQuestionInfo">Back to question info</button>
      <dl>
        <dt>Feature</dt>
        <dd>{{qInfo.headline}}</dd>
        <dt>Option chosen</dt>
        <dd>
          <span v-if="answerInfo.english">{{answerInfo.english}}: </span>
          <span v-if="answerInfo.arabic">{{answerInfo.arabic}} </span>
          <span v-if="answerInfo.arabic && answerInfo.transliteration">&lrm;</span>
          <span v-if="answerInfo.transliteration"><i>({{answerInfo.transliteration}})</i></span>
        </dd>
        <dt>Environment</dt>
        <dd>{{answerInfo.environment}}</dd>
        <dt>Options</dt>
        <dd>
          <list :selection="optionValues" iterKey="number" v-slot="{item: option}"
            @item-clicked="showRespondents"
          >
            <i>{{option.value}}</i><template v-if="option.indicates.length > 0">. This answer indicates:</template>
            <div v-for="item in option.indicates" :key="item" style="border: 1px solid white; padding: 5px;">
              {{item}}
            </div>
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
      if (this.answerValues.length == 1) {
        this.answerInfo = this.answerValues[0];
      }
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
      this.$emit('show-respondents', option.answeredBy);
    },
    backToQuestions() {
      this.clicked = false;
      this.subClicked = false;
      this.qInfo = null;
    },
    backToQuestionInfo() {
      this.$emit('show-respondents', []);
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
