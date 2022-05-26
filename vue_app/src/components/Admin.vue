<template>
	<section class="container">
		<div class="row">
			<h3>Заявки</h3>
		</div>
		<div class="row">
			<!-- orders list -->
			<ul class="grid list-unstyled py-3">
				<!-- order -->
				<li class="g-col-12 g-col-xl-3" v-for="order in orders" :key="order.id">
					<div class="card">
						<!-- img -->
						<div class="card-img-top ratio ratio-16x9 overflow-hidden">
							<img :src="order.item.images[0].filename" alt="..." />
						</div>

						<!-- body -->
						<div class="card-body">
							<h5 class="card-title">
								<span class="badge  bg-secondary">{{ order.item.type }}</span>
								{{ order.item.rooms }}-комн., {{ order.item.size }}м<sup>2</sup>,
								{{ order.item.floor }}/{{ order.item.total_floor }} этаж
							</h5>
							<p class="card-subtitle">{{ order.item.address }}</p>
							<p class="card-text"><strong>{{ order.item.price }} тыс.р.</strong></p>

							<!-- button -->
							<router-link :to="{ name: 'item', params: { id: order.item.id } }" class="btn btn-secondary">О квартире</router-link>
						</div>
						<ul class="list-group list-group-flush">
							<li class="list-group-item">{{ order.created }}</li>
							<li class="list-group-item">
								<select name="" id="" class="form-control">
									<option value="Обработана">Обработана</option>
									<option value="Ожидание">Ожидание</option>
									<option value="Ожидание" class="bg-danger">Не удалось связаться</option>
								</select>
							</li>
							<li class="list-group-item">
								<button class="btn btn-primary">Сохранит</button>
							</li>
						</ul>
					</div>
				</li>

				<!-- <!-1- create cart -1-> -->
				<!-- <li v-if="currentUser.role=='admin'" class="g-col-12 g-col-xl-3"> -->
				<!-- 	<div class="card new-card justify-content-center align-items-center"> -->
				<!-- 		<router-link :to="{ name: 'create_item' }" class="btn btn-primary">Добавить</router-link> -->
				<!-- 	</div> -->
				<!-- </li> -->
			</ul>
		</div>
	</section>
</template>

<script>
import { orders_list_api } from "../api";

export default {
	data() {
		return {
			orders: Array(),
		};
	},
	methods: {
		async updateOrders() {
			orders_list_api
				.get()
				.then((response) => (this.orders = response["data"]));
		},
	},
	mounted() {
		this.updateOrders();
	},
};
</script>

<style lang="scss" scoped>
img {
	object-fit: cover;
}
</style>
