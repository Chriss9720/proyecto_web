<template>
    <div class="Piloto">
        <div v-if="verPilotos">
            <h2>Pilotos</h2>
            <div class="float-right col-sm-6">
                <div class="input-group mb-4">
                    <input type="text" class="form-control " placeholder="Buscar">
                    <button class="btn btn-primary border" type="submit">Buscar</button>
                    <button class="btn btn-primary border" @click="vAddPiloto">Agregar</button>
                </div>
            </div>
            <div class="contenedor">
                <div class="table-responsive">
                    <table class="table table-hover table-bordered">
                        <thead>
                            <tr>
                                <th>Nombre</th>
                                <th>Edad</th>
                                <th>Experiencia</th>
                                <th>Vuelos</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td  @click="vInfoPiloto()">info</td>
                                <td  @click="vInfoPiloto()">info</td>
                                <td  @click="vInfoPiloto()">info</td>
                                <td  @click="vInfoPiloto()">info</td>
                                <td><img src="https://cdn-icons-png.flaticon.com/512/3221/3221845.png" style="cursor:pointer;" alt="" width="25"
                                        height="25" class="rounded-circle me-2" ></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div v-if="verInfo">
            <InfoPiloto :titulo="titMod" :cantvuelos="vuelos"/>
            <div class="text-center">
                <br>
                <button v-if="!modPiloto" v-on:click="vCancelar()" class="btn btn-block mybtn btn-primary tx-tfm">Volver</button>
                <button v-if="!modPiloto" v-on:click="modPiloto=true" class=" btn btn-block mybtn btn-primary tx-tfm">Modificar</button>
                <button v-if="modPiloto" v-on:click="modPiloto=false, vCancelar()" class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                <button v-if="modPiloto" v-on:click="ValRegistro()" class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
            </div>
        </div>
        <div v-if="veraddPiloto">
            <InfoPiloto :titulo="titAdd" :cantvuelos="vuelos"/>
            <div class="text-center">
                <br>
                <h4 class="text-danger">!Ingrese todos los datos¡</h4>
                <button v-on:click="vCancelar()" class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                <button  v-on:click="ValRegistro()" class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
            </div>
        </div>
    </div>
</template>

<script>
import InfoPiloto from './Components-Pilotos/InfoPiloto';

export default {
    name: "Pilotos-v",
    components: {
        InfoPiloto
    },
    data: () => ({
        verPilotos: true,
        verInfo: false,
        titMod: "Información del piloto",
        titAdd: "Agregar piloto",
        vuelos: 10,
        modPiloto: false,
        veraddPiloto: false
    }),
    methods: {
        vInfoPiloto (){
            this.verPilotos= false;
            this.verInfo = true;
            this.veraddPiloto = false;
        },
        vAddPiloto (){
            this.verPilotos= false;
            this.verInfo = false;
            this.veraddPiloto =true;
        },
        vCancelar(){
            this.verPilotos= true;
            this.verInfo = false;
            this.veraddPiloto = false;
        }
    }
}
</script>

<style>
h2 {
    font-family: 'Kaushan Script', cursive;
}
</style>