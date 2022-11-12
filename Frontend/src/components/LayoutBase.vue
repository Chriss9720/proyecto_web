<template>
  <div>
    <div class="p-1 bg-primary text-center">
      <!--<button class="btn-sm btn-primary" @click="retroceder()" style="float: left;">Volver</button> -->
      <h3><router-link id ="Base" to="/" class="text-white">El changarro</router-link></h3>
      
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
};
</script>

<style>
  #Base{
    text-decoration: none;
  }
</style>
