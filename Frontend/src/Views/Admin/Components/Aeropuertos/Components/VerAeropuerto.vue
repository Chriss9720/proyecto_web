<template>
    <div>
        <section class="vh-95">
            <div class="container py-4 h-95">
                <div class="myformR">
                    <form class="alinear">
                        <div class="logo mb-3">
                            <div class="col-md-12 text-center">
                                <h2>Información del aeropuerto</h2>
                            </div>
                        </div>
                        <div class="col-md-12 ">
                            <div class="login-or">
                                <hr class="hr-or">
                            </div>
                        </div>
                        <div class="form-outline mb-4">
                            <div class="row">
                                <div class="col">
                                    <label class="form-label">Selecciona el pais:</label>
                                    <select class="form-select btn btn-primary border" v-model="busPais"
                                        v-on:change="cambio(busPais)" :disabled="modAeropuerto">
                                        <option v-for="i of paises" v-bind:key="i" :value="i.id">{{ i.name }}</option>
                                    </select>

                                </div>
                                <div class="col">
                                    <label class="form-label">Selecciona el estado:</label>
                                    <select class="form-select btn btn-primary border" v-model="busCiudad"
                                        v-on:change="cambioCiudad(busCiudad)" :disabled="modAeropuerto">
                                        <option v-for="i of ciudades" v-bind:key="i" :value="i.id">{{ i.name }}</option>
                                    </select>

                                </div>
                            </div>

                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form6Example4">Nombre:</label>
                            <input :disabled="modAeropuerto" v-model="nombre" type="text" id="form6Example4"
                                class="form-control" />

                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label">Dirección:</label>
                            <input :disabled="modAeropuerto" v-model="direccion" type="text" class="form-control" />
                        </div>
                        <div class="form-outline mb-4 ">
                            <label class="form-label">Código postal:</label>
                            <input :disabled="modAeropuerto" v-model="codigoPostal" type="text" class="form-control" />
                        </div>
                        <div class="text-center">
                            <br>
                            <h4 v-if="correcto" class="text-success">Registro exitoso</h4>
                            <h4 v-if="Error" class="text-danger">{{ ValError }}</h4>
                            <h4 v-if="ErrorDatos" class="text-danger">!Ingrese todos los datos¡</h4>
                            <button v-on:click="vCancelar()" v-if="!correcto"
                                class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                            <button v-on:click="vCancelar()" v-if="correcto"
                                class=" btn btn-block mybtn btn-primary tx-tfm">Volver</button>
                            <button v-on:click="ActualizarAeroPuerto($route.params.idUsuario)" v-if="!correcto"
                                class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
                        </div>
                    </form>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import { useUpdateAeroPuerto } from '../Composables/UseUpdateAeropuerto';
import { useAddAeropuerto } from '../Composables/UseAddAeropuerto';

export default {
    name: "Ver-AeroPuerto",
    data: () => ({
        busPais: "Selecciona un pais",
        busCiudad: "Selecciona el estado",
        modAeropuerto: true
    }),
    setup() {
        const {
            nombre,
            ciudad,
            direccion,
            codigoPostal,
            ActualizarAeroPuerto,
            correcto,
            Error,
            ErrorDatos,
            ValError,
            GetAeroPuerto,
            AeroPuerto
        } = useUpdateAeroPuerto();
        const {
            getPaises,
            paises,
            getCiudades,
            ciudades
        } = useAddAeropuerto();
        return {
            nombre,
            ciudad,
            direccion,
            codigoPostal,
            ActualizarAeroPuerto,
            correcto,
            Error,
            ErrorDatos,
            ValError,
            GetAeroPuerto,
            AeroPuerto,
            getPaises,
            paises,
            getCiudades,
            ciudades
        };
    },
    created() {
        this.getPaises(this.$route.params.idUsuario);
        this.GetAeroPuerto(this.$route.params.idUsuario, this.$route.params.idAeropuerto);
    },
    methods: {
        vCancelar() {
            this.$router.go(-1);
        },
        cambio(busPais) {
            this.getCiudades(this.$route.params.idUsuario, busPais);
        },
        cambioCiudad(busCiudad) {
            this.ciudad = busCiudad;
        }
    }

}
</script>

<style >
.alinear {
    text-align: left;
}

.myformR {
    margin: auto;
    padding: 1rem;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 80%;
    pointer-events: auto;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, .2);
    border-radius: 1.1rem;
    text-align: left;
}
</style>