import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useAddAvion() {
  const cap_max_pasajeros = ref('');
  const cap_max_equipaje_kilos = ref('');
  const origen_id = ref('');
  const destino_id = ref('');
  const salida = ref('');
  const llegada = ref('');
  const filas = ref('');
  const piloto_id = ref('');

 
  const Error = ref(false);
  const ErrorDatos = ref(false);
  const correcto = ref(false);
  const ValError = ref('');

  const RegistrarAeroPuerto = async (idUsuario) => {
    ErrorDatos.value = false;
    Error.value = false;
    correcto.value = false;
    if (cap_max_pasajeros.value == '' || cap_max_equipaje_kilos.value == '' || origen_id.value == '' || destino_id.value == ''
      || salida.value == '' || llegada.value == '' || filas.value == '' || piloto_id.value == '') {
      ErrorDatos.value = true;
    } else {
      apiService.post('/avion/', {
        cap_max_pasajeros: cap_max_pasajeros.value,
        cap_max_equipaje_kilos: cap_max_equipaje_kilos.value,
        origen_id: origen_id.value.toString(),
        destino_id: destino_id.value.toString(),
        salida: salida.value,
        llegada: llegada.value,
        filas: filas.value,
        estado: "Preparando",
        piloto_id: piloto_id.value.toString()
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
            ValError.value = error.response.data.context.detail;
          } catch (e) {
            ValError.value = "Error al registrar, verifique los datos";
          }
          Error.value = true;
        })
    }
  }
 const AeroPuertosO = ref('');
 const AeroPuertosD = ref('');
  const GetAllAeroPuertosO = async (idUsuario) => {

    apiService.get('/aereoPuerto/all', {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        
        AeroPuertosO.value = response.data.aereo_puertos;
        console.log("Los aeropuetos o son ", AeroPuertosO.value)
      })
      .catch(function (error) {
        console.log(error);
      })
  }
  const GetAllAeroPuertosD = async (idUsuario) => {

    apiService.get('/aereoPuerto/all', {
      headers: {
        authorization: `Bearer ${idUsuario}`
      }
    })
      .then(function (response) {
        AeroPuertosD .value = response.data.aereo_puertos;
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  return {
    cap_max_pasajeros,
    cap_max_equipaje_kilos,
    origen_id,
    destino_id,
    salida,
    llegada,
    filas,
    piloto_id,
    RegistrarAeroPuerto,
    correcto,
    Error,
    ErrorDatos,
    ValError,
    AeroPuertosO,
    AeroPuertosD,
    GetAllAeroPuertosD,
    GetAllAeroPuertosO
  };
}