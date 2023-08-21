import axios from 'axios';
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useChatStore = defineStore('chat', () => {

  const userText = ref<string | undefined>();
  const replies = ref<string[]>([]);
  const prompts = ref<string[]>([]);

  const fetchReplies = async (text: string) => {
    const apiEndpoint = 'https://shop-zetu-bot.onrender.com/api/v1/chat';

    // Check if userText.value is undefined, provide a default value (empty string) if it is
    userText.value = text || '';

    try {
      // Make the API call using Axios
      const response = await axios.post(apiEndpoint, {
        message: text,
      });

      // Assuming your API response contains the 'bot' field with the reply text
      const reply = response.data.bot;

      // Add the fetched reply to the replies buffer
      prompts.value.push(userText.value);
      replies.value.push(reply);
      userText.value = '';

    } catch (error) {
      console.error('Error fetching replies:', error);
    }
  };

  return {
    replies,
    prompts,
    fetchReplies,
  }
})
