<template>
    <div>
        <form class="alinear">
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
            <div class="form-outline mb-4">
                <label class="form-label">Nombre:</label>
                <input type="text" class="form-control" />

            </div>
            <div class="form-outline mb-4">
                <label class="form-label" for="form6Example4">Edad:</label>
                <input type="text" id="form6Example4" class="form-control" />

            </div>
            <div class="form-outline mb-4">
                <label class="form-label">Experiencia:</label>
                <input type="text" class="form-control" />
            </div>
            <div class="form-outline mb-4 ">
                <label class="form-label">Vuelos: 0 </label>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "Info-Piloto",
    props: {
        titulo: {
            type: String,
            default: "Registro de usuario"
        },
        cantvuelos: {
            tye: Number,
            default: 0
        }
    },
    
}
</script>

<style >
.alinear{
    text-align: left;
}
</style>