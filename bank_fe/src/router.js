import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';

import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Account from './components/Account.vue'
import Home from './components/Home.vue'
import MedicoUp from './components/MedicoUp.vue'

const routes = [{
        path: '/',
        name: 'root',
        component: App
    },
    {
        path: '/user/logIn',
        name: "logIn",
        component: LogIn
    },
    {
        path: '/user/signUp',
        name: "signUp",
        component: SignUp
    },    
    {
        path: '/user/home',
        name: "home",
        component: Home
    },
    {
        path: '/user/medicoUp',
        name: "medicoUp",
        component: MedicoUp
    },
    {
        path: '/user/account',
        name: "account",
        component: Account
    }    

];
const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;