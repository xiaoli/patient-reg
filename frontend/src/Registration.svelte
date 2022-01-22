<script>
  let isViewing = true;
  let isSubmitSuccess = false;
  let isSubmitFail = false;
  let isPreview = false;
  let isPreview2 = false;
  let isNotLocalPeople = false;
  
  let localPeopleGroup = 1;
  let antiVirusGroup = 2;
  let genderGroup = 3;

  let preview_url = "";
  let preview_url2 = "";
  let errors = {};
  async function handleSubmit(event) {
    event.preventDefault();

    let name = event.target.inputName.value;
    let gender = event.target.inputGender.value;
    let idCardNumber = event.target.inputIdCardNumber.value;
    let businessAddress = event.target.inputBusinessAddress.value;
    let phone = event.target.inputPhone.value;
    let isLocalPeople = event.target.inputLocalPeople.value;
	
	let localAddress = "";
	if (event.target.inputLocalAddress) {
		localAddress = event.target.inputLocalAddress.value;
	}
    
	let antiVirus = event.target.inputAntiVirus.value;

    let files = event.target.inputPhotoID.files;
    if (! (files && files[0])) {
        return;
    }
    let file1 = files[0];
	
    let files2 = event.target.inputPhotoID2.files;
    if (! (files2 && files2[0])) {
        return;
    }
	let file2 = files2[0];

    let data = new FormData();
    data.append('file1', file1);
	data.append('file2', file2);
    data.append('name', name);
    data.append('gender', gender);
    data.append('id_card_number', idCardNumber);
    data.append('phone', phone)
    data.append('business_address', businessAddress);
	data.append('is_local_people', isLocalPeople);
    data.append('local_address', localAddress);
    data.append('anti_virus', antiVirus);

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
  
  function handleFileChange2() {
      var files = !!this.files ? this.files : [];
      if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support

      if (/^image/.test( files[0].type)) { // only image file
          var reader = new FileReader(); // instance of the FileReader
          reader.readAsDataURL(files[0]); // read the local file

          reader.onloadend = function(){ // set image data as background of div
            isPreview2 = true;
            preview_url2 = this.result;
          }
      }
  }

  function handlePreview() {
      let fileInputElement = document.getElementByID("inputPhotoID");
      console.log(fileInputElement);
      fileInputElement.click();
  }
  
  function handlePreview2() {
      let fileInputElement = document.getElementByID("inputPhotoID2");
      console.log(fileInputElement);
      fileInputElement.click();
  }
  
  function handleLocalPeopleClick() {
  	  isNotLocalPeople = false;
  }
  
  function handleNotLocalPeopleClick() {
  	  isNotLocalPeople = true;
  }
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
                <input type="text" id="inputIdCardNumber" class="form-control" placeholder="身份证号码" required>
                <label for="inputIdCardNumber">身份证号码</label>
              </div>
              
              <div class="form-label-group">
                <input type="text" id="inputBusinessAddress" class="form-control" placeholder="地址（商城）：中商广场" required>
                <label for="inputBusinessAddress">地址（商城）：中商广场</label>
              </div>

              <div class="form-label-group">
                <input type="phone" id="inputPhone" class="form-control" placeholder="联系电话" required>
                <label for="inputPhone">联系电话</label>
              </div>
			  
              <div class="form-label-group form-check">
                <div class="form-label-group">
                  <h6><label for="inputGender">性别</label></h6>
                </div>
                <div class="custom-control custom-checkbox">
                  	<input type=radio group={genderGroup} name="inputGender" value={"男"} required>
                  	<label for="inputGender">男</label>
                </div>
                <div class="custom-control custom-checkbox">
                  	<input type=radio group={genderGroup} name="inputGender" value={"女"} required>
                  	<label for="inputGender">女</label>
                </div>
              </div>
              
              <div class="form-label-group form-check">
                  <div class="form-label-group">
                    <h6><label for="inputLocalPeople">是否常住人口</label></h6>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={localPeopleGroup} name="inputLocalPeople" value={"是"} on:click="{handleLocalPeopleClick}" required>
                    	<label for="inputAntiVirus">是</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={localPeopleGroup} name="inputLocalPeople" value={"否"} on:click="{handleNotLocalPeopleClick}" required>
                    	<label for="inputAntiVirus">否</label>
						{#if isNotLocalPeople}
		                <div class="form-label-group">
		                  <input type="text" id="inputLocalAddress" class="form-control" placeholder="暂住地址">
		                  <label for="inputLocalAddress">暂住地址</label>
		                </div>
						{/if}
                  </div>
              </div>
              
              <div class="form-label-group form-check">
                  <div class="form-label-group">
                    <h6><label for="inputAntiVirus">是否接种疫苗</label></h6>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirusGroup} name="inputAntiVirus" value={"否"} required>
                    	<label for="inputAntiVirus">否</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirusGroup} name="inputAntiVirus" value={"第一剂次"} required>
                    	<label for="inputAntiVirus">完成第一剂次</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirusGroup} name="inputAntiVirus" value={"第一、二剂次"} required>
                    	<label for="inputAntiVirus">完成第一、二剂次</label>
                  </div>
                  <div class="custom-control custom-checkbox">
                    	<input type=radio group={antiVirusGroup} name="inputAntiVirus" value={"第一、二、三剂次"} required>
                    	<label for="inputAntiVirus">完成第一、二、三剂次</label>
                  </div>
              </div>
              
              <div class="d-flex justify-content-center form-label-group">
                <div class="fileUpload">
                    {#if isPreview}
                      <div on:click="{handlePreview}" id="imagePreview" class="preview_image" style="background-image: url({preview_url});"></div>
                    {:else}
                      <span class="custom-span">+</span>
                      <p class="customer-para">上传健康码</p>
                    {/if}
                    <input on:change="{handleFileChange}" type="file" accept="image/*" id="inputPhotoID" class="upload" placeholder="健康码" required>
                </div>
			  </div>
              
              <div class="d-flex justify-content-center form-label-group">
			    <div class="fileUpload">
                    {#if isPreview2}
                      <div on:click="{handlePreview2}" id="imagePreview2" class="preview_image" style="background-image: url({preview_url2});"></div>
                    {:else}
                      <span class="custom-span">+</span>
                      <p class="customer-para">上传行程码</p>
                    {/if}
					<input on:change="{handleFileChange2}" type="file" accept="image/*" id="inputPhotoID2" class="upload" placeholder="行程码" required>
                </div>
              </div>
			  
			  <div class="d-grid gap-2">
              	  <button class="btn btn-lg btn-primary btn-register btn-block text-uppercase" type="submit">确认提交</button>
			  </div>
              
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