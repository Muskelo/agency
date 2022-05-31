<template>
	<tr>
        <th scope="row">{{user.id}}</th>
		<td>{{user.login}}</td>
		<td>{{user.number}}</td>
		<td>{{user.role}}</td>
		<td><button class="btn btn-primary">Сохранить</button></td>
	</tr>
</template>

<script>
export default {
	props: ["user"],
};
</script>

<style>
</style>
