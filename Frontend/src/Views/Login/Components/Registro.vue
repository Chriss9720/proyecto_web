<template>
    <div>
        <form>
            <div class="logo mb-3">
                <div class="col-md-12 text-center">
                    <h2>{{titulo}}</h2>
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
            <div class="form-check form-switch" v-if="tipoEmpleado">
                <input class="form-check-input" type="checkbox">
                <label class="form-check-label" for="mySwitch">¿Cuenta de empleado?</label>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "Registro-v",
    props: {
        titulo: {
            type: String,
            default: "Registro de usuario"
        },
        tipoEmpleado: {
            type: Boolean,
            default: true
        }
    }
}
</script>