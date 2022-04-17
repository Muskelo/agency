<script>
export default {
  data() {
    return {
    };
  },
};
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container d-flex justify-content-between">
      <a class="navbar-brand" href="#">AGENCY</a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse flex-grow-0" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 gap-1">

          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>

          <li class="nav-item">
            <button type="button" v-if="!this.current_user.data.id" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalLogin">
              Вход
            </button>
          </li>
          <li class="nav-item">
            <button type="button" v-if="!this.current_user.data['id']" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegister">
              Регистрация
            </button>
          </li>
          <li class="nav-item">
            <button type="button" @click="current_user.logout" v-if="current_user.data['id']" class="btn btn-primary">
              Выход
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
