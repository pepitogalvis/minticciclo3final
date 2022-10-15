<template>

    <div v-if="loaded" class="information">
        <h1>Información de su cuenta</h1>
        <h2>Nombre: <span>{{name}}</span></h2>
        <h2>Apellido: <span>{{lastname}}</span></h2>
        <h2>Direccion: <span>{{address}}</span></h2>
        <h2>Ciudad: <span>{{city}}</span></h2>
        <h2>Telefono: <span>{{phone}}</span></h2>
        <h2>Correo electrónico: <span>{{email}}</span></h2>   
        <h2>Identificación: <span>{{dni}}</span></h2>
        <h2>Fecha de Nacimiento: <span>{{born_date}}</span></h2>                   
             
    </div>



</template>

<script>

import jwt_decode from "jwt-decode";
import axios from 'axios';

export default {
    name: "Account",
    data: function(){
        return {
            name: "",            
            lastname: "",
            address: "",
            city:"",
            phone:"",
            email: "",
            dni:"",
            born_date:"",
            loaded: false,
        }
    },

    methods: {
        getData: async function () {

            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                this.$emit('logOut');
                return;
            }

            await this.verifyToken();
            let token = localStorage.getItem("token_access");
            let userId = jwt_decode(token).user_id.toString();
           

            //axios.get(`http://127.0.0.1:8000/user/${userId}/`, {headers: {'Authorization': `Bearer ${token}`}})
            axios.get(`https://shsprint3.herokuapp.com/user/${userId}/`, {headers: {'Authorization': `Bearer ${token}`}})                        

                .then((result) => {
                    this.name = result.data.name;
                    this.lastname = result.data.lastname;
                    this.address = result.data.address;
                    this.city = result.data.city;
                    this.phone= result.data.phone;
                    this.dni = result.data.dni;
                    this.born_date = result.data.born_date;
                    this.email = result.data.email;                                
                    this.loaded = true;
                })
                .catch(() => {
                    this.$emit('logOut');
                });
        },

        verifyToken: function () {
            //return axios.post("http://127.0.0.1:8000/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}})
            return axios.post("https://shsprint3.herokuapp.com/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}})
    
                .then((result) => {
                    localStorage.setItem("token_access", result.data.access);
                })
        
                .catch(() => {
                    this.$emit('logOut');
                });
        }
    },

    created: async function(){
        this.getData();
    },
}
</script>

<style>
    .information{
        margin: 0;
        padding: 0%;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .information h1{
        font-size: 60px;
        color: #0f1316;
    }

    .information h2{
        font-size: 25px;
        color: #283747;
    }

    .information span{
        color: crimson;
        font-weight: bold;
    }
</style>