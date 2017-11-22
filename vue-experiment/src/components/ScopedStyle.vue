<template>
  <div>
    <h1>{{ msg }}</h1>
    <p>Color of Text in p element of scoped-style is blue</p>
  </div>
</template>

<script>
export default {
  name: 'scopedstyle',
  data () {
    return {
      msg: 'Welcome to ScopedStyled Component.'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  color: blue;
}

</style>
