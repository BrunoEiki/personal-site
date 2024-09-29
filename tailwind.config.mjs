/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
	content: [
		"./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}",
		"./node_modules/flowbite/**/*.js",
	],
	darkMode: "selector",
	theme: {
		extend: {
			fontFamily: {
				serif: ["Source Serif Pro", defaultTheme.fontFamily.serif],
				sans: ["Arial"],
			},
			width: {
				search: "515px",
			},
			fontSize: {
				xxs: "3.8px",
				xxxs: "2px",
			},
			leading: {
				1: "3.2px",
			},
			margin: {
				100: "20rem",
			},
			height: {
				px0: "0.09px",
			},
		},
	},
	plugins: [require("flowbite/plugin")],
};
