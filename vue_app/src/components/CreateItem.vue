<template>
  <!-- create item component -->
  <section>
    <div class="container py-3">
      <!-- title -->
      <div class="row">
        <h4>Добавление</h4>
      </div>

      <!-- image adding -->
      <div class="row">
        <h5>Изображение</h5>
      </div>
      <div class="row row-cols-xl-2 g-2 mb-3">
        <div>
          <CreateItemSlider :images="images" />
        </div>
        <div class="d-flex align-items-center justify-content-center">
          <p></p>
          <input type="file" name="image">
          <button class="btn btn-danger">Удалить</button>
        </div>
      </div>
      <!-- rest datat -->
      <div class="row">
        <h5>Данные</h5>
      </div>

      <div class="mb-3 row">
        <label for="email" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="email" placeholder="email">
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CreateItemSlider from "./CreateItemSlider.vue";

export default {
  components: {
    CreateItemSlider,
  },
  data() {
    return {
      images: [
        {
          pos: 0,
          id: 12,
          url: "item1.jpg",
        },
        {
          pos: 1,
          id: 17,
          url: "item1.jpg",
        },
      ],
    };
  },
};
</script>

<style>
</style>
