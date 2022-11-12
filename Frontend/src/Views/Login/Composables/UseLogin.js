import { ref } from 'vue';
import { useRouter } from 'vue-router';

// eslint-disable-next-line
export function useLogin() {
  const router = useRouter();

  const clientId = ref('');
  const hasError = ref(false);

  const makeLogin = async () => {
    if(clientId.value == "admin@gmail.com"){
        router.push({ name: 'AdminHome' });
    }else{
        router.push({name: "ClientHome"});
    }
  };

  return {
    makeLogin,
    clientId,
    hasError
  };
}
