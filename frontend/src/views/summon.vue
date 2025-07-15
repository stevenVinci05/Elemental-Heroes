<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-900 to-indigo-800 p-6 text-white flex flex-col items-center">
    <h1 class="text-4xl font-bold mb-6">Elemental Heroes - Summon</h1>

    <button
      @click="summon"
      class="bg-yellow-500 text-black px-6 py-3 rounded-xl text-lg font-semibold hover:bg-yellow-400 transition mb-8"
    >
      Summon Hero
    </button>

    <div v-if="heroes.length > 0" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4">
      <HeroCard
        v-for="(hero, index) in heroes"
        :key="index"
        :name="hero.name"
        :element="hero.element"
        :stars="hero.stars"
        :image="hero.image"
      />
    </div>
    <div v-if="loading" class="mb-4 text-yellow-300 font-semibold">Loading...</div>
    <div v-if="error" class="mb-4 text-red-500 font-semibold">Error: {{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import HeroCard from '@/components/HeroCard.vue'

const heroes = ref([])
const loading = ref(false)
const error = ref(null)

async function summon() {
  loading.value = true
  error.value = null
  try {
    const response = await fetch('http://127.0.0.1:8000/summon')
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
    const data = await response.json()
    heroes.value = data.heroes.map(hero => ({
      ...hero,
      image: 'https://via.placeholder.com/80' // puoi cambiare con sprite veri dopo
    }))
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}
</script>
