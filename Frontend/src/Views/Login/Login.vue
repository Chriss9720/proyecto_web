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
                  <label>Nombre de usuario</label>
                  <input v-model="nomUsu" type="text"  class="form-control" 
                    placeholder="Ingresar usuario">
                </div>
                <div class="form-group">
                  <label>Constraseña</label>
                  <input v-model="password"  type="password" name="password" id="password" class="form-control"
                    placeholder="Ingresar contraseña">
                </div>
                <div class="col-md-12 text-center ">
                  <br>
                  <p v-if="errorDatos" class="text-danger">!Ingrese todos los datos¡</p>
                  <button class=" btn btn-block mybtn btn-primary tx-tfm">Ingresar</button>
                </div>
                <div class="col-md-12 ">
                  <div class="login-or">
                    <hr class="hr-or">
                  </div>
                </div>
              </form>
              <div class="form-group">
                <p class="text-center">¿No tienes una cuenta? <router-link :to="{ name: 'Registro' }">¡Registrate aqui!
                  </router-link>
                </p>
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

export default {
  name: 'Login-v',
  data: () => ({
    tit: "Registro de usuario",
    vlogin: true
  }),
  setup() {
    const {
      makeLogin,
      nomUsu,
      password,
      hasError,
      errorDatos
    } = useLogin();

    return {
      nomUsu,
      makeLogin,
      password,
      hasError,
      errorDatos
    };
  }
};
</script>

<style>
h1,
h2,
h3 {
  font-family: 'Kaushan Script', cursive;
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
