<template>
    <div class="Aviones">
        <div v-if="verAvioness">
            <h2>Avioness</h2>
            <div class="float-right col-sm-6">
                <div class="input-group mb-4">
                    <input type="text" class="form-control " placeholder="Buscar">
                    <button class="btn btn-primary border" type="submit">Buscar</button>
                    <button class="btn btn-primary border" @click="vAddAviones">Agregar</button>
                </div>
            </div>
            <div class="contenedor">
                <div class="table-responsive">
                    <table class="table table-hover table-bordered">
                        <thead>
                            <tr>
                                <th>Folio</th>
                                <th>Capacidad pasajeros</th>
                                <th>Capacidad equipaje</th>
                                <th>Origen</th>
                                <th>Destino</th>
                                <th>Escalas</th>
                                <th>Salida</th>
                                <th>LLegada</th>
                                <th>Filas</th>
                                <th>Columnas</th>
                                <th>Estado</th>
                                <th>Aviones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
                                <td @click="vInfoAviones()">info</td>
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
            <InfoAviones :titulo="titMod" :cantvuelos="vuelos" />
            <div class="text-center">
                <br>
                <button v-if="!modAviones" v-on:click="vCancelar()"
                    class="btn btn-block mybtn btn-primary tx-tfm">Volver</button>
                <button v-if="!modAviones" v-on:click="modAviones = true"
                    class=" btn btn-block mybtn btn-primary tx-tfm">Modificar</button>
                <button v-if="modAviones" v-on:click="modAviones = false, vCancelar()"
                    class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                <button v-if="modAviones" v-on:click="ValRegistro()"
                    class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
            </div>
        </div>
        <div v-if="veraddAviones">
            <InfoAviones :titulo="titAdd" :cantvuelos="vuelos" />
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
import InfoAviones from './Components-Aviones/InfoAviones';

export default {
    name: "Aviones-v",
    components: {
        InfoAviones
    },
    data: () => ({
        verAvioness: true,
        verInfo: false,
        titMod: "Información del Aviones",
        titAdd: "Agregar Aviones",
        vuelos: 10,
        modAviones: false,
        veraddAviones: false
    }),
    methods: {
        vInfoAviones() {
            this.verAvioness = false;
            this.verInfo = true;
            this.veraddAviones = false;
        },
        vAddAviones() {
            this.verAvioness = false;
            this.verInfo = false;
            this.veraddAviones = true;
        },
        vCancelar() {
            this.verAvioness = true;
            this.verInfo = false;
            this.veraddAviones = false;
        }
    }
}
</script>

<style>
h2 {
    font-family: 'Kaushan Script', cursive;
}
.mybtn {
  border-radius: 50px;
  width: 300px;
}
</style>
