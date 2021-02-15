<?php 

?>
<!DOCTYPE html>

<html lang="en">

<head>
      <base href="<?php echo base_url();?>">  
     <meta charset="utf-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="author" content="Jthemes"> 
     <meta name="description" content="eTreeks - Education & Courses Landing Page Template">
     <meta name="keywords" content="Responsive, HTML5 Template, Jthemes, Courses, Education, Learning, Online Education, Study">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
         
     <!-- SITE TITLE -->
     <title>The Concept Classes</title>
               
     <!-- FAVICON AND TOUCH ICONS  -->
     <link rel="shortcut icon" href="public\images\favicon.ico" type="image/x-icon">
     <link rel="icon" href="public\images\favicon.ico" type="image/x-icon">
     <link rel="apple-touch-icon" sizes="152x152" href="public\images\apple-touch-icon-152x152.png">
     <link rel="apple-touch-icon" sizes="120x120" href="public\images\apple-touch-icon-120x120.png">
     <link rel="apple-touch-icon" sizes="76x76" href="public\images\apple-touch-icon-76x76.png">
     <link rel="apple-touch-icon" href="public\images\apple-touch-icon.png">
     <link rel="icon" href="public\images\apple-touch-icon.png" type="image/x-icon">

     <!-- GOOGLE FONTS -->
     <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet">   
     <link href="https://fonts.googleapis.com/css?family=Muli:400,600,700,800,900&display=swap" rel="stylesheet">

     <!-- BOOTSTRAP CSS -->

     <link href="public\css\bootstrap.min.css" rel="stylesheet">
         
     <!-- FONT ICONS -->
     <link href="https://use.fontawesome.com/releases/v5.11.0/css/all.css" rel="stylesheet" crossorigin="anonymous">    
     <link href="public\css\flaticon.css" rel="stylesheet">

     <!-- PLUGINS STYLESHEET -->
     <link href="public\css\menu.css" rel="stylesheet"> 
     <link id="effect" href="public\css\dropdown-effects\fade-down.css" media="all" rel="stylesheet">
     <link href="public\css\magnific-popup.css" rel="stylesheet"> 
     <link href="public\css\flexslider.css" rel="stylesheet">
     <link href="public\css\owl.carousel.min.css" rel="stylesheet">
     <link href="public\css\owl.theme.default.min.css" rel="stylesheet">

     <!-- ON SCROLL ANIMATION -->
     <link href="public\css\animate.css" rel="stylesheet">
   
     <!-- TEMPLATE CSS -->
     <link href="public\css\style.css" rel="stylesheet">

     <!-- RESPONSIVE CSS -->
     <link href="public\css\responsive.css" rel="stylesheet"> 
   </head>


<body>
<script type="text/javascript">
   $(window).on('load',function(){
       $('#myModal').modal('show');
   });
</script>
        
 <div class="modal show fade" id="myModal">
  <div class="modal-header">
   <a class="close" data-dismiss="modal">×</a>
   <h3>Modal header</h3>
 </div>
 <div class="modal-body">
   <p>One fine body…</p>
 </div>
 <div class="modal-footer">
   <a href="#" class="btn">Close</a>
   <a href="#" class="btn btn-primary">Save changes</a>
 </div>
</div>

<!-- PRELOADER SPINNER
       ============================================= -->		
       <div id="loader-wrapper">
           <div id="loading">
               <div id="loading-center">
                   <div class="cssload-loading"><i></i><i></i><i></i><i></i></div>
               </div>
           </div>
       </div>

