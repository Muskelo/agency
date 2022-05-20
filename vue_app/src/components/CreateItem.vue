<template>
	<!-- create item component -->
	<section>
		<div class="container py-3">
			<!-- title -->
			<div class="row">
				<h4>Добавление нового объекта</h4>
			</div>

			<!-- image adding -->
			<div class="row">
				<h5>Изображения</h5>
			</div>
			<div class="row g-2 mb-3">
				<!-- slider -->
				<CreateItemSlider ref="slider" />
			</div>

			<!-- rest data -->
			<div class="row">
				<h5>Данные</h5>
			</div>

			<div class="mb-3 row">
				<label for="email" class="col-sm-2 col-form-label">Email</label>
				<div class="col-sm-10">
					<input
						type="text"
						class="form-control"
						id="email"
						placeholder="email"
					/>
				</div>
			</div>
		</div>
	</section>
	<button @click="showId">show</button>
</template>

<script>
import { images_list_api } from "../api";
import { image_api } from "../api";
import { useCurrentUserStore } from "../stores/currentUser";
// components
import CreateItemSlider from "./CreateItemSlider.vue";

export default {
	components: {
		CreateItemSlider,
	},
	data() {
		let currentUser = useCurrentUserStore();
		return {
			images: Array(),
			activeImageId: undefined,
			currentUser,
		};
	},
	methods: {
		async getImages() {
			const response = await images_list_api.get();
			this.images = await response["data"];
		},
		showId() {
			console.log(this.getActiveImageId());
		},
		getActiveImageId() {
			// get images
			const images = this.$refs.slider.$refs.images;

			for (let key in images) {
				if (images[key].classList.contains("active")) {
					this.activeImageId = images[key].id;
					return images[key].id;
				}
			}
		},
		async uploadImage(event) {
			let image = event.target.files[0];
			let data = new FormData();
			data.append("image", image);

			await fetch("/api/images/", {
				method: "POST",
				body: data,
				headers: { Authorization: this.currentUser.auth_header },
			})
				.then((response) => response.json())
				.then((response_body) => console.log(response_body));

			// update images
			this.getImages();
		},
		async deleteImage() {
			let image_id = this.getActiveImageId();
			await image_api.delete(image_id);

			// update images
			await this.getImages();

			this.$refs.slider.$forceUpdate();
		},
	},
	mounted() {
		this.getImages();
	},
};
</script>

<style>
</style>
