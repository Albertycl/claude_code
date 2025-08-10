<template>
  <q-page class="flex flex-center bg-grey-1" padding>
    <div class="column items-center q-gutter-lg" style="max-width: 800px; width: 100%;">
      <!-- API Demo Header -->
      <q-card class="material-card elevation-2 full-width">
        <q-card-section class="bg-gradient text-white text-center">
          <div class="text-h4 q-mb-sm">
            <q-icon name="api" class="q-mr-sm" />
            Backend API Demo
          </div>
          <div class="text-subtitle1">Testing connection to http://10.7.6.77:5491</div>
        </q-card-section>
      </q-card>

      <!-- API Controls -->
      <q-card class="material-card elevation-1 full-width">
        <q-card-section>
          <div class="text-h6 q-mb-md">API Controls</div>
          <div class="row q-gutter-md items-center">
            <q-btn
              color="primary"
              label="Fetch Hello World"
              icon="download"
              @click="fetchHelloWorld"
              :loading="loading"
              :disable="loading"
              unelevated
            />
            <q-btn
              color="secondary"
              label="Clear Response"
              icon="clear"
              @click="clearResponse"
              :disable="!apiResponse && !errorMessage"
              outline
            />
            <q-space />
            <q-chip
              :color="connectionStatus.color"
              :icon="connectionStatus.icon"
              text-color="white"
              :label="connectionStatus.text"
            />
          </div>
        </q-card-section>
      </q-card>

      <!-- API Response -->
      <q-card class="material-card elevation-1 full-width" v-if="apiResponse || errorMessage || loading">
        <q-card-section>
          <div class="text-h6 q-mb-md">
            <q-icon name="receipt" class="q-mr-sm" />
            API Response
          </div>
          
          <!-- Loading State -->
          <div v-if="loading" class="text-center q-pa-lg">
            <q-spinner-dots size="3em" color="primary" />
            <div class="text-body1 q-mt-md">Connecting to backend...</div>
          </div>

          <!-- Success Response -->
          <div v-else-if="apiResponse" class="q-pa-md bg-light-green-1 rounded-borders">
            <div class="row items-center q-mb-sm">
              <q-icon name="check_circle" color="positive" size="1.5em" class="q-mr-sm" />
              <span class="text-h6 text-positive">Success</span>
            </div>
            <div class="api-response">
              <strong>Response Data:</strong>
            </div>
            <pre class="q-mt-sm bg-white q-pa-sm rounded-borders">{{ formatResponse(apiResponse) }}</pre>
            <div class="text-caption text-grey-6 q-mt-sm">
              Response Time: {{ responseTime }}ms | Status: {{ responseStatus }}
            </div>
          </div>

          <!-- Error Response -->
          <div v-else-if="errorMessage" class="q-pa-md bg-red-1 rounded-borders">
            <div class="row items-center q-mb-sm">
              <q-icon name="error" color="negative" size="1.5em" class="q-mr-sm" />
              <span class="text-h6 text-negative">Error</span>
            </div>
            <div class="error-message">
              {{ errorMessage }}
            </div>
            <div class="text-caption text-grey-6 q-mt-sm" v-if="errorDetails">
              Details: {{ errorDetails }}
            </div>
          </div>
        </q-card-section>
      </q-card>

      <!-- Connection Info -->
      <q-card class="material-card elevation-1 full-width">
        <q-card-section>
          <div class="text-h6 q-mb-md">
            <q-icon name="info" class="q-mr-sm" />
            Connection Information
          </div>
          <q-list>
            <q-item>
              <q-item-section avatar>
                <q-icon name="dns" color="primary" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Backend URL</q-item-label>
                <q-item-label caption>http://10.7.6.77:5491</q-item-label>
              </q-item-section>
            </q-item>
            
            <q-item>
              <q-item-section avatar>
                <q-icon name="schedule" color="secondary" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Timeout</q-item-label>
                <q-item-label caption>10 seconds</q-item-label>
              </q-item-section>
            </q-item>

            <q-item>
              <q-item-section avatar>
                <q-icon name="security" color="accent" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Headers</q-item-label>
                <q-item-label caption>Content-Type: application/json</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import { ref, computed } from 'vue'
