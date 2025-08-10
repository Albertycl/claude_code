<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Quasar Vite App
        </q-toolbar-title>

        <q-space />

        <q-btn
          flat
          dense
          round
          icon="notifications"
          aria-label="Notifications"
        />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="bg-grey-1"
    >
      <q-list>
        <q-item-label header class="text-primary text-weight-bold">
          Navigation
        </q-item-label>

        <q-item
          clickable
          v-ripple
          :to="{ name: 'home' }"
          exact
        >
          <q-item-section avatar>
            <q-icon name="home" />
          </q-item-section>

          <q-item-section>
            <q-item-label>Home</q-item-label>
            <q-item-label caption>
              Main dashboard
            </q-item-label>
          </q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :to="{ name: 'api-demo' }"
        >
          <q-item-section avatar>
            <q-icon name="api" />
          </q-item-section>

          <q-item-section>
            <q-item-label>API Demo</q-item-label>
            <q-item-label caption>
              Backend connection test
            </q-item-label>
          </q-item-section>
        </q-item>

        <q-separator />

        <q-item
          clickable
          v-ripple
          @click="showAboutDialog"
        >
          <q-item-section avatar>
            <q-icon name="info" />
          </q-item-section>

          <q-item-section>
            <q-item-label>About</q-item-label>
            <q-item-label caption>
              App information
            </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title class="text-center">
          <small>Powered by Quasar Framework with Vite</small>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

export default {
  name: 'MainLayout',

  setup() {
    const $q = useQuasar()
    const leftDrawerOpen = ref(false)

    const toggleLeftDrawer = () => {
      leftDrawerOpen.value = !leftDrawerOpen.value
    }

    const showAboutDialog = () => {
      $q.dialog({
        title: 'About',
        message: 'This is a Quasar Framework application built with Vite. It demonstrates Material Design components and backend API integration.',
        ok: {
          push: true,
          color: 'primary'
        }
      })
    }

    return {
      leftDrawerOpen,
      toggleLeftDrawer,
      showAboutDialog
    }
  }
}
</script>

<style scoped>
.q-header {
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.12);
}

.q-drawer {
  box-shadow: 2px 0px 4px rgba(0, 0, 0, 0.12);
}

.q-footer {
  box-shadow: 0px -2px 4px rgba(0, 0, 0, 0.12);
}
</style>