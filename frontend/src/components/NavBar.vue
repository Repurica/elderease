<script setup>
// console.log('NavBar component is rendered');   
</script>

<template>
  <footer>
    <nav>
      <ul>
        <li>
          <router-link to="/">Home</router-link>
        </li>
        <!-- <li>
          <router-link to="/about"></router-link>
        </li> -->
        <li>
          <router-link to="/contact">Profile</router-link>
        </li>
      </ul>
    </nav>
  </footer>
</template>

<style scoped>
header {
  background-color: #333;
  color: white;
  padding: 10px;
}

nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 10px;
}

nav ul li a {
  color: white;
  text-decoration: none;
}

nav ul li a:hover {
  text-decoration: underline;
}
</style>