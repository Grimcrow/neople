<script setup>
import {ref } from 'vue'
import axios from 'axios';

const URL = 'http://127.0.0.1:8000'
let name = ""
let date_of_birth = ""
let place_of_birth = ""
let horoscope = ref(null)

async function registerUser() {
  let url = `${URL}/register`

  let user = {
      name: name,
      date_of_birth: date_of_birth,
      place_of_birth: place_of_birth
    }


    console.log(user)
  axios.post(url, user)
  .then(resp => {
    console.log(resp)
  })
}

async function getHoroscope() {
  let url = `${URL}/horoscope/${name}`
  axios.get(url)
  .then(resp => {
    console.log(resp)
    horoscope.value = resp.data.horoscope
  })
}

</script>

<template>
  <header>
    <div class="wrapper">
      <h1>Welcome to Horoscopes!</h1>
      <div>
        <h1>Register</h1>
        <form @submit.prevent="registerUser">
        <input type="text" v-model="name" placeholder="Name" required />
        <input type="date" v-model="date_of_birth" placeholder="Date of Birth" required />
        <input type="text" v-model="place_of_birth" placeholder="Place of Birth" required />
        <button type="submit">Register</button>
        </form>
      </div>
      <div>
        <h1>If already registered enter your name here to get your horoscope</h1>
        <form @submit.prevent="getHoroscope">
          <input type="text" v-model="name" placeholder="Name" required />
          <button type="submit">Get Horoscope</button>
        </form>
        <h1>Your Horoscope is: </h1>
        <p>{{ horoscope }}</p>
        </div>
      </div>
  </header>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
