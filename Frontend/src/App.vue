<template>
  <router-view/>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
}

#nav {
  padding: 5px;

  a {
    font-weight: bold;
    color: #e00e0e;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#login {
  padding: 30px;
}

#conteinerCard {
  display: inline-block;
}
</style>
