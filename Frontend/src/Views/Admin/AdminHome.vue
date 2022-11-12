<template>
  <div class="AdminHome">
    <div>
      <div class="row">
        <div id="menu" class="col-sm-3 ">
          <div class="d-flex flex-column flex-shrink-0 p-3 bg-light" style="width: 280px;">
            <hr>
            <ul class="nav nav-pills flex-column mb-auto">
              <li>
                <a @click="vPiloto ()" style="cursor:pointer;" class="nav-link link-dark bot">
                  <svg class="bi me-2" width="16" height="30">
                  </svg>
                  Pilotos
                </a>
              </li>
              <li>
                <a @click="vAeropuertos()" style="cursor:pointer;" class="nav-link link-dark bot">
                  <svg class="bi me-2" width="16" height="30">
                  </svg>
                  Aeropuertos
                </a>
              </li>
              <li>
                <a @click="vAviones ()" style="cursor:pointer;" class="nav-link link-dark bot">
                  <svg class="bi me-2" width="16" height="30">
                  </svg>
                  Aviones
                </a>
              </li>
              <li>
                <a @click="vVentasHora()" style="cursor:pointer;" class="nav-link link-dark bot">
                  <svg class="bi me-2" width="16" height="30">
                  </svg>
                  Graficas
                </a>
              </li>
            </ul>
            <hr>
            <div class="dropdown">
              <a href="#" class="d-flex align-items-center text-dark text-decoration-none dropdown-toggle"
                id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                <img src="https://cdn-icons-png.flaticon.com/512/456/456212.png" alt="" width="32" height="32"
                  class="rounded-circle me-2">
                <strong>NombreUsuario</strong>
              </a>
              <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                <li><a @click="vPerfil()" style="cursor:pointer;" class="dropdown-item" >Perfil</a></li>
                <li>
                  <hr class="dropdown-divider">
                </li>
                <li><a class="dropdown-item" href="#">Cerrar Sesión</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div id="cont" class="col-sm-8">
          <grafica-ventas v-if="ventanaVentasHora" />
          <pilotos v-if="ventanaPilotos" />
          <Aeropuertos v-if="ventanaAero" />
          <Aviones v-if="ventanaAviones"/>
          <div class="perfil" v-if="ventanaPerfil">
            <ModPerfil :tipoEmpleado="false" :titulo="tit" />
            <div class="text-center">
                <br>
                <button v-if="!modperfil" v-on:click="modperfil=true" class=" btn  btn-primary tx-tfm">Modificar</button>
                <button v-if="modperfil" v-on:click="modperfil=false" class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                <button v-if="modperfil" v-on:click="ValRegistro()" class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GraficaVentas from './Components/GraficaVentas';
import Pilotos from './Components/Pilotos.vue';
import Aeropuertos from './Components/Aeropuertos';
import Aviones from './Components/Aviones';
import ModPerfil from '../Login/Components/Registro';

export default {
  name: 'Admin-v',
  components:
  {
    GraficaVentas,
    Pilotos,
    Aeropuertos,
    Aviones,
    ModPerfil
  },
  data: () => ({
    tit: "Información del perfil",
    ventanaVentasHora: false,
    ventanaPilotos: true,
    ventanaAero: false,
    ventanaAviones: false,
    ventanaPerfil: false,
    modperfil: false
  }),
  methods: {
    vVentasHora() {
      this.ventanaVentasHora = true;
      this.ventanaPilotos = false;
      this.ventanaAero = false;
      this.ventanaAviones = false;
      this.ventanaPerfil = false;
    },
    vPiloto() {
      this.ventanaVentasHora = false;
      this.ventanaPilotos = true;
      this.ventanaAero = false;
      this.ventanaAviones = false;
      this.ventanaPerfil = false;
    },
    vAeropuertos() {
      this.ventanaVentasHora = false;
      this.ventanaPilotos = false;
      this.ventanaAero = true;
      this.ventanaAviones = false;
      this.ventanaPerfil = false;
    },
    vAviones() {
      this.ventanaVentasHora = false;
      this.ventanaPilotos = false;
      this.ventanaAero = false;
      this.ventanaAviones = true;
      this.ventanaPerfil = false;
    },
    vPerfil() {
      this.ventanaVentasHora = false;
      this.ventanaPilotos = false;
      this.ventanaAero = false;
      this.ventanaAviones = false;
      this.ventanaPerfil = true;
    }
  }
};
</script>

<style lang="scss">
.bot:hover {
  background-color: #007bff;
}
.perfil{
  text-align: left;
}
#menu {
  height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #460ee0;
}
</style>
