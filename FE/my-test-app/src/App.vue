<template>
  <div>
    <div>
      <label>Input Angka</label>
      <input
        type="number"
        name="number"
        v-model="number"
        placeholder="Input Angka"
      />
    </div>

    <div>
      <button @click="generateTriangle">Generate Segitiga</button>
      <button @click="generateOdds">Generate Bilangan Ganjil</button>
      <button @click="generatePrimes">Generate Bilangan Prima</button>
    </div>
    <h3>Result :</h3>
    <div>{{ result }}</div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  el: "#app",
  data() {
    return {
      result: "1234",
      number: 5,
    };
  },
  methods: {
    validationNumber() {
      const inNUmber = parseInt(this.number);
      if (isNaN(inNUmber) || inNUmber < 0) {
        this.result = "Invalid number input, please input positive number";
        this.number = 0;
        return false;
      }
      this.result = "";
      return true;
    },
    async generateTriangle() {
      if (this.validationNumber) {
        try {
          const response = await axios.post(
            "http://127.0.0.1:5000/generate_triangle",
            {
              number: this.number,
            }
          );
          this.result = response.data;
          console.log(this.response);
        } catch (error) {
          this.result = error;
          alert(error);
        }
      }
      return "1";
    },
    async generateOdds() {
      if (this.validationNumber) {
        try {
          const response = await axios.post(
            "http://127.0.0.1:5000/generate_odds",
            {
              number: this.number,
            }
          );
          this.result = response.data;
          console.log(this.response);
        } catch (error) {
          this.result = error;
          alert(error);
        }
      }
      return "1";
    },
    async generatePrimes() {
      if (this.validationNumber) {
        try {
          const response = await axios.post(
            "http://127.0.0.1:5000/generate_primes",
            {
              number: this.number,
            }
          );
          this.result = response.data;
          console.log(this.response);
        } catch (error) {
          this.result = error;
          alert(error);
        }
      }
      return "1";
    },
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
