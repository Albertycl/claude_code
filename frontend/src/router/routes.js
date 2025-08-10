const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { 
        path: '', 
        name: 'home',
        component: () => import('pages/IndexPage.vue') 
      },
      { 
        path: '/api-demo', 
        name: 'api-demo',
        component: () => import('pages/ApiDemoPage.vue') 
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes