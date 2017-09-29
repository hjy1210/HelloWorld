<!-- ./src/pages/admin/Edit.vue -->
<template>
  <product-form @save-product="updateProduct" :model="model" :manufacturers="manufacturers" :isEditing="true">
  </product-form>
</template>

<script>
import ProductFrom from '../../components/product/ProductForm.vue'
export default {
  created () {
    if (!this.model.name) {
      console.log('dispatched')
      this.$store.dispatch('productById', this.$route.params['id'])
    }
    if (this.manufacturers.length === 0) {
      this.$store.dispatch('allManufacturers')
    }
  },
  computed: {
    manufacturers () {
      return this.$store.getters.allManufacturers
    },
    model () {
      const productById = this.$store.getters.productById(this.$route.params['id'])
      return Object.assign({}, productById)
    }
  },
  methods: {
    updateProduct (model) {
      console.log('model', model)
      this.$store.dispatch('updateProduct', model)
    }
  },
  components: {
    'product-form': ProductFrom
  }
}
</script>
