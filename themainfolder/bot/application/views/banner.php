<!DOCTYPE html>
 
<html class="loading" lang="en" data-textdirection="ltr">
   
<head>
<title>Admin - Create Banner</title>

    <?php $this->load->view('layouts/head')?>
    
  </head>
  
  <body class="horizontal-layout page-header-light horizontal-menu preload-transitions 2-columns   " data-open="click" data-menu="horizontal-menu" data-col="2-columns">

<?php $this->load->view('layouts/header')?>
<?php $this->load->view('layouts/sidebar')?>

		<div class="main-panel">
			<div class="container">
				<div class="page-inner">
					<div class="page-header">
						<h4 class="page-title">Forms</h4>
						<ul class="breadcrumbs">
							<li class="nav-home">
								<a href="#">
									<i class="flaticon-home"></i>
								</a>
							</li>
							<li class="separator">
								<i class="flaticon-right-arrow"></i>
							</li>
						</ul>
					</div>
					<div class="row">
						<div class="col-md-12">
							<div class="card">
								<div class="card-header">
									<div class="card-title">Create Banner</div>
								</div>
								<div class="card-body">
									<div class="row">
									<form id="myform" enctype="multipart/form-data" action="<?php echo base_url(); ?>Banner/bannerpost" method="post"> 
										<div class="col-md-8 col-lg-8">
											<div class="form-group">
												<label for="email2">Enter Title</label>
												<input type="text" class="form-control" name="b_name" id="email2" placeholder="Enter Title">
											</div>

                                            <div class="form-group">
												<label for="exampleFormControlFile1">Upload Image</label>
												<input type="file" class="form-control-file" name="image" id="exampleFormControlFile1">
											</div>
										</div>
								
									</div>
								</div>
								<div class="card-action">
									<button class="btn btn-success">Submit</button>
								</div>
							</div>
						  </form>
						</div>
					</div>
					<h5>Banner List</h5>
            <div class="col-md-12">
              <table class="table table-responsive">
                <thead>
                   <tr>
                      <th>No.</th>
					  <th>Banner Title</th>
                      <!-- <th>Create Date</th>
                      <th>Updated Date</th> -->
                      <th>Delete</th>
                  </tr>

               <tbody>
                     <?php 
                     $sn=1;
                   foreach ($getBanner as  $row) {
                  
                     ?>
                      <tr>
                       <td><?php echo $sn?></td>
		               <td><?php echo $row->b_name?> </td>
                       <!-- <td><?php echo $row->created_at?> </td>
                       <td><?php echo $row->updated_at?> </td> -->

               
                      <td>
                        <span>
                        <a class=" "
                           href="<?php echo base_url()?>Banner/deleteBanner/<?php echo  $row->b_id?>"><i class="material-icons">delete</i>
                        </a></span>
                        

                    </td>

                      </tr>
                      <?php $sn=$sn+1; }?>
                
                </tbody>
              </table>
            </div>
				</div>
			</div>
 <?php $this->load->view('layouts/footer')?>
			