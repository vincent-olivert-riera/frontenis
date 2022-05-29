<template>
  <div class="relative bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div
        class="flex justify-between items-center border-b-2 border-gray-100 py-6 md:justify-start md:space-x-10"
      >
        <div class="flex justify-start">
          <a href="#">
            <img class="h-8 w-auto sm:h-10" src="/assets/logo.png" alt="Logo" />
          </a>
        </div>
        <div as="nav" class="hidden md:flex space-x-10">
          <div class="relative">
            <button
              :class="[
                open ? 'text-gray-900' : 'text-gray-500',
                'group bg-white rounded-md inline-flex items-center text-base font-medium hover:text-gray-900 focus:outline-none',
              ]"
            >
              <span>{{ $t("availability") }}</span>
            </button>
          </div>
        </div>
        <div class="hidden md:flex items-center justify-end md:flex-1 lg:w-0">
          <button
            class="ml-8 whitespace-nowrap inline-flex px-4 py-2 border border-transparent rounded-md shadow-sm justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            @click="logout()"
          >
            {{ $t("logout") }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    logout() {
      axios
        .post("/api/v1/logout")
        .then(() => {
          window.location.replace("/");
        })
        .catch((err) => {
          console.log("Error", err);
        });
    },
  },
};
</script>