<!-- PAGE CONTENT
       ============================================= -->	
       <div id="page" class="page">
            <!-- HEADER
           ============================================= -->
           <header id="header" class="header white-menu navbar-dark">
               <div class="header-wrapper">


                   <!-- MOBILE HEADER -->
                   <div class="wsmobileheader clearfix">	
                       <a id="wsnavtoggle" class="wsanimated-arrow"><span></span></a>	    	
                       <span class="smllogo smllogo-black"><img src="public\images\logo.png" width="40%" height="auto" alt="mobile-logo"></span>
                       <span class="smllogo smllogo-white"><img src="public\images\logo-white.png" width="40%" height="auto" alt="mobile-logo"></span>
                    </div>


                    <!-- NAVIGATION MENU -->
                     <div class="wsmainfull menu clearfix">
                       <div class="wsmainwp clearfix">


                           <div class="desktoplogo"><a href="#hero-9" class="logo-black"><img src="public\images\logo.png" width="70%" height="auto" alt="header-logo"></a></div>
                           <div class="desktoplogo"><a href="#hero-9" class="logo-white"><img src="public\images\logo-white.png" width="70%" height="auto" alt="header-logo"></a></div>


                           <!-- MAIN MENU -->
   <nav class="wsmenu clearfix">
   <ul class="wsmenu-list">


       <!-- SIMPLE NAVIGATION LINK -->
       <li class="nl-simple" aria-haspopup="true"><a href="#hero-9" class="font-weight-bold">Home</a></li>
       <li class="nl-simple" aria-haspopup="true"><a href="#services-2" class="font-weight-bold">Courses</a></li>
       <li class="nl-simple" aria-haspopup="true"><a href="#pricing-2" class="font-weight-bold">About Us</a></li>
       <li class="nl-simple" aria-haspopup="true"><a href="#reviews-1" class="font-weight-bold">Achievers</a></li>
       <li class="nl-simple" aria-haspopup="true"><a href="#footer-1" class="font-weight-bold">Contact Us</a></li>

  </ul>
                           </nav>	<!-- END MAIN MENU -->

                       </div>
                   </div>	<!-- END NAVIGATION MENU -->

               </div>     <!-- End header-wrapper -->
           </header>	<!-- END HEADER -->

           <!-- HERO-9
           ============================================= -->	
           <section id="hero-9" class="bg-scroll hero-section division">
               <div class="container">
                   <div class="row d-flex align-items-center">


                       <!-- HERO TEXT -->
                       <div class="col-md-7">
                           <div class="hero-txt mb-40 white-color">

                               <img class="img img-responsive w-75" style="border-radius:5px;box-shadow:1px 1px 5px #fff;" src="public\images/classes.jpg" /> 
                               
                           </div>
                       </div>	<!-- END HERO TEXT -->


                       <!-- HERO REGISTER FORM -->
                       <div class="col-md-5">
                 
                           <div id="register-form">
           <form action="<?php echo base_url();?>Welcome/login" method="post" >
                    
                        <h4>Admin Login</h4>
                        <br>
                                <div id="input-name" class="col-md-12">
                                    <p>user name*</p>
                                    <input type="text" name="username" class="form-control name" placeholder="Enter user name*" required=""> 
                                </div>
                            <br>

                            <div id="input-name" class="col-md-12">
                                    <p>Enter Password*</p>
                                    <input type="text" name="password" class="form-control name" placeholder="Enter Password*" required=""> 
                                </div>
                            <br>
                                   <!-- Form Button -->
                                   <div class="col-md-12 form-btn">  
                                       <input  type="submit" name="submit" class="btn btn-md btn-rose tra-black-hover submit" value="Login">
                                   </div>
                                                    
                               </form>
                           </div>
                       </div>	<!-- END HERO REGISTER FORM -->
                   
                   </div>    <!-- End row -->
               </div>     <!-- End container -->
           </section>	<!-- END HERO-9 -->

           <!-- BANNER-1
           ============================================= -->
          
         <!-- FOOTER-1
           ============================================= -->
           <footer id="footer-1" class="footer division pt-0">
               <div class="container">

       
                   <!-- BOTTOM FOOTER -->
                   <div class="bottom-footer">
                       <div class="row">


                           <!-- FOOTER COPYRIGHT -->
                           <div class="col-lg-8">
                               <ul class="bottom-footer-list">
                                   <li><p>For More Information Contact</p></li>
                                   <li><p><a href="tel:8889102367">+91 8889102367</a></p></li>
                                   <li><p class="last-li"><a href="mailto:info@theconceptclasses.com">info@theconceptclasses.com</a></p></li>
                               </ul>
                           </div>


                           <!-- FOOTER SOCIALS LINKS -->
                           <div class="col-lg-4 text-right">
                               <ul class="foo-socials text-center clearfix">

                                   <li><a href="#" class="ico-facebook"><i class="fab fa-facebook-f"></i></a></li>
                                   <li><a href="#" class="ico-twitter"><i class="fab fa-twitter"></i></a></li>	 
                                    <li><a href="#" class="ico-youtube"><i class="fab fa-youtube"></i></a></li>			
                                   <li><a href="#" class="ico-instagram"><i class="fab fa-instagram"></i></a></li>																										
                                   <!--
                                   <li><a href="#" class="ico-behance"><i class="fab fa-behance"></i></a></li>	
                                   <li><a href="#" class="ico-dribbble"><i class="fab fa-dribbble"></i></a></li>									
                                       
                                   <li><a href="#" class="ico-linkedin"><i class="fab fa-linkedin-in"></i></a></li>
                                   <li><a href="#" class="ico-pinterest"><i class="fab fa-pinterest-p"></i></a></li>								
                                                                           
                                   <li><a href="#" class="ico-vk"><i class="fab fa-vk"></i></a></li>
                                   <li><a href="#" class="ico-yelp"><i class="fab fa-yelp"></i></a></li>
                                   <li><a href="#" class="ico-yahoo"><i class="fab fa-yahoo"></i></a></li>
                                   -->	

                               </ul>
                           </div>

                   </div>
                   </div>	<!-- END BOTTOM FOOTER -->

               </div>	   <!-- End container -->										
           </footer>	<!-- END FOOTER-1 -->

       </div>	<!-- END PAGE CONTENT -->

       <!-- EXTERNAL SCRIPTS
       ============================================= -->	
       <script src="public\js\jquery-3.3.1.min.js"></script>
     <script src="public\js\bootstrap.min.js"></script> 
     <script src="public\js\modernizr.custom.js"></script>
     <script src="public\js\jquery.easing.js"></script>
     <script src="public\js\jquery.appear.js"></script>
     <script src="public\js\menu.js"></script>
     <script src="public\js\materialize.js"></script> 
     <script src="public\js\jquery.scrollto.js"></script>
     <script src="public\js\jquery.countdown.min.js"></script>
     <script src="public\js\imagesloaded.pkgd.min.js"></script>
     <script src="public\js\isotope.pkgd.min.js"></script>
     <script src="public\js\jquery.flexslider.js"></script>
     <script src="public\js\owl.carousel.min.js"></script>
     <script src="public\js\jquery.magnific-popup.min.js"></script> 
     <script src="public\js\register-form.js"></script> 
     <script src="public\js\comment-form.js"></script>  
     <script src="public\js\jquery.validate.min.js"></script> 
     <script src="public\js\jquery.ajaxchimp.min.js"></script>  

     <!-- Custom Script -->   
     <script src="public\js\custom.js"></script>

   </body>
</html>	