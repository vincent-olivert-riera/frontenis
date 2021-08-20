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
        <img
          class="mx-auto h-12 w-auto"
          src="/assets/logo.png"
          alt="Logo"
        />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          {{ $t("sign-in-message") }}
        </h2>
      </div>
      <form class="mt-8 space-y-6" action="#" method="POST">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email-address" class="sr-only">{{ $t("email") }}</label>
            <input
              id="email-address"
              name="email"
              type="email"
              autocomplete="email"
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
                rounded-t-md
                focus:outline-none
                focus:ring-blue-500
                focus:border-blue-500
                focus:z-10
                sm:text-sm
              "
              :placeholder="$t('email')"
            />
          </div>
          <div>
            <label for="password" class="sr-only">{{ $t('password') }}</label>
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
                rounded-b-md
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

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              class="
                h-4
                w-4
                text-blue-600
                focus:ring-blue-500
                border-gray-300
                rounded
              "
            />
            <label for="remember-me" class="ml-2 block text-sm text-gray-900">
              {{ $t("remember-me") }}
            </label>
          </div>

          <div class="text-sm">
            <a
              href="#"
              class="font-medium text-blue-600 hover:text-blue-500"
            >
              {{ $t("forgot-password") }}
            </a>
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
