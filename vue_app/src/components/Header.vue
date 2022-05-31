<template>
	<!-- header component -->
	<header class="navbar navbar-expand-lg shadow-sm">
		<div class="container d-flex justify-content-between align-items-center">
			<!-- logo -->
			<router-link to="/" class="navbar-brand">AGENCY</router-link>

			<!-- menu button -->
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
					<path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z" />
				</svg>
			</button>

			<!-- menu -->
			<div class="collapse navbar-collapse flex-grow-0" id="navbarSupportedContent">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0">
					<!-- admin  -->
					<li v-if="currentUser.hasRole(['admin', 'moder'])" class="nav-item mx-1">
						<router-link :to="{name: 'admin'}" class="nav-link">Админ. панель</router-link>
					</li>
					<!-- login -->
					<li class="nav-item my-1 mx-lg-1" v-if="!currentUser.id">
						<router-link :to="{ name: 'login' }" class="btn btn-primary">Вход</router-link>
					</li>
					<!-- register -->
					<li class="nav-item my-1 mx-lg-1" v-if="!currentUser.id">
						<router-link :to="{ name: 'register' }" class="btn btn-primary">Регистрация</router-link>
					</li>
					<!-- logout -->
					<li class="nav-item my-1 mx-lg-1" v-if="currentUser.id">
						<router-link :to="{name: 'home'}" @click="currentUser.logout" class="btn btn-primary">
							Выход
						</router-link>
					</li>
				</ul>
			</div>
		</div>
	</header>
</template>

<script>
import { useCurrentUserStore } from "../stores/currentUser.js";

export default {
	data() {
		return {
			currentUser: useCurrentUserStore(),
		};
	},
};
</script>

<style lang="scss" scoped>
</style>

