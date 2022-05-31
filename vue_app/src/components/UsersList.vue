<template>
	<h3>Пользователи</h3>
	<!-- pagination -->
	<div class="row">
		<nav class="d-flex justify-content-center" aria-label="Page navigation example">
			<ul class="pagination">
				<li class="page-item">
					<button @click="offset -= 20" :disabled="offset == 20" class="page-link">Назад</button>
				</li>
				<li v-for="(page, index) in pages" :key="index" :class="{ active: offset==(page-1)*20 }" class="page-item">
					<button class="page-link" @click="offset=(page-1)*20">{{page}}</button>
				</li>
				<li class="page-item">
					<button @click="offset += 20" :disabled="offset == (pages-1)*20" class="page-link">Вперед</button>
				</li>
			</ul>
		</nav>
	</div>
	<table class="table">
		<thead>
			<tr>
				<th scope="col">#</th>
				<th scope="col">Логин</th>
				<th scope="col">Телефон</th>
				<th scope="col">Роль</th>
				<th scope="col"></th>
			</tr>
		</thead>
		<tbody>
			<UsersItem v-for="user in users" :key="user.id" :user="user" />
		</tbody>
	</table>
	<!-- pagination -->
	<div class="row">
		<nav class="d-flex justify-content-center" aria-label="Page navigation example">
			<ul class="pagination">
				<li class="page-item">
					<button @click="offset -= 20" :disabled="offset == 20" class="page-link">Назад</button>
				</li>
				<li v-for="(page, index) in pages" :key="index" :class="{ active: offset==(page-1)*20 }" class="page-item">
					<button class="page-link" @click="offset=(page-1)*20">{{page}}</button>
				</li>
				<li class="page-item">
					<button @click="offset += 20" :disabled="offset == (pages-1)*20" class="page-link">Вперед</button>
				</li>
			</ul>
		</nav>
	</div>
</template>

<script>
import { users_list_api } from "../api";
import UsersItem from "./UsersItem.vue";

export default {
	data() {
		return {
			users: Array(),
			offset: 0,
			total: 0,
			pages: 0,
		};
	},
	methods: {
		async updateUsersList() {
			users_list_api.get().then((response) => {
				this.users = response["data"];
				this.total = response["total"];
				this.pages = Math.ceil(this.total / 20);
			});
		},
	},
	watch: {
		// whenever question changes, this function will run
		offset(newOffset, oldOffset) {
			this.updateUsersList();
		},
	},
	mounted() {
		this.updateUsersList();
	},
	components: {
		UsersItem,
	},
};
</script>

<style>
</style>
