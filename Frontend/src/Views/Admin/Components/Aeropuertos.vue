<template>
    <div class="Aeropuerto">
        <div v-if="verAeropuertos">
            <h2>Aeropuertos</h2>
            <div class="float-right col-sm-6">
                <div class="input-group mb-4">
                    <input type="text" class="form-control " placeholder="Buscar">
                    <button class="btn btn-primary border" type="submit">Buscar</button>
                    <button class="btn btn-primary border" @click="vAddAeropuerto">Agregar</button>
                </div>
            </div>
            <div class="contenedor">
                <div class="table-responsive">
                    <table class="table table-hover table-bordered">
                        <thead>
                            <tr>
                                <th>Ciudad</th>
                                <th>Nombre</th>
                                <th>Dirección</th>
                                <th>Código postal</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td @click="vInfoAeropuerto()">info</td>
                                <td @click="vInfoAeropuerto()">info</td>
                                <td @click="vInfoAeropuerto()">info</td>
                                <td @click="vInfoAeropuerto()">info</td>
                                <td><img src="https://cdn-icons-png.flaticon.com/512/3221/3221845.png"
                                        style="cursor:pointer;" alt="" width="25" height="25"
                                        class="rounded-circle me-2"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div v-if="verInfo">
            <InfoAeroPuerto :titulo="titMod" :cantvuelos="vuelos" />
            <div class="text-center">
                <br>
                <button v-if="!modAeropuerto" v-on:click="vCancelar()"
                    class="btn btn-block mybtn btn-primary tx-tfm">Volver</button>
                <button v-if="!modAeropuerto" v-on:click="modAeropuerto = true"
                    class=" btn btn-block mybtn btn-primary tx-tfm">Modificar</button>
                <button v-if="modAeropuerto" v-on:click="modAeropuerto = false, vCancelar()"
                    class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                <button v-if="modAeropuerto" v-on:click="ValRegistro()"
                    class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
            </div>
        </div>
        <div v-if="veraddAeropuerto">
            <InfoAeroPuerto :titulo="titAdd" :cantvuelos="vuelos" />
            <div class="text-center">
                <br>
                <h4 class="text-danger">!Ingrese todos los datos¡</h4>
                <button v-on:click="vCancelar()" class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                <button v-on:click="ValRegistro()" class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
            </div>
        </div>
    </div>
</template>

<script>
import InfoAeroPuerto from './Components-Aeropuerto/InfoAeroPuerto';

export default {
    name: "Aeropuertos-v",
    components: {
        InfoAeroPuerto
    },
    data: () => ({
        verAeropuertos: true,
        verInfo: false,
        titMod: "Información del Aeropuerto",
        titAdd: "Agregar Aeropuerto",
        vuelos: 10,
        modAeropuerto: false,
        veraddAeropuerto: false
    }),
    methods: {
        vInfoAeropuerto() {
            this.verAeropuertos = false;
            this.verInfo = true;
            this.veraddAeropuerto = false;
        },
        vAddAeropuerto() {
            this.verAeropuertos = false;
            this.verInfo = false;
            this.veraddAeropuerto = true;
        },
        vCancelar() {
            this.verAeropuertos = true;
            this.verInfo = false;
            this.veraddAeropuerto = false;
        }
    }
}
</script>

<style>
h2 {
    font-family: 'Kaushan Script', cursive;
}
</style>
