var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
	mode: 'development', // hardcoding dev mode for now. Will add hot reloading when needed.
	context: __dirname,
	entry: './assets/js/index',
	output: {
		path: path.resolve('./political_search_engine/static/bundles/'),
		filename: "[name]-[hash].js",
	},
	plugins: [
		new BundleTracker({filename: './webpack-stats.json'}),
	],
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: ['babel-loader']
			}
		]
	},
	resolve: {
		extensions: ['*', '.js', '.jsx']
	}
};
