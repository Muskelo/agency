<template>
  <div
    id="carouselExampleControls"
    class="carousel slide"
    data-bs-ride="carousel"
  >
    <!-- main -->
    <div class="carousel-inner ratio ratio-16x9">
      <!-- images -->
      <div
        v-for="image in images"
        :key="image.id"
        :class="{ active: image.pos === 0 }"
        class="carousel-item"
      >
        <img src="item1.jpg" class="d-block w-100" alt="..." />
      </div>

      <!-- if no images -->
      <div v-if="images.lenght == 0" class="empty"></div>
    </div>
    <!-- images -->

    <!-- buttons -->
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleControls"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleControls"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
    <!-- buttons -->
  </div>
</template>

<script>
export default {
  props: ["images"],
};
</script>

<style lang="scss" scoped>
.empty {
  background-color: #ddd;
}
</style>
