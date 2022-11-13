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
      if (nomUsu.value == "admin@gmail.com") {
        router.push({ name: 'AdminHome' });
      } else {
        console.log(nomUsu.value,password.value);
        apiService.post('/tokens', {
          username: nomUsu.value,
          password: password.value
        })
          .then(function (response) {
            router.push({ name: "ClientHome" });
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            ValError.value = error.response.data.context.Message;
            hasError.value = true;
          })
      }

    }
  };

  return {
    makeLogin,
    nomUsu,
    password,
    hasError,
    errorDatos
  };
}
