const { fontFamily } = require("tailwindcss/defaultTheme");

// https://medium.com/@bargadyahmed/docusaurus-a-guide-to-seamless-integration-with-tailwind-css-dd202211caac

/** @type {import('tailwindcss').Config} */
module.exports = {
  corePlugins: {
    preflight: false,
    container: false,
  },
  darkMode: ['class', '[data-theme="dark"]'],
  content: ['./src/**/*.{js,jsx,ts,tsx,html}'],
  plugins: [
    require('@tailwindcss/typography')
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Google Sans"', ...fontFamily.sans],
      },
    },
  },
  variants: {
    listStyleType: ['responsive', 'hover', 'focus'],
    listStylePosition: ['responsive', 'hover', 'focus'],
  },
  corePlugins: {
    preflight: false,
  }
};