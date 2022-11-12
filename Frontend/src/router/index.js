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
      }
    ]
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../components/LayoutAdmin.vue'),
    children: [
      {
        path: '',
        name: 'AdminHome',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/AdminHome.vue')
      },
      {
        path: '/',
        name: 'GraficaVentas',
        component: () => import(/* webpackChunkName: "login" */ '../Views/Admin/Components/GraficaVentas')
      }
    ]
  },
  {
    path: '/Client',
    name: 'Client',
    component: () => import('../components/LayoutClient.vue'),
    children: [
      {
        path: '',
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
