<template>
  <!-- create item component -->
  <section>
    <div class="container py-3">
      <!-- title -->
      <div class="row">
        <h4>Добавление нового объекта</h4>
      </div>

      <!-- image adding -->
      <div class="row">
        <h5>Изображения</h5>
      </div>
      <div class="row g-2 mb-3">
        <div>
          <CreateItemSlider :images="images" />
        </div>
        <div class="d-flex align-items-center justify-content-between">
          <input type="file" name="image" class="form-control" />
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
          <input type="text" class="form-control" id="email" placeholder="email" />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { images_list_api } from "../api";
// components
import CreateItemSlider from "./CreateItemSlider.vue";

export default {
  components: {
    CreateItemSlider,
  },
  data() {
    return {
      images: Array(),
      currentImageNum: 0,
    };
  },
  methods: {
    async getImages() {
      const response = await images_list_api.get();
      this.images = response["data"];
    },
  },
  mounted() {
    this.getImages();
  },
};
</script>

<style>
</style>
