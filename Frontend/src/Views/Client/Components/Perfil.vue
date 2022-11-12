<template>
    <div class="contenido">
        <form>
            <div class="logo mb-3">
                <div class="col-md-12 text-center">
                    <h2>Mi perfil</h2>
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
                            <input type="text" class="form-control" />

                        </div>
                    </div>
                    <div class="col">
                        <div class="form-outline">
                            <label class="form-label">Apellido Paterno:</label>
                            <input type="text" class="form-control" />
                        </div>
                    </div>
                    <div class="col">
                        <div class="form-outline">
                            <label class="form-label">Apellido Materno:</label>
                            <input type="text" class="form-control" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="cont">
                <div class="form-outline mb-4">
                    <label class="form-label">Correo:</label>
                    <input type="text" class="form-control" />

                </div>
                <div class="form-outline mb-4">
                    <label class="form-label" for="form6Example4">Nombre de usuario:</label>
                    <input type="text" id="form6Example4" class="form-control" />

                </div>
                <div class="form-outline mb-4">
                    <label class="form-label">Clave:</label>
                    <input type="email" class="form-control" />
                </div>
            </div>
        </form>
        <div class="text-center">
            <br>
            <button v-if="!modperfil" v-on:click="volver()" class=" btn btn-block mybtn btn-primary tx-tfm">Volver</button>
            <button v-if="!modperfil" v-on:click="modperfil = true" class=" btn btn-block mybtn btn-primary tx-tfm">Modificar</button>
            <button v-if="modperfil" v-on:click="modperfil = false"
                class=" btn btn-block mybtn btn-primary tx-tfm">Cancelar</button>
            <button v-if="modperfil" v-on:click="ValRegistro()"
                class=" btn btn-block mybtn btn-primary tx-tfm">Guardar</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "Registro-v",
    data: () => ({
    modperfil: false
  }),
  methods: {
    volver() {
        this.$router.go(-1)
    }
  }
}
</script>

<style>
.contenido {
    margin: auto;
    width: 80%;
}

.cont {
    text-align: left;
}
</style>