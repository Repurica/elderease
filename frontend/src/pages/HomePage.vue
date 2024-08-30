<script setup lang="ts">
import Button from 'primevue/button';
import { useRouter } from 'vue-router';

// Initialize the router
const router = useRouter();

// Define the function that navigates to the next page
function goToNextPage() {
  router.push('/requestforhelper.vue'); // Replace with the correct route
}
</script>

<template>

  <div class="page-container">
    <h1 class="page-title">ElderEase</h1>
    <div class="button-container">
      <Button @click="goToNextPage()" label="Request for Helper" class="p-button-success custom-button"/>
      <Button label="Emergency Alert" class="p-button-success custom-button"/> <br>
      <Button label="Speak to Me" class="p-button-success custom-button"/> 
      <Button label="Request for Check-Up" class="p-button-success custom-button"/>
    </div>
  </div>
</template>


<style scoped>

/* Custom styles for the page */

.page-container {
  padding: 20px;
  text-align: center;
  background-color: beige;
  height: 1000px;
}

.page-title {
  font-size: 2em;
  margin-bottom: 20px;
}

.button-container {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.custom-button{
  background-color: 	#5C4033;
  color: white;
  border-color: 	#5C4033;
}
</style>

