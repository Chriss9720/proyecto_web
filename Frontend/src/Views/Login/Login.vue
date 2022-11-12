<template>
  <div class="login">
    <section class="vh-95">
      <div class="container py-4 h-95">
        <div class="row d-flex align-items-center justify-content-center h-95">
          <div class="col-md-6" v-if="vlogin">
            <img src="@/assets/LoginImg.png" alt="" class="img-fluid" />
          </div>
          <div class="col-md-5 mx-auto" v-if="vlogin">
            <div class="myform form ">
              <div class="logo mb-3">
                <div class="col-md-12 text-center">
                  <h1>Inicio de sesión</h1>
                </div>
              </div>
              <form @submit.prevent="makeLogin">
                <div class="form-group">
                  <label>Correo eléctronico</label>
                  <input v-model="clientId" type="email" name="email" class="form-control" id="email"
                    placeholder="Ingresar email">
                </div>
                <div class="form-group">
                  <label>Constraseña</label>
                  <input type="password" name="password" id="password" class="form-control"
                    placeholder="Ingresar contraseña">
                </div>
                <div class="col-md-12 text-center ">
                  <br>
                  <button class=" btn btn-block mybtn btn-primary tx-tfm">Ingresar</button>
                </div>
                <div class="col-md-12 ">
                  <div class="login-or">
                    <hr class="hr-or">
                  </div>
                </div>
              </form>
              <div class="form-group">
                <p class="text-center">¿No tienes una cuenta? <button class="registro"
                    v-on:click="Registrarse()">¡Registrate aqui!</button></p>
              </div>
            </div>
          </div>
          <div class="col-md-8 mx-auto" v-if="vregistro">
            <div class="myformR">
              <Registro-Usuario :tipoEmpleado="true" :titulo="tit" />
              <div class="text-center">
                <br>
                <h2 v-if="valregistro" class="text-success">Registro exitoso</h2>
                <button v-on:click="cancelar()" class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                <button v-on:click="ValRegistro()" class=" btn btn-block mybtn btn-primary tx-tfm">Registrarse</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { useLogin } from "./Composables/UseLogin";
import RegistroUsuario from "./Components/Registro.vue";

export default {
  name: 'Login-v',
  data: () => ({
    tit: "Registro de usuario",
    vlogin: true,
    vregistro: false,
    valregistro: false
  }),
  components: {
    RegistroUsuario
  },
  setup() {
    const {
      makeLogin,
      clientId,
      hasError
    } = useLogin();

    return {
      clientId,
      makeLogin,
      hasError
    };
  },
  methods: {
    Registrarse() {
      this.vlogin = false;
      this.vregistro = true;
    },
    cancelar() {
      this.vlogin = true;
      this.vregistro = false;
    },
    ValRegistro() {
      this.valregistro = true;
    }
  },
};
</script>

<style>
h1,
h2,
h3 {
  font-family: 'Kaushan Script', cursive;
}

.registro {
  cursor: pointer;
  border: 0px solid #3498db;
  background-color: transparent;
  color: #3498db;
  font-size: 1em;
  text-decoration: underline;
}

.myformR {

  padding: 1rem;
  -ms-flex-direction: column;
  flex-direction: column;
  width: 100%;
  pointer-events: auto;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, .2);
  border-radius: 1.1rem;
  text-align: left;
}

.myform {
  position: relative;
  display: -ms-flexbox;
  display: flex;
  padding: 1rem;
  -ms-flex-direction: column;
  flex-direction: column;
  width: 100%;
  pointer-events: auto;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, .2);
  border-radius: 1.1rem;
  outline: 0;
}

.tx-tfm {
  text-transform: uppercase;
}

.mybtn {
  border-radius: 50px;
  width: 300px;
}
</style>
