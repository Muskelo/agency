<template>
	<div class="toasts">
		<div v-for="(alert_, index) in alerts.data" :key="index" :class="alert_.type" class="toast show">
			<div class="toast-header">
				<strong class="me-auto">{{alert_.title}}</strong>
				<button @click="alerts.deleteAlert(index)" class="btn-close"></button>
			</div>
			<div class="toast-body">
				{{ alert_.message }}
			</div>
		</div>
	</div>
</template>

<script>
import { useAlertsStore } from "../stores/alerts";

export default {
	data() {
		const alerts = useAlertsStore();

		return {
			alerts,
		};
	},
};
</script>

<style lang="scss" scoped>
.toasts {
	position: fixed;
	bottom: 24px;
	right: 24px;
}
.success .toast-header {
	background-color: rgba(176, 251, 170, 0.85);
}
.error .toast-header {
	background-color: rgba(255, 178, 174, 0.85);
}
</style>
