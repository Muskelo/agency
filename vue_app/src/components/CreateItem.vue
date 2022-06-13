<template>
	<!-- create item component -->
	<section>
		<form @submit="createItem" class="container py-3">
			<!-- title -->
			<div class="row px-2">
				<h4>Добавление нового объекта</h4>
			</div>

			<!-- images title -->
			<div class="row px-2">
				<h5>Изображения</h5>
			</div>

			<!-- grid images -->
			<div class="row mb-2">
				<div class="grid">
					<!-- grid item -->
					<div v-for="image in images" :key="image.id" class="g-col-12 g-col-xl-6 position-relative">
						<!-- image -->
						<div class="ratio ratio-16x9">
							<img :src="image.filename" alt="image.filename" />
						</div>
						<!-- button -->
						<button @click="deleteImage(image.id)" class="btn btn-danger position-absolute bottom-0 end-0 translate-middle">
							Удалить
						</button>
					</div>
				</div>
			</div>

			<!-- add images -->
			<div class="row mb-3">
				<div class="d-flex align-items-center justify-content-between">
					<input @change="uploadImage" type="file" name="image" class="form-control" />
				</div>
			</div>

			<!-- rest data -->
			<div class="row px-2">
				<h5>Данные</h5>
			</div>

			<div class="row row-cols-xl-2 g-2">
				<div>
					<label class="form-label">Площадь</label>
					<input v-model="size" type="number" class="form-control" required pattern="^[1-9]+$" />
				</div>
				<div>
					<label class="form-label">Цена, тыс.р.</label>
					<input v-model="price" type="number" class="form-control" required pattern="^[1-9]+$" />
				</div>
				<div>
					<label class="form-label">Комнат</label>
					<input v-model="rooms" type="number" class="form-control" required pattern="^[1-9]+$" />
				</div>
				<div>
					<label class="form-label">Этаж</label>
					<input v-model="floor" type="number" class="form-control" required pattern="^[1-9]+$" />
				</div>
				<div>
					<label class="form-label">Всего этаже</label>
					<input v-model="total_floor" type="number" class="form-control" required pattern="^[1-9]+$" />
				</div>
				<div>
					<label class="form-label">Тип</label>
					<select v-model="type" class="form-select" required>
						<option selected value="Квартира">Квартира</option>
						<option value="Дом">Дом</option>
						<option value="Дача">Дача</option>
					</select>
				</div>
				<div>
					<label class="form-label">Город</label>
					<input list="cities" v-model="city" type="text" class="form-control" required minlength="3" />
					<dataList></dataList>
				</div>
				<div>
					<label class="form-label">Аддрес</label>
					<input v-model="address" type="text" class="form-control" required minlength="5" />
				</div>
				<div class="w-100">
					<label class="form-label">Описание</label>
					<textarea class="form-control" v-model="description" required></textarea>
				</div>
				<div class="w-100 d-flex justify-content-center">
					<button type="submit" class="btn btn-primary">
						Добавить
					</button>
				</div>
			</div>
		</form>
	</section>
</template>

<script>
import { images_list_api, image_api, items_list_api } from "../api";
import { useCurrentUserStore } from "../stores/currentUser";
import { useAlertsStore } from "../stores/alerts";
import { useCatalogStore } from "../stores/catalog";

import dataList from "../components/dataList.vue";

export default {
	data() {
		let alerts = useAlertsStore();

		return {
			currentUser: useCurrentUserStore(),
			alerts,
			catalog: useCatalogStore(),
			images: Array(),
			// data
			size: undefined,
			price: undefined,
			rooms: undefined,
			floor: undefined,
			total_floor: undefined,
			type: "Квартира",
			city: "Казань",
			address: undefined,
			description: undefined,
		};
	},
	components: { dataList },
	methods: {
		// ITEMS METHODS
		async createItem() {
			const images_id = Array.from(this.images, (x) => x.id);
			if (images_id.length == 0) {
				this.alerts.addAlert(
					"Добавление",
					"Нужно хотябы 1 изображение"
				);
				return false;
			}

			const data = {
				data: {
					size: this.size,
					price: this.price,
					rooms: this.rooms,
					floor: this.floor,
					total_floor: this.total_floor,
					type: this.type,
					city: this.city,
					address: this.address,
					description: this.description,
					images_id: images_id,
				},
			};

			try {
				const response = await items_list_api.post(data);

                await this.catalog.updateCatalog();

				// go to created item
				this.$router.push({
					name: "item",
					params: { id: response.data.id },
				});
			} catch {
				this.alerts.addAlert(
					"Добавление",
					"Неудалось создать объект.",
					"error"
				);
			}
		},
		// IMAGES METHODS
		async updateImages() {
			const response = await images_list_api.get();
			this.images = await response["data"];
		},
		async uploadImage(event) {
			const image = event.target.files[0];
			const data = new FormData();
			data.append("image", image);

			await fetch("/api/images/", {
				method: "POST",
				body: data,
				headers: { Authorization: this.currentUser.auth_header },
			});

			// update images
			this.updateImages();
		},
		async deleteImage(id) {
			await image_api.delete(id);

			// update images
			this.updateImages();
		},
	},
	mounted() {
		this.updateImages();
	},
};
</script>

<style lang="scss" scoped>
img {
	object-fit: contain;
}
</style>
