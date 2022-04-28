<template>
  <!-- catalog component -->
  <section class="catalog">
    <CatalogTitle />
    <CatalogList :items="items" />
  </section>
</template>

<script>
import CatalogTitle from "./CatalogTitle.vue";
import CatalogList from "./CatalogList.vue";

export default {
  components: {
    CatalogTitle,
    CatalogList,
  },
  data() {
    return {
      items: [
        {
          id: 28,
          rooms: 3,
          size: 107,
          floor: 3,
          floor_total: 5,
          price: 200000,
          images: [
            {
              id: 3,
              url: "item1.jpg",
            },
          ],
        },
        {
          id: 28,
          rooms: 3,
          size: 107,
          floor: 3,
          floor_total: 5,
          price: 200000,
          images: [
            {
              id: 3,
              url: "item1.jpg",
            },
          ],
        },
        {
          id: 28,
          rooms: 3,
          size: 107,
          floor: 3,
          floor_total: 5,
          price: 200000,
          images: [
            {
              id: 3,
              url: "item1.jpg",
            },
          ],
        },
      ],
    };
  },
};
</script>

<style>
</style>
