<template>
  <div class="bg-white rounded-2xl shadow-md p-4 w-40 text-center">
    <img :src="image" alt="Hero" class="w-20 h-20 mx-auto mb-2" />
    <h3 class="font-bold text-lg">{{ name }}</h3>
    <p class="text-sm text-gray-500">{{ element }}</p>
    <div class="mt-2 text-yellow-400">
      <span v-for="n in stars" :key="n">★</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  element: String,
  stars: Number,
  image: String
});
</script>
