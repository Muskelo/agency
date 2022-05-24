<template>
	<!-- DATA LIST CITIES START  -->
	<datalist id="cities">
		<option v-for="city in cities" :key="city.city" :value="city.city" />
	</datalist>
	<!-- DATA LIST CITIES END  -->
</template>

<script>
import json from "../assets/russia.json";

export default {
	data() {
		return {
			cities: json,
		};
	},
};
</script>

<style>
</style>
