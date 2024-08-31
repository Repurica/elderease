<template>
    <div class="chat-container">
      <div class="message-list">
        <div v-for="message in messages" :key="message.id" class="message">
          <strong>{{ message.user }}:</strong>
          <p v-if="message.type === 'text'">{{ message.content }}</p>
          <audio v-if="message.type === 'audio'" :src="message.content" controls></audio>
        </div>
      </div>
      <div class="message-input">
        <input v-model="textMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
        <button @click="startRecording">Record</button>
        <button @click="stopRecording">Stop</button>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import Recorder from 'recorder-js'; // Ensure recorder-js is installed
  
  const messages = ref<any[]>([]);
  const textMessage = ref('');
  const recorder = new Recorder(new (window as any).AudioContext());
  
  function sendMessage() {
    if (textMessage.value.trim()) {
      messages.value.push({ id: Date.now(), user: 'Me', type: 'text', content: textMessage.value });
      textMessage.value = '';
    }
  }
  
  function startRecording() {
    recorder.start().then(() => {
      console.log('Recording started');
    });
  }
  
  function stopRecording() {
    recorder.stop().then(({ blob }) => {
      const url = URL.createObjectURL(blob);
      messages.value.push({ id: Date.now(), user: 'Me', type: 'audio', content: url });
    });
  }
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }
  
  .message-list {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    background-color: #f1f1f1;
  }
  
  .message {
    margin-bottom: 10px;
  }
  
  .message-input {
    display: flex;
    align-items: center;
    padding: 10px;
    background-color: #fff;
  }
  
  .message-input input {
    flex: 1;
    padding: 10px;
    margin-right: 10px;
  }
  
  .message-input button {
    margin-left: 5px;
  }
  </style>