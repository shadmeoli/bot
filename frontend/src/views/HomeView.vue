<script setup lang="ts">
</script>

<template>
  <Suspense>

    <template #default>
      <main>
        <h1>Home Page</h1>
      </main>
    </template>

    <template #fallback>
      <div>
        <h1>Loading ...</h1>
      </div>
    </template>
    
  </Suspense>
</template>
