<script setup lang="ts">
// import navbar from '../components/NavBar.vue'
import Card from 'primevue/card'
</script>

<template>
  <!-- <navbar></navbar> -->
  <Card style="width: 25rem; overflow: hidden">
    <template #header>
      <img alt="user header" src="https://primefaces.org/cdn/primevue/images/usercard.png" />
    </template>
    <template #title>Advanced Card</template>
    <template #subtitle>Card subtitle</template>
    <template #content>
      <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error
        repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa
        ratione quam perferendis esse, cupiditate neque quas!
      </p>
    </template>
    <template #footer>
      <div class="flex gap-4 mt-1">
        <Button label="Cancel" severity="secondary" outlined class="w-full" />
        <Button label="Save" class="w-full" />
      </div>
    </template>
  </Card>
</template>


/*chatgpt part*/
<script setup lang="ts">
import Button from 'primevue/button';
</script>

<template>
  <div class="page-container">
    <h1 class="page-title">ElderEase</h1>
    <div class="button-container">
      <Button label="Request for helper" class="p-button-success custom-button"/>
      <Button label="Button 2" class="p-button-success custom-button"/>
      <Button label="Button 3" class="p-button-success custom-button"/>
      <Button label="Button 4" class="p-button-success custom-button"/>
    </div>
  </div>
</template>

<style>
/* Import PrimeVue theme and styles */
@import 'primevue/resources/themes/saga-blue/base.css';
@import 'primevue/resources/primevue.min.css';
@import 'primeicons/primeicons.css';

/* Custom styles for the page */
.page-container {
  padding: 20px;
  text-align: center;
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
  background-color: brown;
  border-color: brown;
  color: white;
}

</style>
