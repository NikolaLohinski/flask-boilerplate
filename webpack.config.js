const AppCachePlugin = require('appcache-webpack-plugin');
const TransformModulesPlugin = require('webpack-transform-modules-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: {
    'app.js': './src/js/main.js'
  },
  output: {
    path: require('path').resolve(__dirname, 'server', 'static'),
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
    new TransformModulesPlugin(),
    new CopyWebpackPlugin([{
      from: require('path').resolve(__dirname, 'src', 'html', 'index.html'),
      to: require('path').resolve(__dirname, 'server', 'templates', 'index.html'),
    }]),
    new AppCachePlugin({
      output: 'cache.manifest'
    })
  ]
};