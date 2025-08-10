<template>
  <q-page class="flex flex-center bg-grey-1" padding>
    <div class="column items-center q-gutter-md" style="max-width: 600px; width: 100%;">
      <!-- Welcome Card -->
      <q-card class="material-card elevation-2 full-width">
        <q-card-section class="bg-primary text-white text-center">
          <div class="text-h4 q-mb-sm">Welcome to Quasar + Vite</div>
          <div class="text-subtitle1">Material Design Components Demo</div>
        </q-card-section>

        <q-card-section class="text-center">
          <q-icon name="rocket_launch" size="4em" color="primary" class="q-mb-md" />
          <div class="text-h6 q-mb-sm">Modern Development Stack</div>
          <div class="text-body2 text-grey-7">
            This application demonstrates Quasar Framework with Vite build tool,
            featuring Material Design 3 components and backend API integration.
          </div>
        </q-card-section>

        <q-card-actions align="center">
          <q-btn
            color="primary"
            label="Test API Connection"
            icon="api"
            @click="$router.push({ name: 'api-demo' })"
            unelevated
            rounded
          />
        </q-card-actions>
      </q-card>

      <!-- Features Grid -->
      <div class="row q-gutter-md full-width">
        <div class="col-12 col-md-6">
          <q-card class="material-card elevation-1 full-height">
            <q-card-section>
              <div class="row items-center q-gutter-sm q-mb-md">
                <q-icon name="speed" size="2em" color="positive" />
                <div class="text-h6">Fast Development</div>
              </div>
              <div class="text-body2">
                Vite provides lightning-fast hot module replacement and optimized builds
                for enhanced developer experience.
              </div>
            </q-card-section>
          </q-card>
        </div>

        <div class="col-12 col-md-6">
          <q-card class="material-card elevation-1 full-height">
            <q-card-section>
              <div class="row items-center q-gutter-sm q-mb-md">
                <q-icon name="palette" size="2em" color="secondary" />
                <div class="text-h6">Material Design</div>
              </div>
              <div class="text-body2">
                Beautiful, consistent UI components following Google's Material Design
                principles and guidelines.
              </div>
            </q-card-section>
          </q-card>
        </div>

        <div class="col-12">
          <q-card class="material-card elevation-1">
            <q-card-section>
              <div class="row items-center q-gutter-sm q-mb-md">
                <q-icon name="cloud" size="2em" color="info" />
                <div class="text-h6">Backend Integration</div>
              </div>
              <div class="text-body2">
                Seamless API integration with proper error handling, loading states,
                and response management using Axios.
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>

      <!-- Quick Actions -->
      <q-card class="material-card elevation-1 full-width">
        <q-card-section>
          <div class="text-h6 q-mb-md text-center">Quick Actions</div>
          <div class="row q-gutter-sm justify-center">
            <q-btn
              color="primary"
              label="API Demo"
              icon="api"
              @click="$router.push({ name: 'api-demo' })"
              outline
            />
            <q-btn
              color="secondary"
              label="Documentation"
              icon="book"
              href="https://quasar.dev"
              target="_blank"
              outline
            />
            <q-btn
              color="accent"
              label="GitHub"
              icon="code"
              href="https://github.com/quasarframework/quasar"
              target="_blank"
              outline
            />
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>

<style scoped>
.q-page {
  min-height: calc(100vh - 128px); /* Account for header and footer */
}

.material-card {
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.material-card:hover {
  transform: translateY(-4px);
}

.full-height {
  height: 100%;
}
</style>