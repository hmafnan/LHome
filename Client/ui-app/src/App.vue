<template>
  <div class="header">
    <div class="logo">
      <router-link to="/"><img src="./assets/logo.svg"></router-link>
    </div>
    <div class="menu">
      <router-link to="/about"><img src="./assets/burger-icon.svg"></router-link>
    </div>
  </div>
  <router-view/>
</template>

<style>
body {
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.header {
  width: 100%;
  height:40px;
  background-color: #ebeae6;
}

.logo {
  width: 30%;
  float: left;
  text-align: left;
  padding: 10px 10px 0 10px;
}

.menu {
  width: 30%;
  float: right;
  text-align: right;
  padding: 10px 10px 0 10px;
}

@media only screen and (min-width: 768px) {
  .header {
    height: 60px;
  }
  .logo {
    margin-left: 5px;
    margin-top: 5px;
  }
  .logo img {
    width: 180px;
  }
}

</style>
