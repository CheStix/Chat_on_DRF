<template>
    <div>
        <div v-for="dialog in dialogs" class="dialog">
            <h2>{{dialog.user.username}}</h2>
            <p>{{dialog.text}}</p>
            <span>{{dialog.date}}</span>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Dialog",
        props: {
            id:'',
        },
        data() {
            return {
                dialogs:'',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')},
            });
            this.loadDialog()
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url:'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'GET',
                    data: {
                        room:this.id
                    },
                    success: (response)=>{
                        this.dialogs=response.data.data
                    }
                })
            }
        }
    }
</script>


<style scoped>
    .dialog {
        width: 60%;
        height: 150px;
        border: 1px solid #000;
        margin-bottom: 5px;
        margin-top: 10px;
        float: right;
    }
</style>
