import { createApp } from 'vue'
import { Quasar, Notify, Dialog, Loading } from 'quasar'

// Import icon libraries  
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/dist/quasar.css'

// Import app styles
import './css/app.scss'

// Assumes your root component is App.vue
// and placed in same folder as main.js
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

const myApp = createApp(App)

myApp.use(Quasar, {
  plugins: {
    Notify,
    Dialog,
    Loading
  },
  config: {
    notify: {
      position: 'top',
      timeout: 3000
    }
  }
})

const pinia = createPinia()
myApp.use(pinia)
myApp.use(router)

// Mount to the app element defined by Quasar
myApp.mount('#q-app')