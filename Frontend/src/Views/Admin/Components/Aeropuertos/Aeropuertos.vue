<template>
    <div class="AeroPuerto">
        <div v-if="verAeroPuertos">
            <h2>AeroPuertos</h2>
            <div>
                <div class="row">
                    <div class="col">
                        <button id="btnAgregar" class="btn btn-primary border"
                            @click="this.$router.push({ name: 'AddAeroPuerto', params: { idUsuario } })">Agregar</button>
                    </div>
                </div>
            </div>
            <div class="contenedor">
                <div class="table-responsive">
                    <table class="table table-hover table-bordered">
                        <thead>
                            <tr>
                                <th>Nombre</th>
                                <th>Dirección</th>
                                <th>Código postal</th>
                            </tr>
                        </thead>
                        <tbody v-for="i of AeroPuertos" v-bind:key="i">
                            <tr>
                                <td @click="VerAeroPuerto(idUsuario, i.id)">{{ i.nombre }}</td>
                                <td @click="VerAeroPuerto(idUsuario, i.id)">{{ i.direccion}}</td>
                                <td @click="VerAeroPuerto(idUsuario, i.id)">{{ i.codigo_postal }}</td>
                                <td @click="eliminarAeroPuerto(idUsuario, i.id)"><img
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
import { useVerAeropuerto } from './Composables/UseVerAeropuerto';

export default {
    name: "AeroPuertos-v",
    data: () => ({
        verAeroPuertos: true,
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
            AeroPuertos,
            GetAllAeroPuertos,
            DeleteAeroPuerto
        } = useVerAeropuerto();
        return {
            AeroPuertos,
            GetAllAeroPuertos,
            DeleteAeroPuerto
        };
    },
    created() {
        this.GetAllAeroPuertos(this.idUsuario);
    },
    methods: {
        VerAeroPuerto(idUsuario, idAeropuerto) {
            this.$router.push({ name: 'VerAeropuerto', params: { idUsuario, idAeropuerto } })
        },
        eliminarAeroPuerto(idUsuario, idAeroPuerto) {
            if (confirm("Esta seguro de eliminar el AeroPuerto?")) {
                this.DeleteAeroPuerto(idUsuario, idAeroPuerto);
            }
        },
        cambio(filtroselec) {
            this.datoBuscar="";
            if(filtroselec == 'Todos'){
                this.verTodos = true;
                this.GetAllAeroPuertos(this.idUsuario);
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