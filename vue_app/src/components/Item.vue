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
import { item_api } from "../api";
import ItemSlider from "./ItemSlider.vue";

export default {
	props: ["id"],
	components: {
		ItemSlider,
	},
	data() {
		return {
			item: {},
		};
	},
	methods: {
		async getItem() {
			await item_api
				.get(this.id)
				.then((response) => (this.item = response["data"]));
		},
	},
	mounted() {
		this.getItem();
	},
};
</script>

<style>
</style>
