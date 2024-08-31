<script setup lang="ts">
import { ref } from 'vue';
import NavBar from '../components/NavBar.vue';

// Define the helpers data using the ref function from Vue
const dummyhelpers = ref([
  { id: 1, name: 'John Doe', skill: 'Plumbing', distance: 2, details: 'Experienced in residential plumbing repairs.' },
  { id: 2, name: 'Jane Smith', skill: 'Electrical', distance: 5, details: 'Licensed electrician with 10 years of experience.' },
  { id: 3, name: 'Sam Wilson', skill: 'Carpentry', distance: 3, details: 'Specializes in custom furniture and home renovations.' },
  // Add more helpers as needed
]);
</script>

<template>
  <!-- Include the NavBar component -->
  <NavBar />

  <div class="helper-list">
    <h1>Nearby Helpers</h1>
    <div class="helper-container" v-for="helper in dummyhelpers" :key="helper.id">
      <h2>{{ helper.name }}</h2>
      <p><strong>Skill:</strong> {{ helper.skill }}</p>
      <p><strong>Distance:</strong> {{ helper.distance }} km</p>
      <p><strong>Details:</strong> {{ helper.details }}</p>
    </div>
  </div>
</template>

<style scoped>
.helper-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.helper-container {
  background-color: #f4f4f4;
  padding: 20px;
  margin: 15px 0;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.helper-container h2 {
  margin-bottom: 10px;
}

.helper-container p {
  margin: 5px 0;
}

.helper-container strong {
  color: #333;
}
</style>