import { api } from '../boot/axios'
import { useQuasar } from 'quasar'

export default {
  name: 'ApiDemoPage',

  setup() {
    const $q = useQuasar()
    const loading = ref(false)
    const apiResponse = ref(null)
    const errorMessage = ref('')
    const errorDetails = ref('')
    const responseTime = ref(0)
    const responseStatus = ref(null)
    const lastRequestTime = ref(null)

    const connectionStatus = computed(() => {
      if (loading.value) {
        return {
          color: 'orange',
          icon: 'sync',
          text: 'Connecting...'
        }
      } else if (apiResponse.value) {
        return {
          color: 'positive',
          icon: 'wifi',
          text: 'Connected'
        }
      } else if (errorMessage.value) {
        return {
          color: 'negative',
          icon: 'wifi_off',
          text: 'Connection Failed'
        }
      } else {
        return {
          color: 'grey',
          icon: 'help',
          text: 'Not Tested'
        }
      }
    })

    const fetchHelloWorld = async () => {
      loading.value = true
      apiResponse.value = null
      errorMessage.value = ''
      errorDetails.value = ''
      responseTime.value = 0
      responseStatus.value = null

      const startTime = Date.now()
      lastRequestTime.value = startTime

      try {
        console.log('Fetching from /hello endpoint')
        const response = await api.get('/hello')

        responseTime.value = Date.now() - startTime
        responseStatus.value = response.status
        apiResponse.value = response.data

        $q.notify({
          type: 'positive',
          message: `Successfully connected to backend!`,
          caption: `Endpoint: /hello | Time: ${responseTime.value}ms`,
          timeout: 3000,
          actions: [
            { label: 'Dismiss', color: 'white', handler: () => {} }
          ]
        })

      } catch (error) {
        responseTime.value = Date.now() - startTime
        console.error('API Error:', error)

        if (error.response) {
          // Server responded with error status
          errorMessage.value = `Server Error: ${error.response.status} ${error.response.statusText}`
          errorDetails.value = `Response: ${JSON.stringify(error.response.data, null, 2)}`
          responseStatus.value = error.response.status
        } else if (error.request) {
          // Request made but no response received
          errorMessage.value = 'Network Error: Unable to reach the backend server'
          errorDetails.value = 'Please check if the backend server is running on http://10.7.6.77:5491'
        } else {
          // Something else happened
          errorMessage.value = `Request Error: ${error.message}`
          errorDetails.value = 'An unexpected error occurred while making the request'
        }

        $q.notify({
          type: 'negative',
          message: 'Failed to connect to backend',
          caption: errorMessage.value,
          timeout: 5000,
          actions: [
            { label: 'Dismiss', color: 'white', handler: () => {} }
          ]
        })
      } finally {
        loading.value = false
      }
    }

    const clearResponse = () => {
      apiResponse.value = null
      errorMessage.value = ''
      errorDetails.value = ''
      responseTime.value = 0
      responseStatus.value = null

      $q.notify({
        type: 'info',
        message: 'Response cleared',
        timeout: 1000
      })
    }

    const formatResponse = (data) => {
      if (typeof data === 'string') {
        return data
      } else if (typeof data === 'object') {
        return JSON.stringify(data, null, 2)
      } else {
        return String(data)
      }
    }

    return {
      loading,
      apiResponse,
      errorMessage,
      errorDetails,
      responseTime,
      responseStatus,
      connectionStatus,
      fetchHelloWorld,
      clearResponse,
      formatResponse
    }
  }
}
</script>

<style scoped>
.q-page {
  min-height: calc(100vh - 128px);
}

.bg-gradient {
  background: linear-gradient(135deg, var(--q-primary) 0%, var(--q-secondary) 100%);
}

pre {
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 0.9rem;
  line-height: 1.4;
  max-height: 300px;
  overflow-y: auto;
  border: 1px solid #e0e0e0;
}

.api-response {
  font-weight: 500;
}

.error-message {
  font-size: 1rem;
  line-height: 1.5;
}
</style>