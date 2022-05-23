<template>
	<!-- slider -->
	<div id="carouselCreateItem" v-if="slider" class="carousel slide" data-bs-interval="false">
		<div class="carousel-inner ratio ratio-16x9">
			<!-- images list-->
			<div v-for="(image, index) in images" :key="image.id" :id="image.id" :class="{ active: index  === 0 }" ref="images" class="carousel-item">
				<img :src="image.filename" class="d-block w-100" alt="..." />
			</div>

			<!-- if no images -->
			<div v-if="!images.length" class="empty"></div>
		</div>

		<!-- prev button -->
		<button class="carousel-control-prev" type="button" data-bs-target="#carouselCreateItem" data-bs-slide="prev">
			<span class="carousel-control-prev-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Previous</span>
		</button>
		<!-- next button -->
		<button class="carousel-control-next" type="button" data-bs-target="#carouselCreateItem" data-bs-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Next</span>
		</button>
	</div>

	<!-- add/delete image -->
	<div class="d-flex align-items-center justify-content-between">
		<input @change="uploadImage" type="file" name="image" class="form-control" />

		<button @click="deleteImage" class="btn btn-danger">Удалить</button>
	</div>
</template>

<script>
import { images_list_api } from "../api";
import { image_api } from "../api";
import { useCurrentUserStore } from "../stores/currentUser";

export default {
	data() {
		let currentUser = useCurrentUserStore();
		return {
			images: [],
			slider: 1,
			currentUser,
		};
	},
	methods: {
		async updateImages() {
			const response = await images_list_api.get();
			this.images = await response["data"];
            console.log(this.$refs.images);
		},
		getActiveImageId() {
			// get images
			const images = this.$refs.images;

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
			this.updateImages();
		},
		async deleteImage() {
			let image_id = this.getActiveImageId();
			await image_api.delete(image_id);

			// update images
			await this.updateImages();
            this.$refs.images[1].classList.push("active")
            // this.$refs.images[0].classList.append("active")
		},
	},
	mounted() {
		this.updateImages();
	},
};
</script>

<style lang="scss" scoped>
.empty {
	background-color: #ddd;
}
</style>
