<template>
	<div class="row">
		<h3>Заявки</h3>
	</div>
	<!-- pagination -->
	<div class="row">
		<nav class="d-flex justify-content-center" aria-label="Page navigation example">
			<ul class="pagination">
				<li class="page-item">
					<button @click="offset -= 20" :disabled="offset == 20" class="page-link">Назад</button>
				</li>
				<li v-for="(page, index) in pages" :key="index" :class="{ active: offset==(page-1)*20 }" class="page-item">
					<button class="page-link" @click="offset=(page-1)*20">{{page}}</button>
				</li>
				<li class="page-item">
					<button @click="offset += 20" :disabled="offset == (pages-1)*20" class="page-link">Вперед</button>
				</li>
			</ul>
		</nav>
	</div>
	<div class="row">
		<!-- orders list -->
		<ul class="grid list-unstyled py-3">
			<!-- order -->
			<OrdersItem v-for="order in orders" :key="order.id" :order="order" @delete="updateOrders" />
		</ul>
	</div>
	<!-- pagination -->
	<div class="row">
		<nav class="d-flex justify-content-center" aria-label="Page navigation example">
			<ul class="pagination">
				<li class="page-item">
					<button @click="offset -= 20" :disabled="offset == 20" class="page-link">Назад</button>
				</li>
				<li v-for="(page, index) in pages" :key="index" :class="{ active: offset==(page-1)*20 }" class="page-item">
					<button class="page-link" @click="offset=(page-1)*20">{{page}}</button>
				</li>
				<li class="page-item">
					<button @click="offset += 20" :disabled="offset == (pages-1)*20" class="page-link">Вперед</button>
				</li>
			</ul>
		</nav>
	</div>
</template>

<script>
import { orders_list_api } from "../api";
import OrdersItem from "./OrdersItem.vue";

export default {
	data() {
		return {
			orders: Array(),
			offset: 0,
			total: 0,
			pages: 0,
		};
	},
	methods: {
		async updateOrders() {
			orders_list_api.get(`?offset=${this.offset}`).then((response) => {
				this.orders = response["data"];
				this.total = response["total"];
				this.pages = Math.ceil(this.total / 20);
			});
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
	components: {
		OrdersItem,
	},
};
</script>

<style lang="scss" scoped>
img {
	object-fit: cover;
}
</style>
