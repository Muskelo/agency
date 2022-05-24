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
						<input type="text" list="cities" class="list-group-item col-xl-3" placeholder="Город">
						<input type="number" class="list-group-item col-xl-2" placeholder="Комнат">
						<input type="text" class="list-group-item col-xl-7" placeholder="Улица, адресс...">
					</form>
				</div>
				<!-- DATA LIST CITIES START  -->
				<datalist id="cities">
					<option v-for="city in cities" :key="city.city" :value="city.city" />
				</datalist>
				<!-- DATA LIST CITIES END  -->
				<div class="mx-auto col-auto col-xl-1">
					<button class="btn btn-primary">Поиск</button>
				</div>
			</div>

		</div>
	</div>
</template>

<script>
import json from "../assets/russia.json";

export default {
	data() {
		return {
			cities: json,
		};
	},
	methods: {
		async init() {
			const fd = await open("../assets/russia.json");
			console.log(fd);
			const cities = await fd.readFile();

			console.log(cities);
		},
	},
	mounted() {},
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
