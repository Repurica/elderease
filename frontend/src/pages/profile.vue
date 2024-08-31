<template>
  <div class="profile-page">
    <div class="profile-header">
      <h1>User Profile</h1>
      <button class="edit-profile-button" @click="editProfile">Edit Profile</button>
    </div>
    <div class="profile-card">
      <img :src="user.avatar" alt="User Avatar" class="profile-avatar" />
      <h2>{{ user.name }}</h2>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Bio:</strong> {{ user.bio }}</p>
      <!-- Add more profile details here as needed -->
    </div>
  </div>
</template>

<script setup lang="ts">
// Sample user data (you can replace this with data fetched from an API)
const user = {
  name: 'Lynn Ong Ling Yi',
  email: 'lynn@example.com',
  avatar: 'https://via.placeholder.com/150', // Placeholder avatar image
  bio: 'Software engineer with a passion for developing innovative programs.',
};

// Method to handle edit profile action
const editProfile = () => {
  // Logic to navigate to edit profile page or open a modal
  console.log('Edit Profile clicked');
  // You can use Vue Router to navigate to an edit profile page
  // this.$router.push('/edit-profile');
};
</script>

<style scoped>
.profile-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.edit-profile-button {
  background-color: #5C4033;
  color: white;
  border: none;
  padding: 10px 20px; 
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

.edit-profile-button:hover {
  background-color: #0056b3;
}

.profile-card {
  background-color: beige;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.profile-avatar {
  border-radius: 50%;
  width: 150px;
  height: 150px;
  object-fit: cover;
  margin-bottom: 20px;
}

h2 {
  margin-bottom: 10px;
}

p {
  margin: 5px 0;
}

strong {
  color: #333;
}
</style>