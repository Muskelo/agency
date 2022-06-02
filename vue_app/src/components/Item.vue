<template>
	<!-- item component -->
	<section>
		<div class="container pt-5">
			<div class="row">
				<div class="col-12 col-xl-6 mb-2 mb-xl-auto">
					<ItemSlider :images="item.images" />
				</div>
				<div class="col-12 col-xl-6 text-center text-xl-start">
					<h2 class="card-title">
						<!-- type badge -->
						<span class="badge bg-secondary">{{ item.type }}</span>
						<!-- info -->
						{{ item.rooms }}-комн., {{ item.size }}м<sup>2</sup>,
						{{ item.floor }}/{{ item.total_floor }} этаж

						<!-- edit button -->
						<router-link :to="{ name: 'edit_item', params: { id: id } }" v-if="currentUser.id == item.user_id || currentUser.hasRole(['admin'])">
							<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 512 512">
								<path d="M362.7 19.32C387.7-5.678 428.3-5.678 453.3 19.32L492.7 58.75C517.7 83.74 517.7 124.3 492.7 149.3L444.3 197.7L314.3 67.72L362.7 19.32zM421.7 220.3L188.5 453.4C178.1 463.8 165.2 471.5 151.1 475.6L30.77 511C22.35 513.5 13.24 511.2 7.03 504.1C.8198 498.8-1.502 489.7 .976 481.2L36.37 360.9C40.53 346.8 48.16 333.9 58.57 323.5L291.7 90.34L421.7 220.3z" />
							</svg>
						</router-link>
						<!-- edit button -->
						<button @click="deleteItem" v-if="currentUser.id == item.user_id || currentUser.hasRole(['admin'])" class="btn">
							<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 448 512">
								<path d="M135.2 17.69C140.6 6.848 151.7 0 163.8 0H284.2C296.3 0 307.4 6.848 312.8 17.69L320 32H416C433.7 32 448 46.33 448 64C448 81.67 433.7 96 416 96H32C14.33 96 0 81.67 0 64C0 46.33 14.33 32 32 32H128L135.2 17.69zM394.8 466.1C393.2 492.3 372.3 512 346.9 512H101.1C75.75 512 54.77 492.3 53.19 466.1L31.1 128H416L394.8 466.1z" />
							</svg>
						</button>
					</h2>
					<p>
						Адресс:
						<strong>г. {{ item.city }}, {{ item.address }}</strong>
					</p>
					<p>
						Цена: <strong>{{ item.price }} тыс.р.</strong>
					</p>
					<p>Описание: {{ item.description }}</p>
					<button @click="makeOrder" class="btn btn-primary" title="Подсказка вверху">
						Связаться
					</button>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
import { item_api, orders_list_api } from "../api";
// stores
import { useCurrentUserStore } from "../stores/currentUser";
import { useAlertsStore } from "../stores/alerts";
// components
import ItemSlider from "./ItemSlider.vue";

export default {
	props: ["id"],
	components: {
		ItemSlider,
	},
	data() {
		return {
			currentUser: useCurrentUserStore(),
			alerts: useAlertsStore(),
			item: {},
		};
	},
	methods: {
		async getItem() {
			await item_api
				.get(this.id)
				.then((response) => (this.item = response["data"]));
		},

		async makeOrder() {
			if (!this.currentUser.id) {
				this.alerts.addAlert(
					"Заявка",
					"Вам нужно авторизоваться для этого"
				);
				return false;
			}
			const request_body = {
				data: { item_id: this.id },
			};

			try {
				const _ = await orders_list_api.post(request_body);
				this.alerts.addAlert(
					"Заявка",
					"Мы составили заявку для нашего специалиста. Мы постараемся связаться с вами как можно раньше",
					"success"
				);
			} catch {
				this.alerts.addAlert(
					"Заявка",
					"Не удалось оставить заявку, попробуйте позже",
					"error"
				);
			}
		},

		async deleteItem() {
			if (!confirm("Вы уверены что хотите удалить этот объект?")) {
				return false;
			}
			try {
				const _ = await item_api.delete(this.id);

				this.$router.push({ name: "home" });

				this.alerts.addAlert("Удаление", "Объект удален", "success");
			} catch {
				this.alerts.addAlert(
					"Удаление",
					"Не удалось удалить объект",
					"error"
				);
			}
		},
	},
	mounted() {
		this.getItem();
	},
};
</script>

<style>
</style>
