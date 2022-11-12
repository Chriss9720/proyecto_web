<template>
  <div class="GraficaVentas">
    <h2>Venta de boletos por hora</h2>
  <select v-model="seleccion">
    <option v-for="i of Fechas" v-bind:key="i">{{i}}</option>
  </select>
  <Bar v-if="cargado"
    :chart-options="chartOptions"
    :chart-data="chartData"
  />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';
import { useGrafica } from '../composables/useGrafica';

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: 'GraficaVentas',
  components: { Bar },
  setup() {
    const {
      VentasHora,
      labels,
      ventasXHora,
      cargado,
      ventasXHoraAnteAyer,
      ventasXHoraAyer,
      Fechas
    } = useGrafica();
    const Hoy = new Date();
    const hoyFormato = `${Hoy.getFullYear()}-${Hoy.getMonth() + 1}-${Hoy.getDate()}`;
    VentasHora(hoyFormato);
    return {
      VentasHora,
      labels,
      ventasXHora,
      cargado,
      ventasXHoraAnteAyer,
      ventasXHoraAyer,
      Fechas
    };
  },
  data() {
    return {
      seleccion: this.Fechas[0],
      chartData: {
        labels: this.labels,
        datasets: [{
          label: 'Boletos',
          backgroundColor: '#3040f0',
          data: this.ventasXHora
        }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  watch: {
    seleccion(newSeleccion) {
      this.VentasHora(newSeleccion);
    }
  }
};
</script>

<style>
h2{
    font-family: 'Kaushan Script', cursive;
}
</style>