<template>
	<section class="container py-3">
		<!-- Pills content -->
		<div class="tab-pane fade show active" id="pills-register" role="tabpanel" aria-labelledby="tab-register">
			<form @submit.prevent="register">
				<h4 class="text-center">Регистрация</h4>

				<!-- Login input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="login">Логин</label>
					<input type="text" v-model="login" id="login" class="form-control" required minlength="5"/>
				</div>

				<!-- Number input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="number">Телефон</label>
                    <input type="text" v-model="number" id="number" class="form-control" required minlength="11" maxlength="11" pattern="^[1-9]+$"/>
				</div>

				<!-- Password input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="password">Пароль</label>
					<input type="password" v-model="password" id="password" class="form-control" required minlength="5"/>
				</div>


				<div class="form-outline mb-4 text-center">
					<label class="form-label mx-1" for="password">Согласие на обработку персональных данных</label>
                    <input type="checkbox" class="" required>
				</div>

				<!-- Submit button -->
				<button type="submit"  class="btn btn-primary w-100 mb-3">Зарегистрироваться</button>
			</form>
		</div>
	</section>
</template>


<script>
import { useCurrentUserStore } from "../stores/currentUser";
import { useAlertsStore } from "../stores/alerts.js";
export default {
	data() {
		return {
			currentUser: useCurrentUserStore(),
			alerts: useAlertsStore(),
			// data
			login: undefined,
			number: undefined,
			password: undefined,
		};
	},
	methods: {
		async register() {
			const user_data = {
				login: this.login,
				number: this.number,
				password: this.password,
			};

			try {
				const response = await this.currentUser.register(user_data);
				this.$router.push({ name: "home" });
				this.alerts.addAlert(
					"Регистрация",
					"Регистрация прошла успено.",
					"success"
				);
			} catch (error) {
				console.log(error.message);
				if (error.message == "BAD REQUEST") {
					this.alerts.addAlert(
						"Регистрация",
						"Не верные данные",
						"error"
					);
				} else if (error.message == "CONFLICT") {
					this.alerts.addAlert(
						"Регистрация",
						"Пользователь с таким логином или телефоном уже существует",
						"error"
					);
				}
			}
		},
	},
};
</script>

<style lang="scss" scoped>
.container {
	max-width: 600px;
}
</style>
