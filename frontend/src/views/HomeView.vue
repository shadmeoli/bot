<script setup lang="ts">

</script>

<template>
  <Suspense>

    <template #default>
      <main class="h-auto w-screen">
        <nav class="w-screen h-20 p-2 bg-black flex sticky top-0">
          <img src="https://shopzetu.com/cdn/shop/files/Logo_for_white_Background_100x.png?v=1672727778" alt="">
        </nav>
        
        <body class="w-screen h-screen flex flex-col items-center mt-20  md:mt-40">
          <h1 class="font-bold">Chat Window</h1>
          <div class="bg-gray-200 h-[50%] w-[80%] p-4 flex flex-col-reverse justify-end overflow-y-scroll" id="chatWindow">
            <h1 class="flex justify-center mt-40 md:text-4xl font-bold text-gray-300">Chats will apper here ...</h1>
            <div class="mb-4">User: Hello!</div>
            <div class="mb-4">Bot: Hi there!</div>
          </div>

          <div class="flex w-[80%] h-28 bg-black p-4 items-center">
            <input class="outline-none active:outline-none hover:outline-none w-[90%] h-14 md:h-20 bg-gray-200 px-4 font-bold text-black" placeholder="enter text here">
            <button class="h-14 md:h-20 w-40 bg-gradient-to-br from-gray-400 to-gray-300 hover:from-gray-600 hover:to-gray-500 active:from-gray-400 active:to-gray-300 font-bold text-white">SEND</button>
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
