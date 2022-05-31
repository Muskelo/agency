<template>
	<li class="g-col-12 g-col-xl-3">
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

					<lable class="form-lable">Статуc</lable>
					<select v-model="order_status" class="form-control">
						<option value="Новая">Новая</option>
						<option value="В обработке">В обработке</option>
						<option value="Закрытая">Закрытая</option>
					</select>
				</li>
				<li class="list-group-item">
					<lable class="form-lable">Комментарий</lable>
					<textarea v-model="order_comment" cols="30" rows="5" class="form-control"></textarea>
				</li>
				<li class="list-group-item d-flex justify-content-between">
					<button @click="patchOrder" class="btn btn-primary">Сохранить</button>
					<button @click="deleteOrder" class="btn btn-danger">Удалить</button>
				</li>
			</ul>
		</div>
	</li>
</template>

<script>
import { order_api } from "../api";

export default {
	props: ["order"],
	data() {
		return {
			order_status: this.order.status,
			order_comment: this.order.comment,
		};
	},
	methods: {
		async patchOrder() {
			const data = {
				data: {
					status: this.order_status,
					comment: this.order_comment,
				},
			};
			const response = await order_api.patch(this.order.id, data);
		},
		async deleteOrder() {
			const response = await order_api.delete(this.order.id);
			this.$emit("delete");
		},
	},
};
</script>

<style>
</style>
