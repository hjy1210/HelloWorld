# vue

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## resource
based on [scotch.io course](https://scotch.io/courses/build-an-online-shop-with-vue)

## usage
1. mongo --dbpath=d:\mongodb\data-for-vue-intro
2. In d:\work\helloword\api-for-vue-intro, npm start
3. In d:\work\helloword\vue-intro, npm run dev

## Two issues of ProductForm

In original code, in route `/admin/edit/:id`, the `select` element for manufacturer in ProductForm(vue) do not react to `model.manufacturer`, so none option is selected even if the product already has a manufacturer. 

One possible solution is to modify `<option :value="manufacturer._id" :selected="manufacturer._id == (model.manufacturer && model.manufacturer._id)">{{manufacturer.name}}</option>` as `<option :value="manufacturer" :selected="manufacturer._id == (model.manufacturer && model.manufacturer._id)">{{manufacturer.name}}</option>`.

Another issue, submit complete even form data have validation error. Possible solution is modify methods.saveProduct as:
```
    saveProduct () {
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.$emit('save-product', this.model)
        } else {
          alert('Correct errors before submit!')
        }
      })
    }
```