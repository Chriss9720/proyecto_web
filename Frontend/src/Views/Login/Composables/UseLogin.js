import { ref } from 'vue';
import { useRouter } from 'vue-router';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useLogin() {
  const router = useRouter();

  const nomUsu = ref('');
  const password = ref('');
  const hasError = ref(false);
  const ValError = ref('');
  const errorDatos = ref(false);

  const makeLogin = async () => {
    if (nomUsu.value == '' || password.value == ('')) {
      errorDatos.value = true;
    } else {

      console.log(nomUsu.value, password.value);
      var body = {
        username: nomUsu.value,
        password: password.value
      }
      apiService({
        method: 'post',
        url: '/tokens',
        data: body,
        headers: { "Content-Type": "multipart/form-data" },
      })
        .then(function (response) {
          var idUsuario= response.data.access_token;
          if (nomUsu.value == "UsuarioAdmin" && password.value == '1234') {
            router.push({ name: 'AdminHome', params: { idUsuario } });
          } else {
            console.log("el id es ",idUsuario);
            router.push({ name: 'ClientHome', params: { idUsuario } });
            console.log(response);
          }
        })
        .catch(function (error) {
          console.log(error);
          ValError.value = error.response.data.context.Message;
          hasError.value = true;
        })

    }
  };

  return {
    makeLogin,
    nomUsu,
    password,
    hasError,
    errorDatos,
    ValError
  };
}
