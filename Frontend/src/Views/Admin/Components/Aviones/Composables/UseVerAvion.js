import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useVerAviones() {
  const Aviones = ref('');


  const GetAllAviones = async (idUsuario) => {

    apiService.get('/avion/all', {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        console.log(response);
        Aviones.value = response.data.aviones;
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  const DeleteAviones = async (idUsuario, idAvione) => {
    apiService.delete(`/aereoPuerto/${idAvione}`, {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        console.log(response);
        GetAllAviones(idUsuario);
      })
      .catch(function (error) {
        console.log(error);
      })
  }



  return {
    Aviones,
    GetAllAviones,
    DeleteAviones,
  };
}