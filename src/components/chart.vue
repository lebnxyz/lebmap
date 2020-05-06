<script>
import { Bar, mixins } from 'vue-chartjs';

export default {
  name: 'Chart',
  extends: Bar,
  mixins: [
    mixins.reactiveProp
  ],
  props: {
    options: Object
  },
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
  watch: {
    chartData() {
      this.renderChart(this.chartData, this.options);
    }
  }
}
</script>

<style>

</style>
