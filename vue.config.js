// module.exports = {
//   transpileDependencies: [
//     'vuetify'
//   ]
// }

const path = require('path');
const express = require('express');




module.exports = {
  
  productionSourceMap: false,

  transpileDependencies: [
    'vuetify'
  ],
  
  publicPath: process.env.NODE_ENV === 'production'
    ? '/'
    : '/',
  configureWebpack: {
    
    devServer: {

      before: app => {
        app.use('/node_modules/', express.static(path.resolve(__dirname, 'node_modules')))
      },

      headers: { "Cross-Origin-Embedder-Policy" : "require-corp",
                  "Cross-Origin-Opener-Policy" : "same-origin" }
    }




  }
};