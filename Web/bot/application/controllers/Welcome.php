<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {

	 public function __construct() {
        parent::__construct();
        $this->load->model('Loginmodel');
        $this->load->model('Usermodel');

    }
	 

	public function index()
	{
	 
        $this->load->view('welcome_message');
    }

  public function about()
	{
	 
        $this->load->view('about');
    }

    public function contact()
	{
	 
        $this->load->view('contact');
    }

   public function login()
	{
		$this->load->view('login');
	}

  public function signup()
	{
		$this->load->view('signup');
	}

 public function dashboard()
	{
		$this->load->view('dashboard');
	}
// public function profile()
// 	{
// 		$this->load->view('profile');
// 	}


public function valid_password($password = '')
  {
    $password = trim($password);

    $regex_lowercase = '/[a-z]/';
    $regex_uppercase = '/[A-Z]/';
    $regex_number = '/[0-9]/';
    $regex_special = '/[!@#$%^&*()\-_=+{};:,<.>§~]/';

    if (empty($password))
    {
      $this->form_validation->set_message('valid_password', 'The {field} field is required.');

      return FALSE;
    }

    if (preg_match_all($regex_lowercase, $password) < 1)
    {
      $this->form_validation->set_message('valid_password', 'The {field} field must be at least one lowercase letter.');

      return FALSE;
    }

    if (preg_match_all($regex_uppercase, $password) < 1)
    {
      $this->form_validation->set_message('valid_password', 'The {field} field must be at least one uppercase letter.');

      return FALSE;
    }

    if (preg_match_all($regex_number, $password) < 1)
    {
      $this->form_validation->set_message('valid_password', 'The {field} field must have at least one number.');

      return FALSE;
    }

    if (preg_match_all($regex_special, $password) < 1)
    {
      $this->form_validation->set_message('valid_password', 'The {field} field must have at least one special character.' . ' ' . htmlentities('!@#$%^&*()\-_=+{};:,<.>§~'));

      return FALSE;
    }

    if (strlen($password) < 5)
    {
      $this->form_validation->set_message('valid_password', 'The {field} field must be at least 5 characters in length.');

      return FALSE;
    }

    if (strlen($password) > 32)
    {
      $this->form_validation->set_message('valid_password', 'The {field} field cannot exceed 32 characters in length.');

      return FALSE;
    }

    return TRUE;
  }

    public function logout()
     {
      $this->session->sess_destroy(); 
      redirect('Welcome');
     }


  public function profile()
    {
    	 $email=$this->session->userdata('email');  
       $data['getprofileId']=$this->Usermodel->getprofileId($email);
        $this->load->view('profile',$data);
    }

     public function updateuser()
    {
        $u_id=$this->input->post('u_id');
        $username=$this->input->post('username');
        $email=$this->input->post('email');
        $phone=$this->input->post('phone'); 
         $created_at=date('d-m-Y H:i:s');
         $updated_at=date('d-m-Y H:i:s');     
        $updateUser=array(
          'username' =>$username,
          'email' =>$email,
          'phone' =>$phone,
          'created_at'=>$created_at,
          'updated_at'=>$updated_at,
         );
        $updateU=$this->Usermodel->updateU($updateUser,$u_id);
              
        $this->session->set_flashdata('true', 'Your Information Updated Successfully..');
         redirect('Welcome/profile','refresh');           
     }
   
 

	public function loginuser()
	{
		$email=$this->input->post('email');
		$password=$this->input->post('password');
		$adminLogin=$this->Loginmodel->adminLogin($email,$password);
		if($adminLogin->num_rows()>0)
		{
			$sesson=array(
              'email'=>$email,
            );

      $sess= $this->session->set_userdata($sesson);
             redirect('Welcome/dashboard');
		}
		else{
			$this->session->set_flashdata('true', '!oops Something went gone Wrong Please Login Again..');
              redirect('Welcome/login');           
		}
		
	}



    	public function userpost()
	{

      $this->load->library('form_validation');

    $this->form_validation->set_rules('username','Firm Name','required'); 
    $this->form_validation->set_rules('phone', 'Mobile Number ', 'trim|required|regex_match[/^[0-9]{10}$/]');
   $this->form_validation->set_rules('email','Email Id','required|is_unique[user.email]'); 
    $this->form_validation->set_rules('password','Password','trim|required|min_length[8]|max_length[15]|callback_valid_password');
    $this->form_validation->set_rules('conpassword','Confirm Password','trim|required|matches[password]');
        
        //$this->form_validation->set_rules('terms','Terms of Services','required');
          $this->form_validation->set_error_delimiters("<p class='text-danger' style='color:red;'>","</p>");
        
      if($this->form_validation->run())
        {
        $username=$this->input->post('username');
        $gender=$this->input->post('gender');
        $email=$this->input->post('email');
        $phone=$this->input->post('phone');
        $password=$this->input->post('password');     
        $created_at=date('d-m-Y H:i:s');
         $updated_at=date('d-m-Y H:i:s');
         $insertUser=array(
          'username' =>$username,
          'gender' =>$gender,
          'email' =>$email,
          'phone' =>$phone,
          'password' =>$password,  
          'created_at'=>$created_at,
          'updated_at'=>$updated_at,
         );
        $userpost=$this->Usermodel->userpost($insertUser);
      if($userpost)
      {
        
        $sesson=array(
          'email'=>$email,        
    );
        $this->session->set_userdata($sesson);
        echo "<script>alert('Thanks for Registration...')</script>";
         redirect('Welcome/dashboard');
      }
     

        }
    else
        {
          $this->load->view('signup');   
      }      
	}


	public function download()
	{
		$this->load->view('download');
	}


}
?>