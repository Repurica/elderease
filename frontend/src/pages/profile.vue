<template>
    <div class="profile-page">
      <h1>User Profile</h1>
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
    avatar: 'https://via.placeholder.com/150',  // Placeholder avatar image
    bio: 'Software engineer with a passion for developing innovative programs.',
  };
  </script>
  
  <style scoped>
  .profile-page {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
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