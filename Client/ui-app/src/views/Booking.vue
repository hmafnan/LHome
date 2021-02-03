<template>
    <div class="booking">
      <h3>Welcome to booking for {{ title }}</h3>

      <div v-show="showSuccess" class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Holy {{ booking.name }}!</strong> Your booking added successfully
        <button type="button" @click="showSuccess=false" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <form class="booking-form" autocomplete="off">
        <div class="form-group">
          <label for="name">Name</label>
          <input v-model="booking.name" type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Enter Name">
          <small id="nameHelp" class="form-text text-muted errors" v-show="showErrors">{{bookingErrors.name}}</small>

        </div>
        <div class="form-group">
          <label for="phone">Phone</label>
          <input v-model="booking.phone" type="text" class="form-control" id="phone" placeholder="Enter Phone">
          <small id="phoneHelp" class="form-text text-muted errors" v-show="showErrors">{{bookingErrors.phone}}</small>

        </div>
        <div class="form-group">
          <label for="email">Email address</label>
          <input v-model="booking.email" type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">
          <small id="emailHelp" class="form-text text-muted errors" v-show="showErrors">{{bookingErrors.email}}</small>

        </div>
        <div class="form-group">
          <label for="arrivalTime">Arrival Time</label>
          <input v-model="booking.arrival_time" autocomplete="off" id="arrivalTime" type="text" class="form-control" >
          <small id="arrivalTimeHelp" class="form-text text-muted errors" v-show="showErrors">{{bookingErrors.arrival_time}}</small>
        </div>
        <div class="form-group">
          <label for="departureTime">Departure Time</label>
          <input v-model="booking.departure_time" autocomplete="off" type="text" class="form-control" id="departureTime">
          <small id="departureTimeHelp" class="form-text text-muted errors" v-show="showErrors">{{bookingErrors.departure_time}}</small>
        </div>
        <div class="form-group">
          <label for="extraNotes">Extra Notes</label>
          <textarea v-model="booking.note" class="form-control" id="extraNotes" rows="3"></textarea>
          <small id="noteHelp" class="form-text text-muted errors" v-show="showErrors">{{bookingErrors.note}}</small>
        </div>
        <button @click="submitForm" class="btn btn-primary">Submit</button>
      </form>
    </div>
</template>


<script>
import 'bootstrap/dist/css/bootstrap.css';
import 'jquery-datetimepicker/jquery.datetimepicker.css'
import 'jquery-datetimepicker'

const $ = require('jquery');
const axios = require('axios');
const apiURL = '<API_HOST_URL_HERE>'+ '/api/' // Update later


export default {
  name: "Booking",
  props: {
    title: String
  },
  data () {
    return {
      booking : {
        name: '',
        phone: '',
        email: '',
        arrival_time:'',
        departure_time:'',
        note: '',
        title: ''
      },
      bookingErrors : {
        name: [''],
        phone: [''],
        email: [''],
        arrival_time:[''],
        departure_time:[''],
        note: [''],
        title: ['']
      },
      showErrors:false,
      showSuccess:false,
      errors: {}
    }
  },
  mounted() {
    this.booking.title = this.title;
    $('#arrivalTime').datetimepicker({format:'Y-m-d(G:i:00)'});
    $('#departureTime').datetimepicker({format:'Y-m-d(G:i:00)'});
  },
  methods: {
    submitForm(event) {
      event.preventDefault();
      this.showErrors = false;
      this.showSuccess = false;
      this.booking.arrival_time = $('#arrivalTime').val();
      this.booking.departure_time = $('#departureTime').val();
      axios.post(apiURL + 'booking/create/', this.booking)
      .then(response => {
        this.showSuccess = true;
      })
      .catch(e => {
        this.bookingErrors = e.response.data;
        this.showErrors = true;
      })
    }
  },

  components: {}
}
</script>

<style scoped>

h3 {
  font-size: 1.30rem;
  padding: 20px 5px 5px 5px;
  border-bottom: 1px solid grey;
}
.booking-form {
  padding: 5px;
}
.errors {
  color: red !important;
}

@media only screen and (min-width: 768px) {
  .booking {
    width: 800px;
    margin: 0 auto;
  }
}
</style>