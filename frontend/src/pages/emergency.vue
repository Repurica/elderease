<template>
    <div class="emergency-alert">
      <header>
        <h1>Emergency Alert</h1>
      </header>
      <section class="contact-info">
        <h2>Emergency Contacts</h2>
        <div class="contact-card">
          <img src="@/assets/M.jpg" alt="Family Member 1" class="profile-pic">
          <div class="contact-details">
            <h3>Family Member 1</h3>
            <p>John Doe - (555) 123-4567</p>
          </div>
        </div>
        <div class="contact-card">
          <img src="@/assets/W.jpg" alt="Family Member 2" class="profile-pic">
          <div class="contact-details">
            <h3>Family Member 2</h3>
            <p>Jane Doe - (555) 987-6543</p>
          </div>
        </div>
        <div class="contact-card">
          <img src="@/assets/Hospital.jpg" alt="Local Hospital" class="profile-pic">
          <div class="contact-details">
            <h3>Local Hospital</h3>
            <p>City Hospital - (555) 555-5555</p>
          </div>
        </div>
      </section>
      <button @click="sendEmergencyAlert" class="alert-button">Send Emergency Alert</button>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  // Function to handle the sending of an emergency alert
  const sendEmergencyAlert = () => {
    // Simulate sending an alert (e.g., call an API or service)
    alert("Emergency Alert Sent to Loved Ones and Hospitals.");
  };
  </script>
  
  <style scoped>
  .emergency-alert {
    max-width: 500px;
    margin: 30px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  header {
    text-align: center;
    margin-bottom: 20px;
  }
  
  header h1 {
    font-size: 24px;
    color: #333;
    font-weight: 600;
  }
  
  .contact-info {
    margin-bottom: 20px;
  }
  
  .contact-info h2 {
    font-size: 20px;
    color: #333;
    margin-bottom: 15px;
  }
  
  .contact-card {
    display: flex;
    align-items: center;
    background-color: #f2f2f2;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .profile-pic {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 15px;
  }
  
  .contact-details {
    flex: 1;
  }
  
  .contact-details h3 {
    margin: 0;
    font-size: 18px;
    color: #333;
  }
  
  .contact-details p {
    margin: 5px 0 0;
    font-size: 16px;
    color: #555;
  }
  
  .alert-button {
    background-color: #e74c3c;
    color: white;
    padding: 15px 25px;
    font-size: 18px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .alert-button:hover {
    background-color: #c0392b;
  }
  </style>