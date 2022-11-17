import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useUpdatePiloto() {
  const nombre = ref('');
  const edad = ref('');
  const experiencia = ref('');

  const Error = ref(false);
  const ErrorDatos = ref(false);
  const correcto = ref(false);
  const ValError = ref('');

  const piloto = ref('');

  const ActualizarPiloto = async (idUsuario, idPiloto, vuelos) => {
    ErrorDatos.value = false;
    Error.value = false;
    correcto.value = false;
    if (nombre.value == '' || edad.value == '' || experiencia.value == '') {
      ErrorDatos.value = true;
    } else {
      apiService.put(`/piloto/${idPiloto}`, {
        nombre: nombre.value,
        edad: edad.value,
        experiencia: experiencia.value,
        total_vuelos: vuelos
      },{
        headers: {
          authorization: `Bearer ${idUsuario}`
        }
      })
        .then(function (response) {
          correcto.value = true;
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
          try {
            ValError.value = error.response.data.context.detail;
          } catch (e) {
            ValError.value = "Error al actualizar, verifique los datos";
          }
          Error.value = true;
        })
    }
  }

  const GetPiloto = async (idUsuario, idPiloto) => {

    apiService.get(`/piloto/id/${idPiloto}`, {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        piloto.value=response.data;
        nombre.value=piloto.value.nombre;
        edad.value=piloto.value.edad;
        experiencia.value=piloto.value.experiencia;
      })
      .catch(function (error) {
        console.log(error);
      })

  }



  return {
    nombre,
    edad,
    experiencia,
    ActualizarPiloto,
    correcto,
    Error,
    ErrorDatos,
    ValError,
    GetPiloto,
    piloto 
  };
}