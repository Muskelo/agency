<template>
  <div id="carouselCreateItem" class="carousel slide" data-bs-ride="carousel" data-bs-interval="false">
    <div class="carousel-inner ratio ratio-16x9">
      <!-- images list-->
      <div v-for="image in images" :key="image.id" :id="image.id" :class="{ active: images.indexOf(image) == 0 }" ref="images" class="carousel-item">
        <img :src="image.filename" class="d-block w-100" alt="..." />
      </div>

      <!-- if no images -->
      <div v-if="!images.length" class="empty"></div>

    </div>

    <!-- buttons -->
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselCreateItem" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselCreateItem" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
    <!-- buttons -->
  </div>

    <button @click="getActiveImage"> gaag</button>
</template>

<script>
export default {
  props: ["images", "currentImageNum"],
  methods: {
    getActiveImage() {
      this.$refs.images.forEach((element) => {
        console.log(element.className.search("active"));
      });
    },
  },
  mounted() {
  },
};
</script>

<style lang="scss" scoped>
.empty {
  background-color: #ddd;
}
</style>
