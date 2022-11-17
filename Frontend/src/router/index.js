import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Base',
    component: () => import('../components/LayoutBase.vue'),
    children: [
      {
        path: '',
        name: 'Login',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Login/Login.vue')
      },
      {
        path: '/',
        name: 'Registro',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Login/Components/Registro.vue')
      }
    ]
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../components/LayoutAdmin.vue'),
    children: [
      {
        path: '/:idUsuario/',
        name: 'AdminHome',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/AdminHome.vue')
      },
      {
        path: '/',
        name: 'GraficaVentas',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/Components/GraficaVentas')
      },
      {
        path: '/AddPiloto/:idUsuario/',
        name: 'AddPiloto',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/Components/Piloto/Components-Pilotos/AddPiloto.vue')
      },
      {
        path: '/VerPiloto/:idUsuario/:idPiloto/',
        name: 'VerPiloto',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/Components/Piloto/Components-Pilotos/VerPiloto.vue')
      },
      {
        path: '/AddAeroPuerto/:idUsuario/',
        name: 'AddAeroPuerto',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/Components/Aeropuertos/Components/AddAeropuerto.vue')
      },
      {
        path: '/VerAeropuerto/:idUsuario/:idAeropuerto/',
        name: 'VerAeropuerto',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/Components/Aeropuertos/Components/VerAeropuerto.vue')
      },
       {
        path: '/AddAvion/:idUsuario/',
        name: 'AddAvion',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/Components/Aviones/Components/AddAvion.vue')
      }
    ]
  },
  {
    path: '/Client',
    name: 'Client',
    component: () => import('../components/LayoutClient.vue'),
    children: [
      {
        path: '/:idUsuario/',
        name: 'ClientHome',
        component: () => import(/* webpackChunkName: "cliente" */ '../Views/Client/ClientHome.vue')
      },
      {
        path: '/',
        name: 'Perfil',
        component: () => import(/* webpackChunkName: "cliente" */ '../Views/Client/Components/Perfil.vue')
      }
    ]
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
