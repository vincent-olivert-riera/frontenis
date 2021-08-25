module.exports = {
  purge: ["./src/main.html", "./src/login.html", "./src/**/*.{vue,js}"],
  darkMode: false, // or "media" or "class"
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms")],
};
