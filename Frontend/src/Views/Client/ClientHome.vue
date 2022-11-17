<template>
    <div class="ClientHome">

        <section class="banner" id="home">
            <div class="container border principal" style="float:right">
                <div class="container my-4">
                    <h1>¡Encuentra el vuelo que necesitas!</h1>
                    <p>Ingresa los siguientes datos para mostrarte nuestros vuelos disponibles</p>
                    <div class="row">
                        <div class="col">
                            Origen
                            <select class="form-select" aria-label="Default select example">
                                <option selected>Open this select menu</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                        </div>
                        <div class="col">
                            Destino
                            <select class="form-select" aria-label="Default select example">
                                <option selected>Open this select menu</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                        </div>
                    </div>
                    <br><br>
                    <button class=" btn btn-block mybtn2 btn-primary tx-tfm">
                        <h1>Buscar Vuelos</h1>
                    </button>
                </div>
            </div>
        </section>

        <section class="secClima" id="clima">
            <div class="container border centroClima" style="float:left">
                <div class="container my-4">
                    <h1>Estado del clima</h1>
                    <p>El clima a veces influye en nuestros planes de viaje, asi que no olvides revisar el clima de los
                        proximos dias</p>
                    <div class="container py-2 my-2 climaDatos">
                        <!--<select class="form-select" style="width:40%" aria-label="Default select example">
                            <option selected>Open this select menu</option>
                            <option value="1">One</option>
                            <option value="2">Two</option>
                            <option value="3">Three</option>
                        </select> -->
                        <div v-if="datosClima != null">
                            <div class="row text-white">
                                <div class="col colClima border">
                                    <div class="marC">
                                        <p class="titclima">{{ getfecha(4)[0] }}</p>
                                        <img id="imgLibro" v-bind:src="iconoLink" />
                                        <p class="desclima">{{ datosClima.list[4].weather[0].description }}
                                            <br>Temperatura: {{ datosClima.list[4].main.temp_min }}°C
                                        </p>
                                    </div>
                                </div>
                                <div class="col colClima border">
                                    <div class="marC">
                                        <p class="titclima">{{ getfecha(11)[0] }}</p>
                                        <img id="imgLibro" v-bind:src="iconoLink" />
                                        <p class="desclima"> {{ datosClima.list[11].weather[0].description }}
                                            <br>Temperatura: {{ datosClima.list[11].main.temp_min }}°C
                                        </p>
                                    </div>
                                </div>
                                <div class="col colClima border">
                                    <div class="marC">
                                        <p class="titclima">{{ getfecha(19)[0] }}</p>
                                        <img id="imgLibro" v-bind:src="iconoLink" />
                                        <p class="desclima">{{ datosClima.list[19].weather[0].description }}
                                            <br>Temperatura: {{ datosClima.list[19].main.temp_min }}°C
                                        </p>
                                    </div>
                                </div>
                                <div class="col colClima border">
                                    <div class="marC">
                                        <p class="titclima">{{ getfecha(27)[0] }}</p>
                                        <img id="imgLibro" v-bind:src="iconoLink" />
                                        <p class="desclima">{{ datosClima.list[27].weather[0].description }} <br>
                                            Temperatura: {{ datosClima.list[27].main.temp_min }}°C
                                        </p>
                                    </div>
                                </div>
                                <div class="col colClima border">
                                    <div class="marC">
                                        <p class="titclima">{{ getfecha(35)[0] }}</p>
                                        <img id="imgLibro" v-bind:src="iconoLink" />
                                        <p class="desclima">{{ datosClima.list[35].weather[0].description }}
                                            <br>Temperatura: {{ datosClima.list[35].main.temp_min }}°C
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="secEquipaje" id="equipaje">
            <div class="container border MenEquipaje" style="float:left">
                <div class="container my-5">
                    <h5>No olvides revisar la lista de articulos prohibidos</h5>
                    <a href="https://www.iberia.com/mx/equipajes/articulos-peligrosos/">Click aqui</a>
                    <div class="col-md-12 ">
                        <div class="login-or">
                            <hr class="hr-or">
                        </div>
                    </div>
                    <h5>Información sobre transporte de mascotas</h5>
                    <a href="https://www.ceupe.com/blog/transporte-de-animales-en-el-avion.html">Click aqui</a>
                </div>
            </div>
            <div class="container border CalEquipaje" style="float:right">
                <h1>Calcula que costo tendra tu equipaje</h1>
                <div class="row">
                    <div class="col">
                        <p>
                            No olvides que si excede el peso reglamentario debera pagar un costo extra dependiendo del
                            peso
                            extra.
                        </p>
                    </div>
                    <div class="col">
                        <p>
                            Su boleto unicamente permite una maleta, debera documentar el equipaje extra
                        </p>
                    </div>
                </div>
                <div class="calEchico">
                    <div class="row">
                        <div class="col-3">
                            <div class="form-group">
                                <label>Cantidad de maletas</label>
                                <input v-model="cantmaletas" type="number" min="0" max="5" class="form-control"
                                    placeholder="0">
                            </div>
                            <div class="form-group">
                                <label>Peso en kilos</label>
                                <input v-model="pesoMaleta" type="number" min="0" max="35" class="form-control"
                                    placeholder="0">
                            </div>
                        </div>
                        <div class="col-8">
                            <button @click="CalcularEquipaje()" class=" btn btn-block mybtn2 btn-primary tx-tfm">Calcular</button>
                            <br><br>
                            <h1>{{constEquipaje}}</h1>
                        </div>
                    </div>
                </div>

            </div>
        </section>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Cliente-Home",
    data: () => ({
        datosClima: null,
        iconoLink: "",
        ciudad: "Ciudad Obregon",
        constEquipaje: 0,
        cantmaletas: 0,
        pesoMaleta: 0,
        miHTML: ``
    }),
    methods: {
        getfecha(dia) {
            return this.datosClima.list[dia].dt_txt.split(" ");
        },
        CalcularEquipaje(){
            var precioXmaleta=300;
            var precioXExtra=12;
            var totMaletas=0;
            var totPeso=0;
            if(this.cantmaletas>1){
                totMaletas=precioXmaleta*(this.cantmaletas-1);
            }
            if(this.pesoMaleta>25){
                totPeso=precioXExtra* (this.pesoMaleta-25);
            }
            this.constEquipaje=totMaletas + totPeso;
        }

    },
    created() {
        this.ciudad = this.ciudad.replace(" ", "%20")
        axios.get("https://api.openweathermap.org/data/2.5/forecast?lang=es&units=metric&q=" + this.ciudad + "&appid=ce62b1ca2ee75f0ad8d8b0e155bf7cc0").then((result) => {
            this.datosClima = result.data;
            console.log(result.data);
            this.iconoLink = "http://openweathermap.org/img/wn/" + result.data.list[4].weather[0].icon + "@2x.png"
        })
    }
}
</script>

<style scoped>
@import "./composables/Client.css";
</style>

