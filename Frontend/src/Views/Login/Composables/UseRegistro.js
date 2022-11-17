import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useRegistro() {
  const nameUsu = ref('');
  const name = ref('');
  const password = ref('');
  const apellido_paterno = ref('');
  const apellido_materno = ref('');
  const correo = ref('');

  const Error = ref(false);
  const ErrorDatos = ref(false);
  const correcto = ref(false);
  const ValError = ref('');
  const RegistrarUsuario = async () => {
    ErrorDatos.value = false;
    Error.value = false;
    correcto.value = false;
    if (nameUsu.value == '' || password.value == '' || name.value == '' ||
      apellido_paterno.value == '' || apellido_materno.value == '' || correo.value == '') {
      ErrorDatos.value = true;
    } else {
      apiService.post('/users/', {
        username: nameUsu.value,
        password: password.value,
        nombre: name.value,
        apellido_paterno: apellido_paterno.value,
        apellido_materno: apellido_materno.value,
        correo: correo.value,
        empleado: true
      })
        .then(function (response) {
          correcto.value = true;
          console.log(response);
        })
        .catch(function (error) {
          console.log("anda en el error? aqui")
          console.log(error);
          try{
            ValError.value= error.response.data.context.Message;
          }catch(e){
            ValError.value="Ocurrio un error, verifique los datos ingresados"
          }
          console.log(ValError.value);
          console.log("anda en el error?")
          Error.value = true;
        })
    }
  }

  return {
    nameUsu,
    name,
    password,
    apellido_paterno,
    apellido_materno,
    correo,
    RegistrarUsuario,
    correcto,
    Error,
    ErrorDatos,
    ValError
  };
}