<script>
  let isViewing = true;
  let isSubmitSuccess = false;
  let isSubmitFail = false;
  let isPreview = false;

  let preview_url = "";
  let errors = {};
  async function handleSubmit(event) {
    event.preventDefault();

    let first_name = event.target.inputFirstName.value;
    let last_name = event.target.inputLastName.value;
    let date_of_birth = event.target.inputDayOfBirth.value;
    let phone = event.target.inputPhone.value;
    let email = event.target.inputEmail.value;
    let address = event.target.inputAddress.value;
    let dueTime = event.target.inputDueDate.value;

    let files = event.target.inputPhotoID.files;
    if (! (files && files[0])) {
        return;
    }
    let photoFile = files[0];

    let data = new FormData();
    data.append('file', photoFile);
    data.append('first_name', first_name);
    data.append('last_name', last_name);
    data.append('date_of_birth', date_of_birth);
    data.append('phone', phone)
    data.append('email', email);
    data.append('address', address);
    data.append('dueTime', dueTime);

    const res = fetch('http://localhost:8000/api/v1/register/', {
        method: 'POST',
        body: data
    })
    .then(response => response.json())
    .then(data => {
        // console.log(data)
        if (data.status == "ok")
        {
            isViewing = false;
            isSubmitSuccess = true;
            isSubmitFail = false;
        }
    })
    .catch(error => {
        // console.error(error)
        isViewing = false;
        isSubmitSuccess = false;
        isSubmitFail = true;
    })
  };

  function handleBack() {
    isViewing = true;
    isSubmitSuccess = false;
    isSubmitFail = false;
  }

  function handleFileChange() {
      var files = !!this.files ? this.files : [];
      if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support

      if (/^image/.test( files[0].type)) { // only image file
          var reader = new FileReader(); // instance of the FileReader
          reader.readAsDataURL(files[0]); // read the local file

          reader.onloadend = function(){ // set image data as background of div
            isPreview = true;
            preview_url = this.result;
          }
      }
  }

  function handlePreview() {
      let fileInputElement = document.getElementByID("inputPhotoID");
      console.log(fileInputElement);
      fileInputElement.click();
  }
  
  let localPeople = 1;
  let antiVirus = 2;
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
  font-size: 2rem;
}

.card-signin .card-img-left {
  width: 45%;
  /* Link to your background image using in the property below! */
  background: scroll center url('/bg.jpeg');  
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

.fileUpload {
    position: relative;
    overflow: hidden;
    height:auto;
    width: 100%;
    text-align: center;
    border: 1px solid #ced4da;
    border-radius: 2rem;
}

.fileUpload input.upload {
    position: absolute;
    top:0;
    right:0;
    margin:0;
    padding:0;
    font-size: 20px;
    cursor: pointer;
    opacity: 0;
    height: 100%;
    text-align: center;
}
.custom-span{font-family:Arial;font-weight:bold;font-size:50px;color:#FE57A1;}
#uploadFile{border:none;margin-left:10px;width:200px;}
.custome-para{font-family:Arial;font-weight:bold;font-size:24px;color:#585858;}

.preview_image {
    width: 100px;
    height: 100px;
    background-position: center center;
    background-size: cover;
    -webkit-box-shadow: 0 0 1px 1px rgba(0, 0, 0, .3);
    display: inline-block;
    margin-top: 6px;
}

#reg-info-box {
    margin: 304px 0;
}

.btn-register {
    color: #fff;
    background-color: #FD2D55;
    border-color: #FD2D55;
}

.btn-back {
    color: #FD2D55;
    border-color: #FD2D55;
}
</style>


<div class="container">
    <div class="row">
      <div class="col-lg-10 col-xl-9 mx-auto">
        <div class="card card-signin flex-row my-5">
          <div class="card-img-left d-none d-md-flex">
             <!-- Background image for card set in CSS! -->
          </div>
          {#if isViewing}
          <div class="card-body">
            <h5 class="card-title text-center font-weight-bold">联防联控信息采集</h5>
            <form class="form-signin" on:submit|preventDefault="{handleSubmit}">
              <div class="form-label-group">
                <input type="text" id="inputName" class="form-control" placeholder="姓名" required>
                <label for="inputName">姓名</label>
              </div>

              <div class="form-label-group">
                <input type="text" id="inputGender" class="form-control" placeholder="性别" required>
                <label for="inputGender">性别</label>
              </div>

              <div class="form-label-group">
                <input type="text" id="inputID" class="form-control" placeholder="身份证号码" required>
                <label for="inputID">身份证号码</label>
              </div>
              
              <div class="form-label-group">
                <input type="text" id="inputAddress" class="form-control" placeholder="地址（商城）：中商广场" required>
                <label for="inputAddress">地址（商城）：中商广场</label>
              </div>

              <div class="form-label-group">
                <input type="phone" id="inputPhone" class="form-control" placeholder="联系电话" required>
                <label for="inputPhone">联系电话</label>
              </div>
              
              <div class="d-flex justify-content-center form-label-group">
                  <div class="form-label-group">
                    <h2><label for="inputLocalPeople">是否常住人口</label></h2>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={localPeople} name="inputLocalPeople" value={1}>
                    	<label for="inputAntiVirus">是</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={localPeople} name="inputLocalPeople" value={2}>
                    	<label for="inputAntiVirus">否</label>
                  </div>
              </div>
              
              <div class="d-flex justify-content-center form-label-group">
                  <div class="form-label-group">
                    <h2><label for="inputAntiVirus">是否接种疫苗</label></h2>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirus} name="inputAntiVirus" value={1}>
                    	<label for="inputAntiVirus">否</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirus} name="inputAntiVirus" value={2}>
                    	<label for="inputAntiVirus">完成第一剂次</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirus} name="inputAntiVirus" value={3}>
                    	<label for="inputAntiVirus">完成第一、二剂次</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirus} name="inputAntiVirus" value={4}>
                    	<label for="inputAntiVirus">完成第一、二、三剂次</label>
                  </div>
              </div>
              
              <div class="d-flex justify-content-center form-label-group">
                <div class="fileUpload">
                    {#if isPreview}
                      <div on:click="{handlePreview}" id="imagePreview" class="preview_image" style="background-image: url({preview_url});"></div>
                    {:else}
                      <span class="custom-span">+</span>
                      <p class="customer-para">上传健康码和行程码</p>                      
                    {/if}
                    <input on:change="{handleFileChange}" type="file" accept="image/*" id="inputPhotoID" class="upload" placeholder="Photo ID" required>
                </div>
              </div>

              <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="agree-tos">
                <label class="custom-control-label small" for="agree-tos">I agree to the Terms of Service and Privacy Policy.</label>
              </div>

              <button class="btn btn-lg btn-register btn-block text-uppercase" type="submit">确认提交</button>
              
            </form>
          </div>
          {/if}

          {#if isSubmitSuccess}
          <div id="reg-info-box" class="card-body">
            <div class="alert alert-primary" role="alert">
                您已经成功上传信息，谢谢合作。
            </div>
            <div class="d-flex justify-content-center">
                <a class="btn btn-back" on:click={handleBack} href="#">返回</a>
            </div>
          </div>
          {/if}

          {#if isSubmitFail}
          <div id="reg-info-box" class="card-body">
            <div class="alert alert-danger" role="alert">
                出现了一些错误，请返回检查。
            </div>
            <div class="d-flex justify-content-center">
                <a class="btn btn-back" on:click={handleBack} href="#">返回</a>
            </div>
          </div>
          {/if}

        </div>
      </div>
    </div>
  </div>