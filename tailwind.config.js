/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'white': '#ffffff',
      'background':'#17203A',
      'grey':'#FEEEEE'

    },
    extend: {},
  },
  plugins: [
      require("flowbite/plugin")
  ],
}