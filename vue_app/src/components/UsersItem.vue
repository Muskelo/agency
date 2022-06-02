<template>
	<tr>
		<th scope="row">{{user.id}}</th>
		<td>{{user.login}}</td>
		<td>{{user.number}}</td>
		<td>
			<select @change="patchUser" v-model="user_role" name="role" id="role" class="form-control">
				<option value="user">Пользователь</option>
				<option value="admin">Администратор</option>
				<option value="moder">Модератор</option>
			</select>
		</td>
	</tr>
</template>

<script>
import { user_api } from "../api.js";

export default {
	props: ["user"],
	data() {
		return {
			user_role: this.user.role,
		};
	},
	methods: {
		async patchUser() {
			const data = {
				data: {
					role: this.user_role,
				},
			};
			const response = await user_api.patch(this.user.id, data);
		},
	},
};
</script>

<style>
</style>
