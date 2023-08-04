import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios';

export const useChatStore = defineStore('chat', () => {
  const count = ref(0)
  const replies = ref<string[]>([]);
  const prompts = ref<string[]>([]);

  const fetchReplies = async (prompt: string) => {

    const apiEndpoint = 'http://0.0.0.0:8000/api/v1/chat';

    try {
      // Make the API call using Axios
      const response = await axios.post(apiEndpoint, {
        message: prompt
      });

      // Assuming your API response contains the 'bot' field with the reply text
      const reply = response.data.bot;

      // Add the fetched reply to the replies buffer
      prompts.value.push(prompt);
      replies.value.push(reply);

    } catch (error) {
      console.error('Error fetching replies:', error);
    }
  };

  return {
    count,
    replies,
    prompts,
    fetchReplies,
  }
})
