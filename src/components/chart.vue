<script>
import { Bar, mixins } from 'vue-chartjs';

export default {
  name: 'Chart',
  extends: Bar,
  mixins: [
    mixins.reactiveProp
  ],
  mounted() {
    this.renderChart(this.chartData, {responsive: true});
  }
}
</script>

<style>

</style>
