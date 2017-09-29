<template>
  <form @submit.prevent="saveProduct">
    <div class="col-lg-5 col-md-5 col-sm-12 col-xs-12">
      <div class="form-group">
        <label>Name</label>
        <input type="text" placeholder="Name" v-model="model.name" v-validate="'required'" name="name" :class="{'form-control': true, 'error': errors.has('name') }" />
        <span class="small text-danger" v-show="errors.has('name')">{{ errors.first('name') }}</span>
      </div>
      <div class="form-group">
        <label>Price</label>
        <input type="number" :class="{'form-control': true, 'error': errors.has('price') }" placeholder="Price" v-validate="'required'" v-model="model.price" name="price" />
        <span class="small text-danger" v-show="errors.has('price')">{{ errors.first('price') }}</span>
      </div>
      <div class="form-group">
        <label>Manufacturer</label>
        <select :class="{'form-control': true, 'error': errors.has('manufacturer') }" v-validate="'required'" v-model="model.manufacturer" name="manufacturer">
          <template v-for="manufacturer in manufacturers">
            <option :value="manufacturer" :selected="manufacturer._id == (model.manufacturer && model.manufacturer._id)">{{manufacturer.name}}</option>
          </template>
        </select>
        <span class="small text-danger" v-show="errors.has('manufacturer')">{{ errors.first('manufacturer') }}</span>
      </div>
    </div>

    <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
      <div class="form-group">
        <label>Image</label>
        <input type="text" :class="{'form-control': true, 'error': errors.has('image') }" v-validate="'required|url'" placeholder="Image" v-model="model.image" name="image" />
        <span class="small text-danger" v-show="errors.has('image')">{{ errors.first('image') }}</span>
      </div>
      <div class="form-group">
        <label>Description</label>
        <textarea :class="{'form-control': true, 'error': errors.has('description') }" v-validate="'required'" placeholder="Description" rows="5" v-model="model.description" name="description"></textarea>
        <span class="small text-danger" v-show="errors.has('description')">{{ errors.first('description') }}</span>
      </div>
      <div class="form-group new-button">
        <button class="button">
          <i class="fa fa-pencil"></i>
          <!-- Conditional rendering for input text -->
          <span v-if="isEditing">Update Product</span>
          <span v-else>Add Product</span>
        </button>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  props: ['model', 'isEditing', 'manufacturers'],
  methods: {
    saveProduct () {
      // console.log(this.fields.valid())
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.$emit('save-product', this.model)
        } else {
          alert('Correct errors before submit!')
        }
      })
    }
  }
}
</script>