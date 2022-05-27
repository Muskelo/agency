<template>
	<!-- pagination -->
	<div class="row">
		<nav class="d-flex justify-content-center" aria-label="Page navigation example">
			<ul class="pagination">
				<li class="page-item">
					<button @click="offset =- 20" :disabled="offset < 20" class="page-link">Назад</button>
				</li>
				<li v-for="(page, index) in pages" :key="index" class="page-item">
					<button class="page-link" @click="offset=(page-1)*20">{{page}}</button>
				</li>
				<li class="page-item">
					<button @click="offset =- 20" :disabled="offset < 20" class="page-link">Вперед</button>
				</li>
			</ul>
		</nav>
	</div>
</template>

<script>
export default {
	props: ["pages", "offset"],
};
</script>

<style>
</style>
