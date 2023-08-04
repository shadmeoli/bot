import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useChatStore = defineStore('chat', () => {
  const count = ref(0)
  const replies = ref<string[]>();
  const prompts = ref<string[]>();
})
