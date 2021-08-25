<template>
  <div>
    <p>This is the app</p>
    <button type="button" @click="logout">Logout</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    logout() {
      axios.post(
        "/api/v1/logout"
      ).then(() => {
        window.location.replace("/");
      }).catch(err => {
        console.log("Error", err);
      });
    },
  },
};
</script>
