<template>
  <div
    class="
      min-h-screen
      flex
      items-center
      justify-center
      bg-gray-50
      py-12
      px-4
      sm:px-6
      lg:px-8
    "
  >
    <div class="max-w-md w-full space-y-8">
      <div>
        <img class="mx-auto h-28 w-auto" src="/assets/logo.png" alt="Logo" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          {{ $t("sign-in-message") }}
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="login">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">{{ $t("username") }}</label>
            <input
              id="username"
              name="username"
              type="text"
              autocomplete="username"
              required=""
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-md
                focus:outline-none
                focus:ring-blue-500
                focus:border-blue-500
                focus:z-10
                sm:text-sm
              "
              :placeholder="$t('username')"
            />
          </div>
        </div>

        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="password" class="sr-only">{{ $t("password") }}</label>
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required=""
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-md
                focus:outline-none
                focus:ring-blue-500
                focus:border-blue-500
                focus:z-10
                sm:text-sm
              "
              :placeholder="$t('password')"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="
              group
              relative
              w-full
              flex
              justify-center
              py-2
              px-4
              border border-transparent
              text-sm
              font-medium
              rounded-md
              text-white
              bg-blue-600
              hover:bg-blue-700
              focus:outline-none
              focus:ring-2
              focus:ring-offset-2
              focus:ring-blue-500
            "
          >
            {{ $t("sign-in") }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    login(ev) {
      axios
        .post("/api/v1/login", {
          username: ev.target.elements.username.value,
          password: ev.target.elements.password.value,
        })
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
