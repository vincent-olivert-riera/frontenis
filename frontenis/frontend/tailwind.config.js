module.exports = {
  content: ["./src/main.html", "./src/login.html", "./src/**/*.{vue,js}"],
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms")],
};
