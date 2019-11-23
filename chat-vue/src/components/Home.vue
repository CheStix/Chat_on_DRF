<template>
    <div>
        <h1>Чат на Django+DRF+VUE.js</h1>
        <button @click="goLogin">Вход</button>
    </div>
</template>

<script>
    export default {
        name: "Home",
        methods: {
            goLogin() {
                this.$router.push({name: 'login'})
            },
        },
    }
</script>

<style scoped>

</style>
