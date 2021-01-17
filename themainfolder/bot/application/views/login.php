<!DOCTYPE html>
<html lang="en">


<head>
   <?php $this->load->view('layouts/head')?>


<!-- inject css end -->

</head>

<body>

<!-- page wrapper start -->

<div class="page-wrapper">
  
<!-- preloader start -->

<div id="ht-preloader">
  <div class="loader clear-loader"> <span>W</span>
    <span>i</span>
    <span>n</span>
    <span>c</span>
    <span>k</span>
  </div>
</div>

<!-- preloader end -->


<!--header start-->
   <?php $this->load->view('layouts/header')?>



<!--header end-->


<!--hero section start-->

<section class="hero-banner position-relative custom-pt-1 custom-pb-2 bg-dark" data-bg-img="assets/images/bg/02.png">
  <div class="container">
    <div class="row text-white text-center z-index-1">
      <div class="col">
        <h1 class="text-white">Login</h1>
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb justify-content-center bg-transparent p-0 m-0">
            <li class="breadcrumb-item"><a class="text-white" href="#">Home</a>
            </li>
            <li class="breadcrumb-item">Pages</li>
            <li class="breadcrumb-item">Account</li>
            <li class="breadcrumb-item active text-primary" aria-current="page">Login</li>
          </ol>
        </nav>
      </div>
    </div>
    <!-- / .row -->
  </div>
  <!-- / .container -->
  <div class="shape-1 bottom">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
      <path fill="#fff" fill-opacity="1" d="M0,288L48,288C96,288,192,288,288,266.7C384,245,480,203,576,208C672,213,768,267,864,245.3C960,224,1056,128,1152,96C1248,64,1344,96,1392,112L1440,128L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
    </svg>
  </div>
</section>

<!--hero section end--> 


<!--body content start-->

<div class="page-content">

<!--login start-->

<section>
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-7 col-12">
        <img class="img-fluid" src="assets/images/login.png" alt="">
      </div>
      <div class="col-lg-5 col-12">
        <div>
          <?php if($responce1 = $this->session->flashdata('true')): ?>
        <div class="col-lg-6">
        <div class="alert alert-danger"><?php echo $responce1;?></div>
      </div>
    <?php endif;?>
          <h2 class="mb-3">Sign In</h2>
          <form  method="post" action="<?php echo base_url();?>Welcome/loginuser">
            <div class="messages"></div>
            <div class="form-group">
              <input id="form_name" type="text" name="email" class="form-control" placeholder="Enter Email "required="required" data-error="email is required.">
              <div class="help-block with-errors"></div>
            </div>
            <div class="form-group">
              <input id="form_password" type="password" name="password" class="form-control" placeholder="Password" required="required" data-error="password is required.">
              <div class="help-block with-errors"></div>
            </div>
            <div class="form-group mt-4 mb-5">
              <div class="remember-checkbox d-flex align-items-center justify-content-between">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" value="" id="check1">
                  <label class="form-check-label" for="check1">Remember me</label>
                </div> <a class="btn-link" href="#">Forgot Password?</a>
              </div>
            </div> <button class="btn btn-primary">Login Now</button>
          </form>
          <div class="d-flex align-items-center mt-4"> <span class="text-muted mr-1">Don't have an account?</span>
            <a href="signup.html">Sign Up</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!--login end-->


<!--newsletter start-->

<section>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="bg-light bg-pos-l py-6 px-4 px-lg-6 text-center rounded" data-bg-img="assets/images/bg/02.png">
          <div class="mb-5">
            <h2><span class="font-w-4 d-block">Subscribe newsletter</span> now for a custom built</h2>
          </div>
          <div class="row justify-content-center">
            <div class="col-lg-9">
              <div class="subscribe-form text-center">
                <form id="mc-form" class="row mb-3">
                  <div class="col-md">
                    <input type="text" value="" name="NAME" class="name form-control border-0 shadow-sm rounded" id="mc-name" placeholder="Your Name" required="">
                  </div>
                  <div class="col-md">
                    <input type="email" value="" name="EMAIL" class="email form-control border-0 shadow-sm rounded mt-3 mt-md-0" id="mc-email" placeholder="Email Address" required="">
                  </div>
                  <div class="col-md-auto">
                    <input class="btn btn-dark mt-3 mt-md-0" type="submit" name="subscribe" value="Subscribe Now">
                  </div>
                </form>
<small class="text-dark">Get started for 1 Month free trial No Purchace required.</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!--newsletter end-->

</div>

<!--body content end--> 


<!--footer start-->
   <?php $this->load->view('layouts/footer')?>



<!--footer end-->

</div>

<!-- page wrapper end -->

 
<!--back-to-top start-->

<div class="scroll-top"><a class="smoothscroll" href="#top">Scroll Top</a></div>

<!--back-to-top end-->

<!-- inject js start -->

<script src="assets/js/theme-plugin.js"></script>
<script src="assets/js/theme-script.js"></script>

<!-- inject js end -->

</body>


<!-- Mirrored from themeht.com/winck/ltr/login.html by HTTrack Website Copier/3.x [XR&CO'2014], Sat, 26 Dec 2020 10:24:42 GMT -->
</html>
