<template>
  <div @click="click" :class="{item: true, bold}">
    <div> <!-- because outer div's padding messes fitty up -->
      <fitty
      :options="{maxSize, minSize, multiLine}"
      :create-listener="createResizeListener"
      :destroy-listener="destroyResizeListener"
      >
        <slot></slot>
      </fitty>
    </div>
    <span class="arrow"></span>
  </div>
</template>

<script>
export default {
  props: {
    maxSize: {
      type: Number,
      default: 20
    },
    minSize: {
      type: Number,
      default: 14
    },
    multiLine: {
      type: Boolean,
      default: true
    },
    bold: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    createResizeListener(func) {
      window.addEventListener('resize', func);
    },
    destroyResizeListener(func) {
      window.removeEventListener('resize', func);
    },
    click(e) {
      this.$emit('click', e);
    }
  }
};
</script>

<style scoped>
.item {
  font-family: 'Montserrat', sans-serif;
  font-size: larger;
  color: white;
  cursor: pointer;
  border-radius: 5px;
  background-color: #1c1c1c;
  position: relative;
  width: 50%;
  padding: 1em 2.5em 1em 1em;
  margin-bottom: 1em;
  transition: 0.5s;
  overflow: hidden; /* weird css subelement-height-or-something-like-that hack */
}

.bold {
  font-weight: 800;
}

.item:hover {
  background-color: #555;
}

.arrow {
  position: absolute;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-radius: 0 5px 5px 0;
  top: 0;
  right: 0;
  height: 100%;
  width: 1em;
  padding-right: 10px;
  padding-left: 10px;
  background-color: #777;
}

.arrow::after {
  content: "\25B6";
  font-size: 20px;
}
</style>
