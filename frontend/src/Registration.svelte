<script>
  let email = "";
  let isLoading = false;
  let isSuccess = false;
  export let submit;
  let errors = {};
  async function handleSubmit(event) {
    console.log(event);
    console.log(event.target);
    console.log(event.target.inputEmail.value);
    console.log(event.target.inputFirstName.value);
  };
</script>

<style>
  :root {
  --input-padding-x: 1.5rem;
  --input-padding-y: .75rem;
}

body {
  background: #007bff;
  background: linear-gradient(to right, #0062E6, #33AEFF);
}

.card-signin {
  border: 0;
  border-radius: 1rem;
  box-shadow: 0 0.5rem 1rem 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.card-signin .card-title {
  margin-bottom: 2rem;
  font-weight: 300;
  font-size: 1.5rem;
}

.card-signin .card-img-left {
  width: 45%;
  /* Link to your background image using in the property below! */
  background: scroll center url('https://source.unsplash.com/WEQbe2jBg40/414x512');
  background-size: cover;
}

.card-signin .card-body {
  padding: 2rem;
}

.form-signin {
  width: 100%;
}

.form-signin .btn {
  font-size: 80%;
  border-radius: 5rem;
  letter-spacing: .1rem;
  font-weight: bold;
  padding: 1rem;
  transition: all 0.2s;
}

.form-label-group {
  position: relative;
  margin-bottom: 1rem;
}

.form-label-group input {
  height: auto;
  border-radius: 2rem;
}

.form-label-group>input,
.form-label-group>label {
  padding: var(--input-padding-y) var(--input-padding-x);
}

.form-label-group>label {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  margin-bottom: 0;
  /* Override default `<label>` margin */
  line-height: 1.5;
  color: #495057;
  border: 1px solid transparent;
  border-radius: .25rem;
  transition: all .1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
  color: transparent;
}

.form-label-group input:-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-moz-placeholder {
  color: transparent;
}

.form-label-group input::placeholder {
  color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
  padding-top: calc(var(--input-padding-y) + var(--input-padding-y) * (2 / 3));
  padding-bottom: calc(var(--input-padding-y) / 3);
}

.form-label-group input:not(:placeholder-shown)~label {
  padding-top: calc(var(--input-padding-y) / 3);
  padding-bottom: calc(var(--input-padding-y) / 3);
  font-size: 12px;
  color: #777;
}
</style>


<div class="container">
    <div class="row">
      <div class="col-lg-10 col-xl-9 mx-auto">
        <div class="card card-signin flex-row my-5">
          <div class="card-img-left d-none d-md-flex">
             <!-- Background image for card set in CSS! -->
          </div>
          <div class="card-body">
            <h5 class="card-title text-center">Registration</h5>
            <form class="form-signin" on:submit|preventDefault="{handleSubmit}">
              <div class="form-label-group">
                <input type="text" id="inputFirstName" class="form-control" placeholder="First Name" required autofocus>
                <label for="inputFirstName">First Name</label>
              </div>

              <div class="form-label-group">
                <input type="text" id="inputLastName" class="form-control" placeholder="Last Name" required autofocus>
                <label for="inputLastName">Last Name</label>
              </div>

              <div class="form-label-group">
                <input type="date" id="inputDayOfBirth" class="form-control" placeholder="Date of birth" required autofocus>
                <label for="inputLastName">Day of birth</label>
              </div>

              <div class="form-label-group">
                <input type="email" id="inputEmail" class="form-control" placeholder="Email" required>
                <label for="inputEmail">Email</label>
              </div>
              
              <div class="form-label-group">
                <input type="text" id="inputAddress" class="form-control" placeholder="Address" required>
                <label for="inputAddress">Address</label>
              </div>

              <hr>

              <div class="form-label-group">
                <input type="file" id="inputPhotoID" class="form-control" placeholder="Photo ID" required>
                <label for="inputPhotoID">Photo ID</label>
              </div>
              
              <div class="form-label-group">
                <input type="datetime-local" id="inputDueDate" class="form-control" placeholder="Appointment Date & Time" required>
                <label for="inputDueDate">Appointment Date & Time</label>
              </div>

              <!--<div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="agree-tos">
                <label class="custom-control-label small" for="agree-tos">I agree to the Terms of Service and Privacy Policy.</label>
              </div>-->

              <button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Register</button>
              
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>