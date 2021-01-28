<template>
  <div class="map-container">
      <div id="map"></div>
      <div class="detail" v-show="showDetails">
        <div class="close-container">
          <a href="javascript:void(0);" v-on:click="showDetails=false"><span>x</span>
        </a></div>
        <div class="info">
            <div class="info-img">
                <img :src=details.picture>
            </div>
            <div class="info-room">
              <div class="city">{{ details.city }}</div>
              <div class="title">{{ details.title }}</div>
              <div class="distance">{{details.distance}}</div>
              <div class="price">£{{details.price}}</div>
            </div>
        </div>
        <div class="btn-container">
          <router-link :to="{ name: 'Booking', params: { title: details.title }}"
          title="Go to Booking">
            <button class="btn book-btn">Book</button>
          </router-link>
        </div>
      </div>
  </div>
</template>

<script>
import gmapsInit from '@/utils/gmaps';

export default {
  name: "Map",
  data() {
    return {
      map: null,
      mapCenter: {lat:48.1351, lng:11.5820},
      google: null,
      previousMarker: '',
      showDetails: false,
      details: {
        'city': 'Munich',
        'title': '',
        'price': '',
        'picture': '',
        'distance': '30 Km from the center'
      },
      markers: [
        {
          'position': {lat:48.1303528, lng: 11.5759874},
          'info': 'This is the lime home',
          'price': '600',
          'picture': require('@/assets/rooms/lime-home-1.jpg')
        },
        {
          'position': {lat: 48.1298707, lng: 11.5812582},
          'info': 'The deutschess museum',
          'price': '300',
          'picture': require('@/assets/rooms/lime-home-2.jpg')
        },
        {
          'position': {lat: 48.1632473, lng: 11.6023784},
          'info': 'Englishe Garden',
          'price': '400',
          'picture': require('@/assets/rooms/lime-home-3.jpg')
        },
        {
          'position': {lat:48.1385094, lng: 11.5733445},
          'info': 'Frauen Kirche',
          'price': '200',
          'picture': require('@/assets/rooms/lime-home-4.jpg')
        },
        {
          'position': {lat: 48.1350038, lng: 11.5690823},
          'info': 'Asam Kirche',
          'price': '65',
          'picture': require('@/assets/rooms/lime-home-5.jpg')
        },
        {
          'position': {lat: 48.1284109, lng: 11.5496695},
          'info': 'Bevaria Statue',
          'price': '56',
          'picture': require('@/assets/rooms/lime-home-6.jpg')
        }
      ]
    }
  },
  async mounted() {
    this.google = await gmapsInit();
    this.initMap()
  },
  methods: {
    initMap() {
      this.map = new this.google.maps.Map(document.getElementById('map'), {
        center:this.mapCenter,
        zoom: 13,
        streetViewControl: false,
        mapTypeControl: false,
      });
      this.setMarkers();
    },
    setMarkers() {
      const outer = this
      this.markers.forEach(option => {
        const position = option.position;
        const marker = new this.google.maps.Marker({
          position: position,
          map: this.map,
          icon: require('../assets/home-icon.svg')
        });

        marker.addListener('click', function () {
          marker.setIcon(require('../assets/home-icon-active.svg'));
          outer.details.title = option.info;
          outer.details.price = option.price;
          outer.details.picture = option.picture;
          outer.showDetails = true;
          if (outer.previousMarker !== '') {
            outer.previousMarker.setIcon(require('../assets/home-icon.svg'));
          }
          outer.previousMarker = marker;
        });
      })
    }
  }
}
</script>

<style scoped>
a {text-decoration: none; color: black}
.map-container {
  position: relative;
}

#map {
  width:100%;
  height:600px;
}

.close-container {
  width:100%;
  text-align: right !important;
  color: black;
}

.detail {
  padding: 2px 10px 10px 10px;
  width:285px;
  height:280px;
  background-color: navajowhite;
  position: fixed;
  bottom: 5px;
  left: 0;
  right: 0;
  margin: auto;
}

.info {
  width:250px;
}

.info-img {
  float:left;
  width: 60%;
  height: 210px;
}

.info img {
  width:100%;
  height: 100%;
}

.info-room {
  position: relative;
  float: right;
  width: 35%;
  height: 210px;
  text-align: left;
  font-weight: bold;
}

.city {
  width: 100%;
}

.title {
  width: 100%;
  margin-top: 8px;
  font-size: 15px;
}
.distance {
  font-weight: normal;
  color: grey;
  margin-top:10px;
  font-size: 15px;
}

.price {
  font-size: 16px;
  margin-top: 160px;
  position: absolute;
  left:0;
  bottom:0;
}

.book-btn {
  margin-top: 10px;
  width: 100%;
  padding: 5px;
  background-color: darkorange;
  border: 0;
  color: #ebeae6;
  font-size: 15px;
  cursor: pointer;
}

@media only screen and (max-width: 600px) {
  #map {
    height: 450px;
  }

  .detail {
    width: 270px;
  }
}

@media only screen and (min-width: 768px) {
  #map {
    height: 700px;
  }

  .detail {
    width: 300px;
  }
}

@media only screen and (min-width: 1200px) {
  #map {
    height: 1200px;
  }

  .detail {
    width: 320px;
    bottom: 50px;
  }
}

</style>