<template>
  <div>
    <div class="p-.5 bg-primary text-center">
      <br><br><br>
      <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
        <div class="container">
          <a class="navbar-brand"><img src="@/assets/logoAvion.png" alt="..." /> Aerolinea</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive"
            aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"> Menu
            <i class="fas fa-bars ms-1"></i>
          </button>
          <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav text-uppercase  ms-auto py-4 py-lg-0">
              <li class="nav-item"><a class="nav-link" @click="scrollInto('home')" style="cursor:pointer;">Menu</a>
              </li>
              <li class="nav-item"><a class="nav-link" @click="scrollInto('clima')" style="cursor:pointer;">Clima</a>
              </li>
              <li class="nav-item"><a class="nav-link" @click="scrollInto('equipaje')" style="cursor:pointer;">Equipaje</a>
              </li>
              <div class="dropdown">
                <a href="#" class="nav-link nav-item dropdown-toggle"
                  id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                  Servicios
                </a>
                <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                  <li><router-link :to="{name: 'Perfil'}" style="cursor:pointer;" class="dropdown-item">Compra de boletos</router-link></li>
                  <li>
                    <hr class="dropdown-divider">
                  </li>
                  <li><a class="dropdown-item" href="#">Estado del avion</a></li>
                </ul>
              </div>
              <div class="dropdown">
                <a href="#" class="d-flex align-items-center text-dark text-decoration-none dropdown-toggle"
                  id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                  <img src="https://cdn-icons-png.flaticon.com/512/456/456212.png" alt="" width="25" height="25"
                    class="rounded-circle me-2">
                </a>
                <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                  <li><router-link :to="{name: 'Perfil'}" style="cursor:pointer;" class="dropdown-item">Perfil</router-link></li>
                  <li>
                    <hr class="dropdown-divider">
                  </li>
                  <li><a class="dropdown-item" href="#">Cerrar Sesión</a></li>
                </ul>
              </div>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    scrollInto(elementId) {
      const section = document.querySelector(`#${elementId}`);
      section.scrollIntoView({
        behavior: 'smooth'
      });
    }
  }
};
</script>

<style>
#Base {
  text-decoration: none;
}

#mainNav {
  padding-top: 1rem;
  padding-bottom: 1rem;
  background-color: #007bff;
}

#mainNav .navbar-toggler {
  padding: 0.75rem;
  font-size: 0.75rem;
  font-family: "Montserrat", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  text-transform: uppercase;
  font-weight: 700;
}

#mainNav .navbar-brand {
  color: #ffc800;
  font-family: "Montserrat", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-weight: 700;
  letter-spacing: 0.0625em;
  text-transform: uppercase;
}

#mainNav .navbar-brand img {
  height: 1.5rem;
}

#mainNav .navbar-nav .nav-item .nav-link {
  font-family: "Montserrat", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-size: 0.95rem;
  color: #fff;
  letter-spacing: 0.0625em;
}

#mainNav .navbar-nav .nav-item .nav-link.active,
#mainNav .navbar-nav .nav-item .nav-link:hover {
  color: #ffc800;
}

@media (min-width: 992px) {
  #mainNav {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    border: none;
    background-color: transparent;
    transition: padding-top 0.3s ease-in-out, padding-bottom 0.3s ease-in-out;
  }

  #mainNav .navbar-brand {
    font-size: 1.5em;
    transition: font-size 0.3s ease-in-out;
  }

  #mainNav .navbar-brand img {
    height: 2rem;
    transition: height 0.3s ease-in-out;
  }

  #mainNav.navbar-shrink {
    padding-top: 1rem;
    padding-bottom: 1rem;
    background-color: #212529;
  }

  #mainNav.navbar-shrink .navbar-brand {
    font-size: 1.25em;
  }

  #mainNav.navbar-shrink .navbar-brand svg,
  #mainNav.navbar-shrink .navbar-brand img {
    height: 1.5rem;
  }

  #mainNav .navbar-nav .nav-item {
    margin-right: 1rem;
  }

  #mainNav .navbar-nav .nav-item:last-child {
    margin-right: 0;
  }
}
</style>



