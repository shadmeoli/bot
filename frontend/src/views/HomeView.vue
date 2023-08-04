<script setup lang="ts">

</script>

<template>
  <Suspense>

    <template #default>
      <main class="h-auto w-screen">
        <nav class="w-screen h-20 p-2 bg-black flex sticky top-0">
          <img src="https://shopzetu.com/cdn/shop/files/Logo_for_white_Background_100x.png?v=1672727778" alt="">
        </nav>
        
        <body class="w-screen h-screen flex flex-col items-center justify-center">
          <h1 class="font-bold">Chat Window</h1>
          <div class="bg-gray-200 h-[50%] w-[80%]">
            <h1 class="">Chats will apper here</h1>
          </div>
          <div class="flex w-[80%] h-28 bg-black p-4">
            <input class="rounded-l-xl w-[80%] h-20 bg-gray-200 px-4 font-bold text-black" placeholder="enter text here">
            <button class="h-20 w-40 bg-gradient-to-br from-red-400 to-orange-300 hover:from-red-600 hover:to-orange-500 active:from-red-400 active:to-orange-300 rounded-r-xl font-bold text-white">SEND</button>
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
