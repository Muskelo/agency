<template>

	<div class="row">
		<div class="col-6">
			<h3>Пользователи</h3>
		</div>
		<div class="search col-6 d-flex g-2">
			<input v-model="search" class="form-control" type="text">
			<button @click="updateUsersList" class="mx-2 btn btn-primary">Поиск</button>
		</div>
	</div>
	<div class="row">
		<table class="table">
			<thead>
				<tr>
					<th scope="col">#</th>
					<th scope="col">Логин</th>
					<th scope="col">Телефон</th>
					<th scope="col">Роль</th>
				</tr>
			</thead>
			<tbody>
				<UsersItem v-for="user in users" :key="user.id" :user="user" />
			</tbody>
		</table>
	</div>
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
			search: "",
		};
	},
	methods: {
		async updateUsersList() {
            users_list_api.get(`?login=${this.search}&offset=${this.offset}`).then((response) => {
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
