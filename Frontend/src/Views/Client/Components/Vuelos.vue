<template>
    <div class="vuelos">
        <section class="vh-95">
            <div class="container py-4 h-95 bg-secondary ">
                <div class="myformR ">
                    <h2>¡Vuelos disponibles! </h2>
                    <div class="container">
                        <img src="@/assets/mapag.gif" />
                    </div>
                    <h4>¡Mira las opciones que tenemos para esa ruta y elige el que mejor te convenga! </h4>
                    <div class="container ">
                        <div class="row border " style="cursor:pointer;" @click="$router.push({ name: 'CompraBoletos'});">
                            <div class="col">
                                <p> Origen: Aeropuerto de ciudad de Mexico</p>
                                <p> Destino: Aeropuerto cubano</p>
                            </div>
                            <div class="col">
                                <p> 1/12/2022 10:00:00</p>
                                <p> 1/12/2022 12:00:00</p>
                            </div>
                        </div>
                        <br>
                        <div class="row border " style="cursor:pointer;" @click="$router.push({ name: 'CompraBoletos'});">
                            <div class="col">
                                <p> Origen: Aeropuerto de ciudad de Mexico</p>
                                <p> Destino: Aeropuerto cubano</p>
                            </div>
                            <div class="col">
                                <p> 5/12/2022 09:00:00</p>
                                <p> 5/12/2022 11:00:00</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    name: "vuelos-v"
}
</script>

<style >
.myformR {
    margin: auto;
    padding: 1rem;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 90%;
    pointer-events: auto;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, .2);
    border-radius: 1.1rem;
}
</style>