import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueI18n from "@intlify/vite-plugin-vue-i18n"

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    manifest: true,
    rollupOptions: {
      input: {
        main: "./src/main.html",
        login: "./src/login.html",
      },
    },
  },
  base: process.env === "production" ? "/static/" : "/",
  root: "./src",
  plugins: [
    vue(),
    vueI18n(),
  ],
});
