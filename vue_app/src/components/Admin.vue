<template>
	<section class="container">
		<Orders />
	</section>
</template>

<script>
import Orders from "./Orders.vue";

export default {
	components: {
		Orders,
	},
};
</script>

<style lang="scss" scoped>
img {
	object-fit: cover;
}
</style>
