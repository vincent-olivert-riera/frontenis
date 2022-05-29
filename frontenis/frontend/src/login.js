import { createApp } from "vue";
import App from "./LoginPage.vue";
import "./index.css";

import { createI18n } from "vue-i18n";
import en from "./locales/en.yaml";
import es from "./locales/es.yaml";

const i18n = createI18n({
  globalInjection: true,
  legacy: false,
  locale: "en",
  messages: {
    en,
    es,
  },
});

const app = createApp(App);
app.use(i18n);
app.mount("#app");
