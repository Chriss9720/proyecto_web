import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useUpdateAeroPuerto() {
  const ciudad = ref('');
  const nombre = ref('');
  const direccion = ref('');
  const codigoPostal = ref('');

  const Error = ref(false);
  const ErrorDatos = ref(false);
  const correcto = ref(false);
  const ValError = ref('');

  const AeroPuerto = ref('');

  const ActualizarAeroPuerto = async (idUsuario, idAeroPuerto) => {
    ErrorDatos.value = false;
    Error.value = false;
    correcto.value = false;
    if (nombre.value == '' || ciudad.value == '' || direccion.value == '' || codigoPostal.value == '') {
      ErrorDatos.value = true;
    } else {
      apiService.put(`/aereoPuerto/${idAeroPuerto}`, {
        ciudad_id: ciudad.value,
        nombre: nombre.value,
        direccion: direccion.value,
        codigo_postal: codigoPostal.value
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

  const GetAeroPuerto = async (idUsuario, idAeroPuerto) => {
    apiService.get(`/aereoPuerto/id/{${idAeroPuerto}`, {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        AeroPuerto.value=response.data;
        nombre.value=AeroPuerto.value.nombre;
        direccion.value=AeroPuerto.value.direccion;
        codigoPostal.value=AeroPuerto.value.codigo_postal;
      })
      .catch(function (error) {
        console.log(error);
      })

  }

  return {
    nombre,
    ciudad,
    direccion,
    codigoPostal,
    ActualizarAeroPuerto,
    correcto,
    Error,
    ErrorDatos,
    ValError,
    GetAeroPuerto,
    AeroPuerto 
  };
}