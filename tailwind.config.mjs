/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			fontFamily: {
				serif: ["Source Serif Pro", defaultTheme.fontFamily.serif],
			},
			width: {
				'search': '515px',
			}
		},
	},
	plugins: [],
}
