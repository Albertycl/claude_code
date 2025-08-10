# Quasar Vite Project Development Guide

## Project Overview

This is a Quasar Framework application built with Vite as the build tool. The project demonstrates Material Design 3 components and includes backend API integration capabilities.

## Prerequisites

- Node.js (>= 18.12.0)
- npm (>= 8.12.0) or yarn (>= 1.21.1)

## Installation

1. Install dependencies:
```bash
npm install
# or
yarn
```

## Development

### Start Development Server
```bash
npm run dev
# or
yarn dev
```

The development server will start at `http://localhost:9000` with hot module replacement enabled.

### Backend API Configuration

The application is configured to connect to a backend API at `http://10.7.6.77:5000`. 

- API calls are proxied through `/api` route during development
- The API service (`src/boot/axios.js`) handles authentication, error handling, and request/response interceptors
- Test the API connection using the "API Demo" page in the application

## Build

### Production Build
```bash
npm run build
# or
yarn build
```

### Development Build with Linting
```bash
npm run lint
# or
yarn lint
```

## Project Structure

```
├── index.html                 # HTML entry point
├── package.json              # Dependencies and scripts
├── quasar.config.js          # Quasar configuration with Vite
├── .eslintrc.js              # ESLint configuration
├── public/                   # Static assets
├── src/
│   ├── App.vue              # Root component
│   ├── main.js              # Application entry point
│   ├── boot/
│   │   └── axios.js         # API service configuration
│   ├── components/          # Reusable Vue components
│   ├── css/
│   │   └── app.scss         # Global styles and Material Design customizations
│   ├── layouts/
│   │   └── MainLayout.vue   # Main application layout with Material Design
│   ├── pages/
│   │   ├── IndexPage.vue    # Home page
│   │   ├── ApiDemoPage.vue  # Backend API demonstration
│   │   └── ErrorNotFound.vue # 404 error page
│   ├── router/
│   │   ├── index.js         # Router configuration
│   │   └── routes.js        # Route definitions
│   └── stores/              # Pinia state management (if needed)
```

## Features

### Material Design Implementation
- Uses Quasar's built-in Material Design 3 components
- Follows Google's Material Design color system and typography
- Implements proper elevation, shadows, and spacing
- Responsive design using Quasar's grid system

### Backend Integration
- Axios-based API service with interceptors
- Error handling and loading states
- Configurable timeout and headers
- Development proxy for API requests

### Vite Integration
- Lightning-fast development server with HMR
- Optimized production builds
- Tree-shaking for smaller bundle sizes
- TypeScript support ready

## API Testing

Navigate to the "API Demo" page to test the backend connection. The application will:

1. Attempt to connect to multiple common endpoints (`/`, `/hello`, `/api`, etc.)
2. Display the response data or error information
3. Show connection status and response times
4. Provide proper error handling for network issues

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run clean` - Clean build artifacts
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier
- `npm run test` - Run tests (Vitest)

## Customization

### Theming
Edit `src/css/app.scss` to customize Material Design colors and styles.

### API Configuration
Modify `src/boot/axios.js` to change backend URL, timeout, or headers.

### Components
Add new components in `src/components/` and import them as needed.

### Pages and Routes
Add new pages in `src/pages/` and define routes in `src/router/routes.js`.

## Troubleshooting

### Common Issues

1. **Port already in use**: Change port in `quasar.config.js` under `devServer.port`
2. **API connection issues**: Verify backend server is running at `http://10.7.6.77:5000`
3. **Build errors**: Run `npm run clean` and then `npm run build`

### Development Tools

- Vue DevTools browser extension for debugging
- Quasar DevTools for component inspection
- Network tab for API request debugging