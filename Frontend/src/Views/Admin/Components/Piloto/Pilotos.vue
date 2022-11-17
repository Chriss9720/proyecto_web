<template>
    <div class="Piloto">
        <div v-if="verPilotos">
            <h2>Pilotos</h2>
            <div>
                <div class="row">
                    <div class="col input-group">
                        <input v-model="datoBuscar" v-if="!verTodos" type="text" class="form-control "
                            placeholder="Buscar">
                        <select class="form-select btn btn-primary border" v-model="filtroselec"
                            v-on:change="cambio(filtroselec)">
                            <option selected>Todos</option>
                            <option value="Nombre">Nombre</option>
                            <option value="Experiencia">Experiencia</option>
                            <option value="Vuelos">Vuelos</option>
                        </select>
                        <button @click="VerPilotoFiltrado(idUsuario, filtroselec, datoBuscar)" v-if="!verTodos" class="btn btn-primary border" type="submit">Buscar</button>
                    </div>
                    <div class="col">
                        <button id="btnAgregar" class="btn btn-primary border"
                            @click="this.$router.push({ name: 'AddPiloto', params: { idUsuario } })">Agregar</button>
                    </div>
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
                        <tbody v-for="i of pilotos" v-bind:key="i">
                            <tr>
                                <td @click="VerPiloto(idUsuario, i.id)">{{ i.nombre }}</td>
                                <td @click="VerPiloto(idUsuario, i.id)">{{ i.edad }}</td>
                                <td @click="VerPiloto(idUsuario, i.id)">{{ i.experiencia }}</td>
                                <td @click="VerPiloto(idUsuario, i.id)">{{ i.total_vuelos }}</td>
                                <td @click="eliminarPiloto(idUsuario, i.id)"><img
                                        src="https://cdn-icons-png.flaticon.com/512/3221/3221845.png"
                                        style="cursor:pointer;" alt="" width="25" height="25"
                                        class="rounded-circle me-2"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useVerPiloto } from './Composables/UseVerPilotos';

export default {
    name: "Pilotos-v",
    data: () => ({
        verPilotos: true,
        verInfo: false,
        verTodos: true,
        filtroselec: "Todos",
        datoBuscar: ""
    }),
    props: {
        idUsuario: {
            type: String,
            default: ""
        }
    },
    setup() {
        const {
            pilotos,
            GetAllPilotos,
            DeletePiloto,
            VerPilotoFiltrado
        } = useVerPiloto();
        return {
            pilotos,
            GetAllPilotos,
            DeletePiloto,
            VerPilotoFiltrado
        };
    },
    created() {
        this.GetAllPilotos(this.idUsuario);
    },
    methods: {
        VerPiloto(idUsuario, idPiloto) {
            this.$router.push({ name: 'VerPiloto', params: { idUsuario, idPiloto } })
        },
        eliminarPiloto(idUsuario, idPiloto) {
            if (confirm("Esta seguro de eliminar el piloto?")) {
                this.DeletePiloto(idUsuario, idPiloto);
                this.GetAllPilotos(this.idUsuario);
            }
        },
        cambio(filtroselec) {
            this.datoBuscar="";
            if(filtroselec == 'Todos'){
                this.verTodos = true;
                this.GetAllPilotos(this.idUsuario);
            }else{
                this.verTodos = false;
            }
        }
    }
}
</script>

<style>
h2 {
    font-family: 'Kaushan Script', cursive;
}

#btnAgregar {
    float: right;
}
</style>