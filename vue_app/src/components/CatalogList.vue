<template>
	<!-- catalog list component -->
	<div class="wrapper">
		<div class="container">
			<!-- items list -->
			<ul class="grid list-unstyled py-3">
				<!-- item -->
				<li class="g-col-12 g-col-xl-3" v-for="item in catalog.items" :key="item.id">
					<div class="card">
						<!-- img -->
						<div class="card-img-top ratio ratio-16x9 overflow-hidden">
							<img :src="item.images[0].filename" alt="..." />
						</div>

						<!-- body -->
						<div class="card-body">
							<h5 class="card-title">
								<span class="badge  bg-secondary">{{ item.type }}</span>
								{{ item.rooms }}-комн., {{ item.size }}м<sup>2</sup>,
								{{ item.floor }}/{{ item.total_floor }} этаж
							</h5>
							<p class="card-subtitle">{{ item.address }}</p>
							<p class="card-text"><strong>{{ item.price }} тыс.р.</strong></p>

							<!-- button -->
							<router-link :to="{ name: 'item', params: { id: item.id } }" class="btn btn-primary">Подробнее</router-link>
						</div>
					</div>
				</li>

				<!-- create cart -->
				<li v-if="currentUser.hasRole(['admin', 'moder'])" class="g-col-12 g-col-xl-3">
					<div class="card new-card justify-content-center align-items-center">
						<router-link :to="{ name: 'create_item' }" class="btn btn-primary">Добавить</router-link>
					</div>
				</li>
			</ul>

			<!-- pagination -->
			<div class="row">
				<nav class="d-flex justify-content-center" aria-label="Page navigation example">
					<ul class="pagination">
						<li class="page-item">
							<button @click="catalog.offset -= 20" :disabled="catalog.offset == 0" class="page-link">Назад</button>
						</li>
						<li v-for="(page, index) in catalog.pages" :key="index" :class="{ active: catalog.offset==(page-1)*20 }" class="page-item">
							<button class="page-link" @click="catalog.offset=(page-1)*20">{{page}}</button>
						</li>
						<li class="page-item">
							<button @click="catalog.offset += 20" :disabled="catalog.offset == (catalog.pages-1)*20" class="page-link">Вперед</button>
						</li>
					</ul>
				</nav>
			</div>
		</div>
	</div>
</template>

<script>
import { useCurrentUserStore } from "../stores/currentUser.js";
import { useCatalogStore } from "../stores/catalog.js";

export default {
	props: ["items"],
	data() {
		let currentUser = useCurrentUserStore();
		let catalog = useCatalogStore();
		return {
			currentUser,
			catalog,
		};
	},
	watch: {
		// whenever question changes, this function will run
        'catalog.offset'(newOffset, oldOffset) {
			this.catalog.updateCatalog();
		},
	},
};
</script>

<style lang="scss" scoped>
img {
	object-fit: cover;
}

.new-card {
	min-height: 300px;
	height: 100%;
	background-color: #ddd;
}
</style>
