<template>
  <div>
    <h1>{{ msg }}</h1>

    <p>
      <a
        href="https://vitejs.dev/guide/features.html"
        target="_blank"
        class="text-green-500"
      >
        Vite Documentation
      </a>
      |
      <a href="https://v3.vuejs.org/" target="_blank" class="text-green-500"
        >Vue 3 Documentation</a
      >
    </p>

    <button type="button" @click="state.count++">
      count is: {{ state.count }}
    </button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test hot module replacement.
    </p>
  </div>
</template>

<script setup>
import { defineProps, reactive } from "vue";

defineProps({
  msg: {
    type: String,
    default: "",
  },
});

const state = reactive({ count: 0 });
</script>
