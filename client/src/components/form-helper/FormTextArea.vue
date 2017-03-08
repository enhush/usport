<template lang="html">
  <div class="">

    <div class="columns is-vcentered has-text-right mb0">
      <p class="column">
        <label class="label content is-small">{{label}}</label>
      </p>
      <p class="column">
        <slot name="element"></slot>
      </p>
    </div>
    <div class="has-text-right mt-15">
      <slot name="error"></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: ['label'],
}
</script>

<style scoped>
.mb0 {
  margin-bottom: 0;
}
</style>
