<script setup lang="ts"></script>
<template>
    <div class="checkup-request">
      <header>
        <h1>Request Check-Up</h1>
      </header>
      <section class="request-form">
        <h2>Request Details</h2>
        <form @submit.prevent="submitRequest">
          <div class="form-group">
            <label for="name">Your Name:</label>
            <input type="text" id="name" v-model="requesterName" required />
          </div>
          <div class="form-group">
            <label for="contact">Contact Number:</label>
            <input type="text" id="contact" v-model="contactNumber" required />
          </div>
          <div class="form-group">
            <label for="address">Address:</label>
            <input type="text" id="address" v-model="address" required />
          </div>
          <div class="form-group">
            <label for="request-type">Request Type:</label>
            <select id="request-type" v-model="requestType" required>
              <option value="" disabled>Select Request Type</option>
              <option value="social-visit">Social Visit</option>
              <option value="health-checkup">Health Check-Up</option>
              <option value="both">Both</option>
            </select>
          </div>
          <button type="submit" class="submit-button">Submit Request</button>
        </form>
      </section>
      <section class="info-section">
        <h2>What to Expect</h2>
        <p><strong>Social Visits and Companionship:</strong> Volunteers will visit your home to chat, provide companionship, and check on your well-being. This helps ensure that your living environment is safe and that your needs are met.</p>
        <p><strong>Health Check-Ups:</strong> Healthcare professionals will conduct regular check-ups to monitor your health, address any medical concerns, and provide preventive care to maintain your overall well-being.</p>
      </section>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  // Reactive variables for form data
  const requesterName = ref('');
  const contactNumber = ref('');
  const address = ref('');
  const requestType = ref<string>('');
  
  // Function to handle form submission
  const submitRequest = () => {
    // Example of handling form submission
    alert(`Request submitted:
    \nName: ${requesterName.value}
    \nContact: ${contactNumber.value}
    \nAddress: ${address.value}
    \nRequest Type: ${requestType.value}`);
  
    // Reset form after submission
    requesterName.value = '';
    contactNumber.value = '';
    address.value = '';
    requestType.value = '';
  };
  </script>
  
  <style scoped>
  .checkup-request {
    max-width: 600px;
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
  
  .request-form {
    margin-bottom: 20px;
  }
  
  .request-form h2 {
    font-size: 20px;
    color: #333;
    margin-bottom: 15px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    font-size: 16px;
    color: #555;
    margin-bottom: 5px;
  }
  
  .form-group input,
  .form-group select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
  }
  
  .submit-button {
    background-color: #3498db;
    color: white;
    padding: 15px 25px;
    font-size: 18px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .submit-button:hover {
    background-color: #2980b9;
  }
  
  .info-section {
    margin-top: 30px;
  }
  
  .info-section h2 {
    font-size: 20px;
    color: #333;
    margin-bottom: 15px;
  }
  
  .info-section p {
    font-size: 16px;
    color: #555;
  }
  </style>