<template>
	<div class="row">
		<h3>Заявки</h3>
	</div>
	<div class="row">
		<!-- orders list -->
		<ul class="grid list-unstyled py-3">
			<!-- order -->
			<li class="g-col-12 g-col-xl-3" v-for="order in orders" :key="order.id">
				<div class="card">

					<!-- item info -->
					<div class="card-img-top ratio ratio-16x9 overflow-hidden">
						<img :src="order.item.images[0].filename" alt="..." />
					</div>
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

					<!-- rest order info -->
					<ul class="list-group list-group-flush">
						<li class="list-group-item">Пользователь: {{ order.user.login }}</li>
						<li class="list-group-item">Номер телефона: {{ order.user.number }}</li>
						<li class="list-group-item">Создано: {{ order.created }}</li>
						<li class="list-group-item">
							<select name="" id="" class="form-control">
								<option value="Обработана">Обработана</option>
								<option value="Ожидание">Ожидание</option>
								<option value="Ожидание" class="bg-danger">Не удалось связаться</option>
							</select>
						</li>
						<li class="list-group-item">
							<button class="btn btn-primary">Сохранить</button>
						</li>
					</ul>
				</div>
			</li>
		</ul>
		<nav aria-label="Page navigation example">
			<ul class="pagination">
				<li  class="page-item">
					<button class="page-link" :disabled="offset < 20">Previous</button>
				</li>
				<li class="page-item"><button class="page-link" href="#">Previous</button></li>
				<li class="page-item"><button class="page-link" href="#">Previous</button></li>
				<li class="page-item"><button class="page-link" href="#">Previous</button></li>
			</ul>
		</nav>
	</div>
</template>

<script>
import { orders_list_api } from "../api";

export default {
	data() {
		return {
			orders: Array(),
			offset: 0,
		};
	},
	methods: {
		async updateOrders() {
			orders_list_api
				.get(`?offset=${this.offset}`)
				.then((response) => (this.orders = response["data"]));
		},
	},
	watch: {
		// whenever question changes, this function will run
		offset(newOffset, oldOffset) {
			this.updateOrders();
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
