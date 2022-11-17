import { ref } from 'vue';
import apiService from '@/services/ApiService';

// eslint-disable-next-line
export function useCliente() {
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

     return{
        AeroPuertosO,
        AeroPuertosD,
        GetAllAeroPuertosD,
        GetAllAeroPuertosO
     }
}
