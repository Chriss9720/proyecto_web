<template>
    <div>
        <section class="vh-95">
            <div class="container py-4 h-95">
                <div class="myformR">
                    <form class="alinear">
                        <div class="logo mb-3">
                            <div class="col-md-12 text-center">
                                <h2>Agregar Piloto</h2>
                            </div>
                        </div>
                        <div class="col-md-12 ">
                            <div class="login-or">
                                <hr class="hr-or">
                            </div>
                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label">Nombre:</label>
                            <input v-model="nombre" type="text" class="form-control" />

                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form6Example4">Edad:</label>
                            <input v-model="edad" type="text" id="form6Example4" class="form-control" />

                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label">Experiencia:</label>
                            <input v-model="experiencia" type="text" class="form-control" />
                        </div>
                        <div class="form-outline mb-4 ">
                            <label class="form-label">Vuelos: 0 </label>
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
                            <button v-on:click="RegistrarPiloto($route.params.idUsuario)" v-if="!correcto"
                                class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
                        </div>
                    </form>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import { useAddPiloto } from '../Composables/UseAddPiloto';

export default {
    name: "Add-Piloto",
    setup() {
        const {
            nombre,
            edad,
            experiencia,
            RegistrarPiloto,
            correcto,
            Error,
            ErrorDatos,
            ValError
        } = useAddPiloto();

        return {
            nombre,
            edad,
            experiencia,
            RegistrarPiloto,
            correcto,
            Error,
            ErrorDatos,
            ValError
        };
    },
    methods: {
        vCancelar() {
            this.$router.go(-1);
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