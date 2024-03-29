<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useChatStore } from '../stores/chat';

const chatStore = useChatStore()
const text = ref<string | undefined>();
const messages = ref<{ id: string; text: string; isPrompt: boolean }[]>([])

const fetchReplies = async () => {
  if (text.value !== undefined) { // Fix the typo 'unefined' to 'undefined'
    await chatStore.fetchReplies(text.value);
  }

  messages.value = [...chatStore.prompts, ...chatStore.replies].map((message, index) => ({
    id: `message_${index}`,
    text: message,
    isPrompt: index < chatStore.prompts.length,
  }))
  text.value = ''
}

// Fetch replies when the component is mounted (optional)
onMounted(fetchReplies)
</script>


<template>
  <Suspense>

    <template #default>
      <main class="min-h-screen w-screen">
        <nav class="w-screen h-20 p-2 bg-black flex sticky top-0">
          <img src="https://shopzetu.com/cdn/shop/files/Logo_for_white_Background_100x.png?v=1672727778" alt="">
        </nav>
        
        <body class="w-screen flex flex-col items-center mt-20  md:mt-40">
          <h1 class="font-bold">Chat Window</h1>
          <div class="bg-gray-200 h-[400px] w-[80%] md:w-[40%] p-4 flex flex-col-reverse justify-end overflow-y-scroll" id="chatWindow">
            <h1 v-if="chatStore.prompts.length === 0" class="flex justify-center mt-40 md:text-4xl font-bold text-gray-300">Chats will appear here ...</h1>
            <div v-for="message in messages" :key="message.id" class="mb-4">
              <div v-if="message.isPrompt">
                User: {{ message.text }}
              </div>
              <div v-else>
                Bot: {{ message.text }}
              </div>
            </div>
          </div>

          <div class="flex w-[80%] md:w-[40%] h-28 bg-black p-6 items-center">
            <input v-model="text" class="outline-none active:outline-none hover:outline-none w-[90%] h-14 md:h-20 bg-gray-200 px-4 font-bold text-black" placeholder="enter text here">
            <button @click="fetchReplies" class="h-14 md:h-20 w-40 bg-gradient-to-br from-gray-400 to-gray-300 hover:from-gray-600 hover:to-gray-500 active:from-gray-400 active:to-gray-300 font-bold text-white">SEND</button>
          </div>
        </body>

      </main>
    </template>

    <template #fallback>
      <div>
        <h1>Loading ...</h1>
      </div>
    </template>
  </Suspense>

</template>
