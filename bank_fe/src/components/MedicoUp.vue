<template>

    <div class="signUp_medico">
        <div class="container_signUp_medico">
            <h2>Nuevo Medico</h2>

            <form v-on:submit.prevent="processMedicoUp" >
                <br>
                <br>
                <input type="text" v-model="medico.name" placeholder="Nombre Medico">
                <br>
                <br>
                <input type="text" v-model="medico.last_name" placeholder="Apellido Medico">
                <br>
                <br>
                <input type="text" v-model="medico.phone" placeholder="Numero Telefonico Medico">
                <br>
                <br>
                <input type="text" v-model="medico.especialidad_medico" placeholder="Especialidad del Medico">
                <br>
                <br>
                <input type="text" v-model="medico.tarjeta_profesional" placeholder="Tarjeta Profesional Medico">
                <br>
                <br>
                <input type="text" v-model="medico.documento_medico" placeholder="C.C o DNI">
                <br>
                <br>                
                <button type="submit">Crear Medico</button>
                <br>
                <br> 
            </form>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {

    name: "MedicoUp",

    data: function(){
        return {
            medico: {
                name: "",
                last_name: "",
                phone: "",
                especialidad_medico: "",
                tarjeta_profesional: "",
                documento_medico: ""
                                                                                
            }
        }
    },
    
    methods: {

        processMedicoUp: function () {

            
            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                this.$emit('logOut');
                return;
            }

            this.verifyToken();
            let token = localStorage.getItem("token_access");
            
                        

            //axios.post("http://127.0.0.1:8000/medico/",this.medico, {headers: {'Authorization': `Bearer ${token}`}})        
            axios.post("https://shsprint3.herokuapp.com/medico/",this.medico, {headers: {'Authorization': `Bearer ${token}`}})     
                .then((result) => {
                    let dataLogIn = {                       
                    }

                    this.$emit('completedMedicoUp', dataLogIn)
                })

                .catch((error) => {
                    console.log(error)                    
                    alert("ERROR: Fallo en el registro.");   
                });
        },

        verifyToken: function () {
            return axios.post("https://shsprint3.herokuapp.com/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}})

                .then((result) => {
                    localStorage.setItem("token_access", result.data.access);
                })

                .catch(() => {
                    this.$emit('logOut');
                });
        }                

            
    }, 
    
    
} 
 

</script>

<style>
    .signUp_medico{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_signUp_medico {
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        
    }

    .signUp_medico h2{
        color: #283747;        
        
    }

    .signUp_medico form{
        width: 70%;
        
    }

    .signUp_medico input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #283747;
    }

    .signUp_medico button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }

    .signUp_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }
</style>