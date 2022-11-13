<template>
    <div>
        <section class="vh-95">
            <div class="container py-4 h-95">
                <div class="myformR">
                    <form>
                        <div class="logo mb-3">
                            <div class="col-md-12 text-center">
                                <h2>Registro de usuario</h2>
                            </div>
                        </div>
                        <div class="col-md-12 ">
                            <div class="login-or">
                                <hr class="hr-or">
                            </div>
                        </div>
                        <div class="text-center">
                            <div class="row mb-4">
                                <div class="col">
                                    <div class="form-outline">
                                        <label class="form-label">Nombre:</label>
                                        <input v-model="name" type="text" class="form-control" />

                                    </div>
                                </div>
                                <div class="col">
                                    <div class="form-outline">
                                        <label class="form-label">Apellido Paterno:</label>
                                        <input v-model="apellido_paterno" type="text" class="form-control" />
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="form-outline">
                                        <label class="form-label">Apellido Materno:</label>
                                        <input v-model="apellido_materno" type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label">Correo:</label>
                            <input v-model="correo" type="email" class="form-control" />

                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label" for="form6Example4">Nombre de usuario:</label>
                            <input v-model="nameUsu" type="text" id="form6Example4" class="form-control" />

                        </div>
                        <div class="form-outline mb-4">
                            <label class="form-label">Clave:</label>
                            <input v-model="password" type="email" class="form-control" />
                        </div>
                    </form>
                    <div class="text-center">
                        <br>
                        <h4 v-if="correcto" class="text-success">Registro exitoso</h4>
                        <h4 v-if="Error" class="text-danger">{{ValError}}</h4>
                        <h4 v-if="ErrorDatos" class="text-danger">!Ingrese todos los datos¡</h4>
                        <button v-if="!correcto"  v-on:click="cancelar()"
                            class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
                        <button v-if="!correcto"  v-on:click="RegistrarUsuario()"
                            class=" btn btn-block mybtn btn-primary tx-tfm">Registrarse</button>
                        <button v-if="correcto"  v-on:click="cancelar()"
                            class=" btn btn-block mybtn btn-primary tx-tfm">Iniciar Sesión</button>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import { useRegistro } from "../Composables/UseRegistro";

export default {
    name: "Registro-v",
    setup() {
        const {
            nameUsu,
            name,
            password,
            apellido_paterno,
            apellido_materno,
            correo,
            RegistrarUsuario,
            correcto,
            Error,
            ErrorDatos,
            ValError
        } = useRegistro();

        return {
            nameUsu,
            name,
            password,
            apellido_paterno,
            apellido_materno,
            correo,
            RegistrarUsuario,
            correcto,
            Error,
            ErrorDatos,
            ValError
        };
    },
    methods: {
        cancelar() {
            this.$router.go(-1);
        }
    }
}
</script>

<style scoped>
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