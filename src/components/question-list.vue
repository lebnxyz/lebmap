<template>
  <div>
    <template v-if="!clicked">
      <list :selection="questionValues" iterKey="number" v-slot="{item: question}"
        :show-indices="showIndices"
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
              :show-indices="showIndices"
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
              :show-indices="showIndices"
              :arrows="false"
              :highlight-items="true"
              @item-clicked="optionClicked"
            >
              <i>{{option.value}}</i><template v-if="option.indicates.length > 0">. This answer indicates:</template>
              <div v-for="item in option.indicates" :key="item"
                style="border: 1px solid white; border-radius: 5px; padding: 5px;"
              >
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
            :show-indices="showIndices"
            :arrows="false"
            :highlight-items="true"
            @item-clicked="optionClicked"
          >
            <i>{{option.value}}</i><template v-if="option.indicates.length > 0">. This answer indicates:</template>
            <div v-for="item in option.indicates" :key="item"
              style="border: 1px solid white; border-radius: 5px; padding: 5px;"
            >
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
    questionValues: Array,
    showIndices: Boolean,
    optionClickedFunc: {
      type: Function,
      default: () => {}
    },
    clearStateFunc: {
      type: Function,
      default: function() { this.$emit('clear-state'); }
    }
  },
  data() {
    return {
      clicked: false,
      subClicked: false,
      qInfo: null,
      answerInfo: null,
      optionClicked: this.optionClickedFunc.bind(this),
      clearState: this.clearStateFunc.bind(this)
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
    },
    optionsShowing() {
      return this.answerInfo !== null;  //this.subClicked || this.answerValues.length == 1;
    }
  },
  watch: {
    optionsShowing(value, old) {
      if (value) {
        this.$emit('show-options', this.answerInfo);
      } else {
        this.$emit('remove-options');
      }
    }
  },
  mounted() {
    this.clearState();
  },
  methods: {
    viewQuestion(question) {
      this.clicked = true;
      this.qInfo = question;
      if (this.answerValues.length == 1) {
        this.answerInfo = this.answerValues[0];
      }
    },
    viewAnswer(answer) {
      this.subClicked = true;
      this.answerInfo = answer;
    },
    backToQuestions() {
      this.clearState();
      this.clicked = false;
      this.subClicked = false;
      this.qInfo = null;
      this.answerInfo = null;
    },
    backToQuestionInfo() {
      this.clearState();
      this.subClicked = false;
      this.answerInfo = null;
    }
  }
};
</script>

<style scoped>
dl {
  color: white;
  font-family: 'Montserrat', sans-serif;
}

dt {
  font-weight: bold;
}
</style>
