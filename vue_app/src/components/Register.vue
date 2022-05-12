<template>
  <section class="container py-3">
    <!-- Pills content -->
    <div class="tab-pane fade show active" id="pills-register" role="tabpanel" aria-labelledby="tab-register">
      <form>
        <h4 class="text-center">Регистрация</h4>

        <!-- Login input -->
        <div class="form-outline mb-4">
          <label class="form-label" for="login">Логин</label>
          <input type="text" id="login" class="form-control" />
        </div>

        <!-- Number input -->
        <div class="form-outline mb-4">
          <label class="form-label" for="number">Телефон</label>
          <input type="text" id="number" class="form-control" />
        </div>

        <!-- Password input -->
        <div class="form-outline mb-4">
          <label class="form-label" for="password">Пароль</label>
          <input type="password" id="password" class="form-control" />
        </div>

        <!-- Repeat Password input -->
        <div class="form-outline mb-4">
          <label class="form-label" for="Password">Повтор пароля</label>
          <input type="password" id="password_re" class="form-control" />
        </div>

        <!-- Submit button -->
        <button type="submit" class="btn btn-primary w-100 mb-3">Зарегистрироваться</button>
      </form>
    </div>
  </section>
</template>


<script>
export default {};
</script>

<style lang="scss" scoped>
.container {
  max-width: 600px;
}
</style>
