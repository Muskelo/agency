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
						<router-link :to="{ name: 'edit_item', params: { id: id } }" v-if="currentUser.id == item.user_id">
							<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 512 512">
								<path d="M362.7 19.32C387.7-5.678 428.3-5.678 453.3 19.32L492.7 58.75C517.7 83.74 517.7 124.3 492.7 149.3L444.3 197.7L314.3 67.72L362.7 19.32zM421.7 220.3L188.5 453.4C178.1 463.8 165.2 471.5 151.1 475.6L30.77 511C22.35 513.5 13.24 511.2 7.03 504.1C.8198 498.8-1.502 489.7 .976 481.2L36.37 360.9C40.53 346.8 48.16 333.9 58.57 323.5L291.7 90.34L421.7 220.3z" />
							</svg>
						</router-link>
					</h2>
					<p>
						Адресс:
						<strong>г. {{ item.city }}, {{ item.address }}</strong>
					</p>
					<p>
						Цена: <strong>{{ item.price }} тыс.р.</strong>
					</p>
					<p>Описание: {{ item.description }}</p>
					<button @click="makeOrder" :disabled="!currentUser.id" class="btn btn-primary">
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
			const request_body = {
				data: { item_id: this.id },
			};
			orders_list_api.post(request_body).then((response) => {
				this.alerts.addAlert(
					"Заявка",
					"Мы составили заявку для нашего специалиста. Мы постараемся связаться с вами как можно раньше.",
					"success"
				);
			});
		},
	},
	mounted() {
		this.getItem();
	},
};
</script>

<style>
</style>
