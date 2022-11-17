import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useVerAeropuerto() {
  const AeroPuertos = ref('');


  const GetAllAeroPuertos = async (idUsuario) => {

    apiService.get('/aereoPuerto/all', {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        AeroPuertos.value = response.data.aereo_puertos;
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  const DeleteAeroPuerto = async (idUsuario, idAeroPuerto) => {
    apiService.delete(`/aereoPuerto/${idAeroPuerto}`, {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        console.log(response);
        GetAllAeroPuertos(idUsuario);
      })
      .catch(function (error) {
        console.log(error);
      })
  }



  return {
    AeroPuertos,
    GetAllAeroPuertos,
    DeleteAeroPuerto,
  };
}