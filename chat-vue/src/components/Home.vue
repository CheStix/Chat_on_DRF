<template>
    <div>
        <h1>Чат на Django+DRF+VUE.js</h1>
        <button v-if="!auth" @click="goLogin">Вход</button>
        <button v-else @click="logout">Выход</button>

        <Room v-if="auth" @openDialog="openDialog"></Room>
        <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
    </div>
</template>

<script>
    import Room from "./rooms/Room";
    import Dialog from "./rooms/Dialog";

    export default {
        name: "Home",
        components: {
            Dialog,
            Room
        },
        data(){
            return {
                dialog:{
                    id:'',
                    show:false,
                }
            }
        },
        computed:{
            auth(){
                if (sessionStorage.getItem('auth_token')) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: 'login'})
            },
            //TODO сделать логаут через post запрос на url allauth для токена
            logout() {
                sessionStorage.removeItem('auth_token')
                window.location='/'
            },
            openDialog(id) {
                this.dialog.id=id
                this.dialog.show=true
            }
        },
    }
</script>

<style scoped>

</style>
