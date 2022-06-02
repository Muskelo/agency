<template>
	<!-- create item component -->
	<section>
		<form class="container py-3">
			<!-- title -->
			<div class="row px-2">
				<h4>Изменить объект</h4>
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
					<input v-model="size" type="number" class="form-control" required />
				</div>
				<div>
					<label class="form-label">Цена, тыс.р.</label>
					<input v-model="price" type="number" class="form-control" required />
				</div>
				<div>
					<label class="form-label">Комнат</label>
					<input v-model="rooms" type="number" class="form-control" required />
				</div>
				<div>
					<label class="form-label">Этаж</label>
					<input v-model="floor" type="number" class="form-control" required />
				</div>
				<div>
					<label class="form-label">Всего этаже</label>
					<input v-model="total_floor" type="number" class="form-control" required />
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
					<input list="cities" v-model="city" type="text" class="form-control" required />
					<dataList></dataList>
				</div>
				<div>
					<label class="form-label">Аддрес</label>
					<input v-model="address" type="text" class="form-control" required />
				</div>
				<div class="w-100">
					<label class="form-label">Описание</label>
					<textarea class="form-control" v-model="description" required></textarea>
				</div>
				<div class="w-100 d-flex justify-content-center">
					<button type="submit" @click="updateItem" class="btn btn-primary">
						Сохранить
					</button>
				</div>
			</div>
		</form>
	</section>
</template>

<script>
import { image_api, item_api } from "../api";
// stores
import { useCurrentUserStore } from "../stores/currentUser";
import { useAlertsStore } from "../stores/alerts";
// components
import dataList from "../components/dataList.vue";

export default {
	props: ["id"],
	data() {
		return {
			currentUser: useCurrentUserStore(),
			alerts: useAlertsStore(),

			// data
			images: Array(),
			size: undefined,
			price: undefined,
			rooms: undefined,
			floor: undefined,
			total_floor: undefined,
			type: "Квартира",
			city: undefined,
			address: undefined,
			description: undefined,
			images_id: undefined,
		};
	},
	components: { dataList },
	methods: {
		async getItem() {
			await item_api.get(this.id).then((response) => {
				const item = response["data"];
				for (let key in item) {
					if (key == "id") {
						continue;
					}
					this[key] = item[key];
				}
			});
		},

		async uploadImage(event) {
			const image = event.target.files[0];
			const data = new FormData();
			data.append("image", image);

			const response = await fetch(`/api/images/?item_id=${this.id}`, {
				method: "POST",
				body: data,
				headers: {
					Authorization: this.currentUser.auth_header,
				},
			});
			if (response.status >= 200 && response.status < 300) {
				// update images
				this.getItem();
			} else {
				this.alerts.addAlert(
					"Добавка изображения",
					"Не удалось добавить изображение",
					"error"
				);
			}
		},

		async deleteImage(id) {
			if (this.images.length == 1) {
				this.alerts.addAlert(
					"Удаление изображения.",
					"Нужно хотябы 1 изображение."
				);
				return false;
			}

			try {
				const _ = await image_api.delete(id);
				// update images
				this.getItem();
			} catch (error) {
				this.alerts.addAlert(
					"Удаление изображения",
					"Не удалось удалить изображение",
					"error"
				);
			}
		},

		async updateItem() {
			const images_id = Array.from(this.images, (x) => x.id);
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
					images_id,
				},
			};
			try {
				const _ = await item_api.patch(this.id, data);
				// go to updatet item
				this.$router.push({ name: "item", params: { id: this.id } });
			} catch {
				this.alerts.addAlert(
					"Изменение объекта",
					"Не удалось изменить объект",
					"error"
				);
			}
		},
		show(id) {
			console.log(id);
		},
	},
	mounted() {
		this.getItem();
	},
};
</script>

<style lang="scss" scoped>
img {
	object-fit: contain;
}
</style>
