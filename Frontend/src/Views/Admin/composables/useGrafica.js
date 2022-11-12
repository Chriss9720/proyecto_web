import { ref } from 'vue';

// eslint-disable-next-line
export function useGrafica() {
  const error = ref(false);
  const labels = [];
  const Fechas = [];
  const Fecha = new Date();
  const FechaHoy = new Date();
  const ventasXHora = [];
  const visitasXHora = [];
  const cargado = ref(false);
  const cargadoVisitas = ref(false);
  const ConRate = ref(0);
  // const hoy = new Date();
  for (let i = 0; i < 3; i += 1) {
    Fecha.setDate(FechaHoy.getDate());
    Fecha.setDate(Fecha.getDate() - i);
    Fechas[i] = `${Fecha.getFullYear()}-${Fecha.getMonth() + 1}-${Fecha.getDate()}`;
  }
  function iniciarValores() {
    for (let i = 0; i <= 23; i += 1) {
      if (i < 10) {
        labels[i] = `0${i}:00:00`;
      } else {
        labels[i] = `${i}:00:00`;
      }
    }
    for (let i = 0; i <= 23; i += 1) {
      ventasXHora[i] = 0;
      visitasXHora[i] = 0;
    }
  }
  const VentasHora = async () => {
    iniciarValores();
    cargado.value = false;
    error.value = false;
    cargado.value = true;
  };
  return {
    VentasHora,
    labels,
    ventasXHora,
    cargado,
    Fechas,
    visitasXHora,
    cargadoVisitas,
    ConRate
  };
}
