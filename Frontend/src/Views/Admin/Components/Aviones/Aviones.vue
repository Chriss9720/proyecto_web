<template>
    <div class="Avion">
        <div v-if="verAviones">
            <h2>Aviones</h2>
            <div>
                <div class="row">
                    <div class="col">
                        <button id="btnAgregar" class="btn btn-primary border"
                            @click="this.$router.push({ name: 'AddAvion', params: { idUsuario } })">Agregar</button>
                    </div>
                </div>
            </div>
            <div class="contenedor">
                <div class="table-responsive">
                    <table class="table table-hover table-bordered">
                        <thead>
                            <tr>
                                <th>Capacidad pasajeros</th>
                                <th>Capacidad equipaje</th>
                                <th>Origen</th>
                                <th>Destino</th>
                                <th>Escalas</th>
                                <th>Salida</th>
                                <th>LLegada</th>
                                <th>Filas</th>
                                <th>Estado</th>
                            </tr>
                        </thead>
                        <tbody v-for="i of Aviones" v-bind:key="i">
                            <tr>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.cap_max_pasajeros}}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.cap_max_equipaje_kilos }}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.origen_id }}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.destino_id }}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.escalas }}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.salida }}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.llegada }}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.filas }}</td>
                                <td @click="VerAvion(idUsuario, i.id)">{{ i.estado }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useVerAviones } from './Composables/UseVerAvion';

export default {
    name: "Aviones-v",
    data: () => ({
        verAviones: true,
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
            Aviones,
            GetAllAviones,
            DeleteAviones
        } = useVerAviones();
        return {
            Aviones,
            GetAllAviones,
            DeleteAviones
        };
    },
    created() {
        this.GetAllAviones(this.idUsuario);
    },
    methods: {
        VerAvion(idUsuario, idAvion) {
            this.$router.push({ name: 'VerAvion', params: { idUsuario, idAvion } })
        },
        eliminarAvion(idUsuario, idAvion) {
            if (confirm("Esta seguro de eliminar el Avion?")) {
                this.DeleteAviones(idUsuario, idAvion);
            }
        },
        cambio(filtroselec) {
            this.datoBuscar="";
            if(filtroselec == 'Todos'){
                this.verTodos = true;
                this.GetAllAviones(this.idUsuario);
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