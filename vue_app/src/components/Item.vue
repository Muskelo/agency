<template>
  <!-- item component -->
  <section>
    <div class="container pt-5">
      <div class="row">
        <div class="col-12 col-xl-6 mb-2 mb-xl-auto">
          <ItemSlider :images="item.images" />
        </div>
        <div class="col-12 col-xl-6 text-center text-xl-start">
          <h2 class="card-title">{{item.rooms}}-комн., {{item.size}}м<sup>2</sup>, {{item.floor}}/{{item.floor_total}} этаж</h2>
          <p>Адресс: <strong>{{item.address}}</strong></p>
          <p>Цена: <strong>{{item.price}} тыс.р.</strong></p>
          <router-link :to="{ name: 'chat', params: { id: null, item_id: item.id }}" class="btn btn-primary">Связаться</router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import ItemSlider from "./ItemSlider.vue";

export default {
  props: ["id"],
  components: {
    ItemSlider,
  },
  data() {
    return {
      item: {
        id: 16,
        rooms: 2,
        size: 103.74,
        floor: 4,
        floor_total: 9,
        price: 2000,
        address: "Ул.Никулина, д.36, кв.54",
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
      },
    };
  },
};
</script>

<style>
</style>
