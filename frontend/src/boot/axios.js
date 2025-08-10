import { boot } from 'quasar/wrappers'
import axios from 'axios'

// Create axios instance
const api = axios.create({
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    console.log('Making API request to:', config.url)
    return config
  },
  (error) => {
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  (response) => {
    console.log('API response received:', response.status)
    return response
  },
  (error) => {
    console.error('Response error:', error.response?.status, error.message)
    return Promise.reject(error)
  }
)

export default boot(({ app }) => {
  // Make axios available globally
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = api
})

export { api }