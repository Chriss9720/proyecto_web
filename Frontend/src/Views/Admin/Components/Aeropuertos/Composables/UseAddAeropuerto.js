import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useAddAeropuerto() {
  const ciudad = ref('');
  const nombre = ref('');
  const direccion = ref('');
  const codigoPostal = ref('');
  const paises = ref('');
  const ciudades = ref('');
  const Error = ref(false);
  const ErrorDatos = ref(false);
  const correcto = ref(false);
  const ValError = ref('');

  const getPaises = async (idUsuario) => {
    apiService.get('/paisEstado/paises',  {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        paises.value=response.data.paises;
      })
      .catch(function (error) {
        console.log(error);
      })
  }
  const getCiudades = async (idUsuario, id) => {
    apiService.get(`/paisEstado/estados/${id}`,  {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        ciudades.value=response.data.estados;
      })
      .catch(function (error) {
        console.log(error);
      })
  }
  const RegistrarAeroPuerto = async (idUsuario) => {
    ErrorDatos.value = false;
    Error.value = false;
    correcto.value = false;
    console.log("Los datos que recibe son ", nombre.value, " ", ciudad.value, " ", direccion.value, " ", codigoPostal.value)
    if (nombre.value == '' || ciudad.value == '' || direccion.value == '' || codigoPostal.value == '') {
      ErrorDatos.value = true;
    } else {
      apiService.post('/aereoPuerto/', {
        ciudad_id: ciudad.value,
        nombre: nombre.value,
        direccion: direccion.value,
        codigo_postal: codigoPostal.value
      }, {
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
            ValError.value = error.response.data.context.Message;
          } catch (e) {
            ValError.value = "Error al registrar, verifique los datos";
          }
          Error.value = true;
        })
    }
  }

  return {
    nombre,
    ciudad,
    direccion,
    codigoPostal,
    RegistrarAeroPuerto,
    correcto,
    Error,
    ErrorDatos,
    ValError,
    getPaises,
    paises,
    getCiudades,
    ciudades
  };
}