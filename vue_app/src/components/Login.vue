<template>
	<section class="container py-3">
		<!-- Pills content -->
		<div class="tab-content">
			<div class="tab-pane fade show active" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
				<form @submit="login_f">
					<h4 class="text-center">Вход</h4>
					<!-- login input -->
					<div class="form-outline mb-4">
						<label class="form-label" for="login">Логин</label>
						<input v-model="login" type="text" id="login" class="form-control" required minlength="5" />
					</div>

					<!-- Password input -->
					<div class="form-outline mb-4">
						<label class="form-label" for="password">Пароль</label>
						<input v-model="password" type="password" id="password" class="form-control" required minlength="5" />
					</div>

					<!-- Submit button -->
					<button type="submit" class="btn btn-primary mb-4 w-100">Войти</button>
				</form>
			</div>
		</div>
		<!-- Pills content -->
	</section>
</template>

<script>
import { useCurrentUserStore } from "../stores/currentUser.js";
import { useAlertsStore} from "../stores/alerts";
export default {
	data() {
		let currentUser = useCurrentUserStore();

		return {
			login: undefined,
			password: undefined,
			currentUser,
            alerts: useAlertsStore()
		};
	},
	methods: {
		async login_f() {
			const user_id = await this.currentUser.login_f(
				this.login,
				this.password
			);
			if (this.currentUser.id) {
				this.alerts.addAlert("Авторизация", "Вы вошли.", "success");
				this.$router.push({ name: "home" });
			}
            console.log(this.currentUser.id);
		},
	},
};
</script>

<style lang="scss" scoped>
.container {
	max-width: 600px;
}
</style>
