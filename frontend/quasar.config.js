/* eslint-env node */

/*
 * This file runs in a Node context (it's NOT transpiled by Babel), so use only
 * the ES6 features that are supported by your Node version. https://node.green/
 */

// Configuration for your app
// https://v2.quasar.dev/quasar-cli-vite/quasar-config-js

import { configure } from 'quasar/wrappers'

export default configure(function (/* ctx */) {
  return {
    eslint: {
      warnings: true,
      errors: true
    },

    // https://v2.quasar.dev/quasar-cli-vite/prefetch-feature
    preFetch: true,

    // app boot file (/src/boot)
    // --> boot files are part of "main.js"
    boot: [
      'axios'
    ],

    // https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#css
    css: [
      'app.scss'
    ],

    // https://github.com/quasarframework/quasar/tree/dev/extras
    extras: [
      // 'ionicons-v4',
      // 'mdi-v7',
      // 'fontawesome-v6',
      // 'eva-icons',
      // 'themify',
      // 'line-awesome',
      // 'roboto-font-latin-ext', // this or...
      'roboto-font', // this
      'material-icons' // optional, you are not bound to it
    ],

    // Full list of options: https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#build
    build: {
      vueRouterMode: 'hash', // available values: 'hash', 'history'

      // transpile: false,
      // publicPath: '/',

      // Add support for TypeScript files
      // https://v2.quasar.dev/quasar-cli-vite/handling-vite#typescript-support
      // extendViteConf (viteConf, { isServer, isClient }) {},

      // vitePlugins: [
      //   ['@vitejs/plugin-vue', {
      //     template: { transformAssetUrls: { img: 'src' } }
      //   }]
      // ]
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#devserver
    devServer: {
      open: true, // opens browser window automatically
      port: 5490,
      proxy: {
        '/api': {
          target: 'http://10.7.6.77:5491',
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '')
        },
        '/hello': {
          target: 'http://10.7.6.77:5491',
          changeOrigin: true
        }
      }
    },

    // https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#framework
    framework: {
      config: {},

      // iconSet: 'material-icons', // Quasar icon set
      // lang: 'en-US', // Quasar language pack

      // For special cases outside of where the auto-import strategy can have an impact
      // (like functional components as one of the examples),
      // you can manually specify Quasar components/directives to be available everywhere:
      //
      // components: [],
      // directives: [],

      // Quasar plugins
      plugins: [
        'Notify',
        'Dialog',
        'Loading'
      ]
    },

    // animations: 'all', // --- includes all animations
    // https://v2.quasar.dev/options/animations
    animations: [],

    // https://v2.quasar.dev/quasar-cli-vite/developing-ssr/configuring-ssr
    ssr: {
      pwa: false,

      // manualStoreHydration: true,
      // manualPostHydrationTrigger: true,

      prodPort: 3000, // The default port that the production server should use
                      // (gets superseded if process.env.PORT is specified at runtime)

      maxAge: 1000 * 60 * 60 * 24 * 30,
        // Tell browser when a file from the server should expire from cache (in ms)

      chainWebpackWebserver (chain) {
        chain.plugin('eslint-webpack-plugin')
          .use(ESLintPlugin, [{ extensions: [ 'js', 'vue' ] }])
      },

      middlewares: [
        'render' // keep this as last one
      ]
    },

    // https://v2.quasar.dev/quasar-cli-vite/developing-pwa/configuring-pwa
    pwa: {
      workboxPluginMode: 'GenerateSW', // 'GenerateSW' or 'InjectManifest'
      workboxOptions: {}, // only for GenerateSW

      // for the custom service worker ONLY (/src-pwa/custom-service-worker.[js|ts])
      // if using workbox in InjectManifest mode
      chainWebpackCustomSW (chain) {
        chain.plugin('eslint-webpack-plugin')
          .use(ESLintPlugin, [{ extensions: [ 'js' ] }])
      },

      manifest: {
        name: `Quasar Vite App`,
        short_name: `Quasar Vite App`,
        description: `A Quasar project with Vite build tool`,
        display: 'standalone',
        orientation: 'portrait',
        background_color: '#ffffff',
        theme_color: '#027be3',
        icons: [
          {
            src: 'icons/icon-128x128.png',
            sizes: '128x128',
            type: 'image/png'
          },
          {
            src: 'icons/icon-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'icons/icon-256x256.png',
            sizes: '256x256',
            type: 'image/png'
          },
          {
            src: 'icons/icon-384x384.png',
            sizes: '384x384',
            type: 'image/png'
          },
          {
            src: 'icons/icon-512x512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-vite/developing-cordova-apps/configuring-cordova
    cordova: {
      // noIosLegacyBuildFlag: true, // uncomment only if you know what you are doing
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-vite/developing-capacitor-apps/configuring-capacitor
    capacitor: {
      hideSplashscreen: true
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-vite/developing-electron-apps/configuring-electron
    electron: {
      bundler: 'packager', // 'packager' or 'builder'

      packager: {
        // https://github.com/electron-userland/electron-packager/blob/master/docs/api.md#options

        // OS X / Mac App Store
        // appBundleId: '',
        // appCategoryType: '',
        // osxSign: '',
        // protocol: 'myapp://path',

        // Windows only
        // win32metadata: { ... }
      },

      builder: {
        // https://www.electron.build/configuration/configuration

        appId: 'quasar-vite-project'
      },

      // "chain" is a webpack-chain object https://github.com/neutrinojs/webpack-chain
      chainWebpackMain (chain) {
        chain.plugin('eslint-webpack-plugin')
          .use(ESLintPlugin, [{ extensions: [ 'js' ] }])
      },

      chainWebpackPreload (chain) {
        chain.plugin('eslint-webpack-plugin')
          .use(ESLintPlugin, [{ extensions: [ 'js' ] }])
      }
    }
  }
})