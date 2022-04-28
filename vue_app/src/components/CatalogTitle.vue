<template>
  <!-- catalog title component -->
  <div class="wrapper">
    <div class="container py-5">

      <div class="row mb-4">
        <h1>Перемены к лучшему!</h1>
      </div>

      <div class="row">
        <div class="col-xl-11 mb-3">
          <form class="list-group list-group-horizontal-xl">
            <input type="number" class="list-group-item col-xl-2" placeholder="Комнат">
            <input type="number" class="list-group-item col-xl-2" placeholder="Цена">
            <input type="text" class="list-group-item col-xl-8" placeholder="Город, улица, адресс...">
          </form>
        </div>
        <div class="mx-auto col-auto col-xl-1">
          <button class="btn btn-primary">Поиск</button>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.wrapper {
  background: url(title.jpg) center center;
  background-size: cover;
}
h1 {
  color: white;
}
</style>
