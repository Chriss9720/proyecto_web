import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useVerPiloto() {
  const pilotos = ref('');


  const GetAllPilotos = async (idUsuario) => {

    apiService.get('/piloto/all', {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        pilotos.value = response.data.pilotos;
        console.log("los pilotos son",pilotos.value);
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  const DeletePiloto = async (idUsuario, idPiloto) => {

    apiService.delete(`/piloto/${idPiloto}`, {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  const VerPilotoFiltrado = async (idUsuario, filtro, datFiltro) => {
    switch (filtro) {
      case 'Nombre':
        apiService.get(`/piloto/name/${datFiltro}`, {
          headers: {
            authorization: `Bearer ${idUsuario}`
          }
        })
          .then(function (response) {
            pilotos.value = response.data;
          })
          .catch(function (error) {
            console.log(error);
          })
        break;
      case 'Experiencia':
        apiService.get(`/piloto/exp/${datFiltro}`, {
          headers: {
            authorization: `Bearer ${idUsuario}`
          }
        })
          .then(function (response) {
            pilotos.value = response.data;
          })
          .catch(function (error) {
            console.log(error);
          })
        break;
      case 'Vuelos':
        apiService.get(`/piloto/vuelos/${datFiltro}`, {
          headers: {
            authorization: `Bearer ${idUsuario}`
          }
        })
          .then(function (response) {
            pilotos.value = response.data;
          })
          .catch(function (error) {
            console.log(error);
          })
        break;
    }
  }

  return {
    pilotos,
    GetAllPilotos,
    DeletePiloto,
    VerPilotoFiltrado
  };
}