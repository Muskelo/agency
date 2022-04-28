<template>
  <!-- chat component -->
  <section>
    <div class="container">

      <div class="chat border col-xl-6 offset-xl-3">
        <div class="chat-header d-flex p-2 border-bottom">
          <img :src="item.images[0].url" alt="">
          <p>{{item.rooms}}-комн., {{item.size}}м<sup>2</sup>, {{item.floor}}/{{item.floor_total}} этаж</p>
        </div>
        <div class="chat-body">
          <ul class="list-unstyled p-3">

            <li v-for="message in messages" :key="message.id" class="mb-2">
              <div class="card col-9" v-bind:class="{ 'offset-3' : message.owner === 'me'}">
                <div class="card-header p-1" :class="{ 'text-end' : message.owner === 'me'}">
                  {{message.owner}}
                </div>
                <div class="card-body">
                  {{message.body}}
                </div>
              </div>
            </li>

          </ul>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  props: ["id", "item_id"],
  data() {
    return {
      item: {
        rooms: 3,
        size: 103,
        floor: 4,
        floor_total: 5,
        images: [
          {
            id: 2,
            url: "item1.jpg",
          },
        ],
      },
      messages: [
        {
          id: 17,
          body: "hahahahaha, cool",
          owner: "admin",
        },
        {
          id: 19,
          body: "NOONNOON hahahaha, cool",
          owner: "me",
        },
        {
          id: 17,
          body: "hahahahaha, cool",
          owner: "admin",
        },
        {
          id: 19,
          body: "NOONNOON hahahaha, cool",
          owner: "me",
        },
        {
          id: 17,
          body: "hahahahaha, cool",
          owner: "admin",
        },
        {
          id: 19,
          body: "NOONNOON hahahaha, cool",
          owner: "me",
        },
        {
          id: 17,
          body: "hahahahaha, cool",
          owner: "admin",
        },
        {
          id: 19,
          body: "NOONNOON hahahaha, cool",
          owner: "me",
        },
        {
          id: 17,
          body: "hahahahaha, cool",
          owner: "admin",
        },
        {
          id: 19,
          body: "NOONNOON hahahaha, cool",
          owner: "me",
        },
        {
          id: 17,
          body: "hahahahaha, cool",
          owner: "admin",
        },
        {
          id: 19,
          body: "NOONNOON hahahaha, cool",
          owner: "me",
        },
        {
          id: 17,
          body: "hahahahaha, cool",
          owner: "admin",
        },
        {
          id: 19,
          body: "NOONNOON hahahaha, cool",
          owner: "me",
        },
      ],
    };
  },
};
</script>

<style lang="scss"  scoped>
.chat-header {
  height: 50px;
}
.chat-body {
    max-height: 80vh;
    overflow-y: scroll;
}
</style>
