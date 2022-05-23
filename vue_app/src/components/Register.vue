<template>
	<section class="container py-3">
		<!-- Pills content -->
		<div class="tab-pane fade show active" id="pills-register" role="tabpanel" aria-labelledby="tab-register">
			<form>
				<h4 class="text-center">Регистрация</h4>

				<!-- Login input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="login">Логин</label>
					<input type="text" v-model="login" id="login" class="form-control" />
				</div>

				<!-- Number input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="number">Телефон</label>
					<input type="text" v-model="number" id="number" class="form-control" />
				</div>

				<!-- Password input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="password">Пароль</label>
					<input type="password" v-model="password" id="password" class="form-control" />
				</div>

				<!-- Repeat Password input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="Password">Повтор пароля</label>
					<input type="password" v-model="password_re" id="password_re" class="form-control" />
				</div>

				<!-- Submit button -->
				<router-link :to="{ name: 'home' }" type="submit" @click="register" class="btn btn-primary w-100 mb-3">Зарегистрироваться</router-link>
			</form>
		</div>
	</section>
</template>


<script>
import { useCurrentUserStore } from "../stores/currentUser";
export default {
	data() {
		const currentUser = useCurrentUserStore();

		return {
			currentUser,
			// data
			login: undefined,
			number: undefined,
			password: undefined,
			password_re: undefined,
		};
	},
	methods: {
		async register() {
			const user_data = {
				login: this.login,
				number: this.number,
				password: this.password,
			};
			await this.currentUser.register(user_data);
		},
	},
};
</script>

<style lang="scss" scoped>
.container {
	max-width: 600px;
}
</style>
