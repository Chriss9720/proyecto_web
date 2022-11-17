<template>
    <div>
        <section class="vh-95">
            <div class="container py-4 h-95">
                <div class="myformR">
                    <form class="alinear">
                        <div class="logo mb-3">
                            <div class="col-md-12 text-center">
                                <h2>Agregar Avión</h2>
                            </div>
                        </div>
                        <div class="col-md-12 ">
                            <div class="login-or">
                                <hr class="hr-or">
                            </div>
                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form6Example4">Capacidad de pasajeros:</label>
                            <input v-model="cap_max_pasajeros" type="Number" id="form6Example4" class="form-control" />
                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form6Example4">Capacidad de equipaje en kilos: </label>
                            <input v-model="cap_max_equipaje_kilos" type="Number" id="form6Example4"
                                class="form-control" />
                        </div>
                        <div class="form-outline mb-4">
                            <div class="row">
                                <div class="col">
                                    <label class="form-label" for="form6Example4">Seleccione el origen: </label>
                                </div>
                                <div class="col">
                                    <div>
                                        <select class="form-select btn btn-primary border" v-model="busPaisO"
                                            v-on:change="cambioO(busPaisO)">
                                            <option v-for="i of AeroPuertosO" v-bind:key="i" :value="i.id">{{
                                                    i.direccion
                                            }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <br>
                        <div class="form-outline mb-4">
                            <div class="row">
                                <div class="col">
                                    <label class="form-label" for="form6Example4">Seleccione el destino: </label>
                                </div>
                                <div class="col">
                                    <div>
                                        <select class="form-select btn btn-primary border" v-model="busPaisD"
                                            v-on:change="cambioD(busPaisD)">
                                            <option v-for="i of AeroPuertosD" v-bind:key="i" :value="i.id">{{
                                                    i.direccion
                                            }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <br>
                        <label for="start">Salida:</label>
                        <input v-model="salida" type="date" id="start" name="trip-start">
                        <label for="start">LLegada:</label>
                        <input v-model="llegada" type="date" id="start" name="trip-start">
                        <br>
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form6Example4">Filas:</label>
                            <input v-model="filas" type="Number" id="form6Example4" class="form-control" />
                        </div>
                        <div class="form-outline mb-4 ">
                            <label class="form-label">Estado: En espera</label>
                        </div>
                        <div>
                            <div class="row">
                                <div class="col-3">
                                    <p>Seleccione el piloto:</p>
                                </div>
                                <div class="col-8"><select class="form-select btn btn-primary border"
                                        v-model="piloto_id" style="width: 200px">
                                        <option v-for="i of pilotos" v-bind:key="i" :value="i.id">{{ i.nombre }}
                                        </option>
                                    </select></div>
                            </div>
                        </div>
                    </form>
                    <div class="text-center">
                        <br>
                        <h4 v-if="correcto" class="text-success">Registro exitoso</h4>
                        <h4 v-if="Error" class="text-danger">{{ ValError }}</h4>
                        <h4 v-if="ErrorDatos" class="text-danger">!Ingrese todos los datos¡</h4>
                        <button v-on:click="vCancelar()" v-if="!correcto"
                            class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                        <button v-on:click="vCancelar()" v-if="correcto"
                            class=" btn btn-block mybtn btn-primary tx-tfm">Volver</button>
                        <button @click.prevent="RegistrarAeroPuerto($route.params.idUsuario)" v-if="!correcto"
                            class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import { useAddAvion } from '../Composables/UseAddAvion';
import { useVerPiloto } from '../../Piloto/Composables/UseVerPilotos';

export default {
    name: "Add-AeroPuerto",
    data: () => ({
        busPaisO: "Selecciona un pais",
        busPaisD: "Selecciona un pais",
        busCiudadO: "Selecciona el estado",
        busCiudadD: "Selecciona el estado",
        buspiloto: "Selecciona el piloto"
    }),
    setup() {
        const {
            cap_max_pasajeros,
            cap_max_equipaje_kilos,
            origen_id,
            destino_id,
            salida,
            llegada,
            filas,
            piloto_id,
            RegistrarAeroPuerto,
            correcto,
            Error,
            ErrorDatos,
            ValError,
            AeroPuertosO,
            AeroPuertosD,
            GetAllAeroPuertosD,
            GetAllAeroPuertosO
        } = useAddAvion();
        const {
            pilotos,
            GetAllPilotos
        } = useVerPiloto();
        return {
            pilotos,
            GetAllPilotos,
            cap_max_pasajeros,
            cap_max_equipaje_kilos,
            origen_id,
            destino_id,
            salida,
            llegada,
            filas,
            piloto_id,
            RegistrarAeroPuerto,
            correcto,
            Error,
            ErrorDatos,
            ValError,
            AeroPuertosO,
            AeroPuertosD,
            GetAllAeroPuertosD,
            GetAllAeroPuertosO
        };
    },
    created() {
        this.GetAllPilotos(this.$route.params.idUsuario);
        this.GetAllAeroPuertosD(this.$route.params.idUsuario);
        this.GetAllAeroPuertosO(this.$route.params.idUsuario);
    },
    methods: {
        vCancelar() {
            this.$router.go(-1);
        },
        cambioD(id) {
            this.destino_id = id;
        },
        cambioO(id) {
            this.origen_id = id;
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