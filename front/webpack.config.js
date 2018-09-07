const Webpack = require('webpack');
const HTMLWebpackPlugin = require('html-webpack-plugin');
const TransformModulesPlugin = require('webpack-transform-modules-plugin');
module.exports = {
  entry: {
    'app.js': require('path').resolve(__dirname, 'src', 'js', 'main.js')
  },
  output: {
    path: require('path').resolve(__dirname, 'dist'),
    filename: '[name]'
  },
  resolve: {
    alias: {
      'vue': 'vue/dist/vue.common.js'
    }
  },
  devServer: {
    port: 8080,
    compress: true,
    stats: 'errors-only'
  },
  module: {
    rules: [
      {
        enforce: 'pre',
        test: /\.(js|vue)$/,
        exclude: [/node_modules/, /\.min.js$/],
        loader: 'eslint-loader'
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
      },
      {
        test: /\.(png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot|otf|min.js)(\?.*$|$)/,
        loader: 'file-loader',
        options: {
          name: 'assets/[hash].[ext]'
        }
      },
      {
        test: /\.html$/,
        exclude: /node_modules/,
        use: [{
          loader: 'html-loader',
          options: {
            minimize: true,
            removeComments: true,
            collapseWhitespace: true,
            attrs: ['link:href', 'script:src']
          }
        }]
      },
      {
        test: /\.json$/,
        loader: 'json-loader'
      },
      {
        test: /\.js$/,
        exclude: [/node_modules\/(?!(deck-of-cards)\/).*/],
        loader: 'babel-loader'
      },
      {
        test: /\.vue$/,
        exclude: [/node_modules/],
        loader: 'vue-loader',
        options: {
          loaders: {
            scss: 'vue-style-loader!css-loader!sass-loader'
          }
        }
      }
    ]
  },
  plugins: [
    new Webpack.DefinePlugin({
      '__VERSION__': JSON.stringify(require('./package.json').version)
    }),
    new TransformModulesPlugin(),
    new HTMLWebpackPlugin({
      template: 'src/html/index.html',
      filename: 'index.html',
      favicon: require('path').resolve(__dirname, 'src', 'img', 'stacklabs.png')
    })
  ]
};