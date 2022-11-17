import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useAddPiloto() {
  const nombre = ref('');
  const edad = ref('');
  const experiencia = ref('');

  const Error = ref(false);
  const ErrorDatos = ref(false);
  const correcto = ref(false);
  const ValError = ref('');

  const RegistrarPiloto = async (idUsuario) => {
    console.log("entra a registrar piloto");
    ErrorDatos.value = false;
    Error.value = false;
    correcto.value = false;
    if (nombre.value == '' || edad.value == '' || experiencia.value == '') {
      ErrorDatos.value = true;
    } else {
      apiService.post('/piloto', {
        nombre: nombre.value,
        edad: edad.value,
        experiencia: experiencia.value,
        total_vuelos: 0
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
            ValError.value = error.response.data.context.Message;
          } catch (e) {
            ValError.value = "Error al registrar, verifique los datos";
          }
          Error.value = true;
        })
    }
    console.log("sale sin error");
  }

  return {
    nombre,
    edad,
    experiencia,
    RegistrarPiloto,
    correcto,
    Error,
    ErrorDatos,
    ValError
  };
}