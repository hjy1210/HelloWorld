// ./src/pages/Home
<template>
  <div>
    <div class="title">
      <h1><i class="fa fa-braille"></i> In Stock</h1>
    </div>
    <product-list></product-list>
  </div>
</template>

<script>
  import ProductList from '../components/product/ProductList.vue'
  export default {
    name: 'home',
    components: {
      'product-list': ProductList
    }
  }
</script>
