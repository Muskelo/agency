<template>
	<!-- catalog title component -->
	<div class="wrapper">
		<div class="container py-5">

			<div class="row mb-4">
				<h1>Перемены к лучшему!</h1>
			</div>

			<div class="row">
				<div class="col-xl-11 mb-3">
					<form class="list-group list-group-horizontal-xl">
						<!-- city -->
						<input v-model="city" type="text" list="cities" class="list-group-item col-xl-3" placeholder="Город">
						<dataList></dataList>
						<!-- type -->
						<select v-model="type" class="list-group-item col-xl-2">
							<option value="">Выбрать тип</option>
							<option value="Квартира">Квартира</option>
							<option value="Дом">Дом</option>
							<option value="Дача">Дача</option>
						</select>
						<!-- rooms -->
						<input v-model="rooms" type="number" class="list-group-item col-xl-2" placeholder="Комнат">
						<!-- price label -->
						<label class="list-group-item col-xl-1 text-xl-end">Цена:</label>
						<!-- mix price -->
						<input v-model="min_price" type="number" class="list-group-item col-xl-2" placeholder="От">
						<!-- max price -->
						<input v-model="max_price" type="number" class="list-group-item col-xl-2" placeholder="До">
					</form>
				</div>
				<div class="mx-auto col-auto col-xl-1">
					<button @click="search" class="btn btn-primary">Поиск</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import dataList from "../components/dataList.vue";
import { useCatalogStore } from "../stores/catalog.js";

export default {
	data() {
		const catalog = useCatalogStore();
		return {
			catalog,
			city: "Казань",
			type: "",
			rooms: "",
			min_price: "",
			max_price: "",
		};
	},
	components: {
		dataList,
	},
	methods: {
		async search() {
			this.catalog.updateCatalog(
				this.city,
				this.type,
				this.rooms,
				this.min_price,
				this.max_price
			);
		},
	},
    mounted() {
        this.search();
    }
};
</script>

<style lang="scss" scoped>
.wrapper {
	background: url(title.jpg) center center;
	background-size: cover;
}
h1 {
	color: white;
}
</style>
