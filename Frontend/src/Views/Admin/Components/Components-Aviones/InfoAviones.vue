<template>
    <div>
        <form class="alinear">
            <div class="logo mb-3">
                <div class="col-md-12 text-center">
                    <h2>{{ titulo }}</h2>
                </div>
            </div>
            <div class="col-md-12 ">
                <div class="login-or">
                    <hr class="hr-or">
                </div>
            </div>
            <div class="form-outline mb-4">
                <label class="form-label">Folio:</label>
                <input type="text" class="form-control" />

            </div>
            <div class="form-outline mb-4">
                <label class="form-label" for="form6Example4">Capacidad pasajeros:</label>
                <input type="Number" id="form6Example4" class="form-control" />
            </div>
            <div class="form-outline mb-4">
                <label class="form-label" for="form6Example4">Capacidad equipaje: </label>
                <input type="Number" id="form6Example4" class="form-control" />
            </div>
            <div class="dropdown">
                <label class="form-label" for="form6Example4">Seleccione el origen: </label>
                <button type="button" class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown">
                    Origen
                </button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Link 1</a></li>
                    <li><a class="dropdown-item" href="#">Link 2</a></li>
                    <li><a class="dropdown-item" href="#">Link 3</a></li>
                </ul>
            </div>
            <br>
            <div class="dropdown">
                <label class="form-label" for="form6Example4">Seleccione el destino:</label>
                <button type="button" class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown">
                    Destino
                </button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Link 1</a></li>
                    <li><a class="dropdown-item" href="#">Link 2</a></li>
                    <li><a class="dropdown-item" href="#">Link 3</a></li>
                </ul>
            </div>
            <br>
            <div class="form-check form-switch" v-if="tipoEmpleado">
                <input class="form-check-input" type="checkbox">
                <label class="form-check-label" for="mySwitch">¿Escalas?</label>
            </div>
            <label for="start">Salida:</label>

            <input type="date" id="start" name="trip-start" value="2022-11-04" >
            <label for="start">LLegada:</label>

            <input type="date" id="start" name="trip-start" value="2022-11-04">
            <br>
            <div class="form-outline mb-4">
                <label class="form-label" for="form6Example4">Filas:</label>
                <input type="Number" id="form6Example4" class="form-control" />
            </div>
            <div class="form-outline mb-4">
                <label class="form-label" for="form6Example4">Columnas:</label>
                <input type="Number" id="form6Example4" class="form-control" />
            </div>
            <div class="form-outline mb-4 ">
                <label class="form-label">Estado:</label>
                <input type="text" class="form-control" />
            </div>
            <div class="dropdown">
                <button type="button" class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown">
                    Piloto
                </button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Link 1</a></li>
                    <li><a class="dropdown-item" href="#">Link 2</a></li>
                    <li><a class="dropdown-item" href="#">Link 3</a></li>
                </ul>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "Info-Aeropuerto",
    props: {
        titulo: {
            type: String,
            default: "Aeropuerto"
        }
    },

}
</script>

<style >
.alinear {
    text-align: left;
}
</style>