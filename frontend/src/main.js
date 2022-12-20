import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// tailwind css
import './assets/tailwind.css'

// fortawesome icon
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(fas)

// SweetAlert2
const sweetalert2_option = {
  confirmButtonColor: '#41b882',
  cancelButtonColoe: '#ff7674'
}
import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.all'

const app = createApp(App)
app.use(VueSweetalert2, sweetalert2_option)
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
