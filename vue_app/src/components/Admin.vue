<template>
	<section class="container">
		<OrdersList />
		<UsersList v-if="currentUser.hasRole('admin')" />
	</section>
</template>

<script>
import OrdersList from "./OrdersList.vue";
import UsersList from "./UsersList.vue";
import { useCurrentUserStore } from "../stores/currentUser";

export default {
	data() {
		return {
			currentUser: useCurrentUserStore(),
		};
	},
	components: {
		OrdersList,
		UsersList,
	},
};
</script>

<style lang="scss" scoped>
img {
	object-fit: cover;
}
</style>
