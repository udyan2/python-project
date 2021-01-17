<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Usermodel extends CI_Model {
 
   public function getUser()
   {
   	$query=$this->db->get('user');
   	return $query->result();
   }

    public function userpost($insertUser) 
    {
    	$query=$this->db->insert('user',$insertUser);
    	return $query;
    }

      public function getprofileId($email) 
    {
    	$this->db->where('email',$email);
    	$query=$this->db->get('user');
    	return $query->result();
    }

    public function updateU($updateUser,$u_id)
    {
    	$this->db->where('u_id',$u_id);
    	$query=$this->db->update('user',$updateUser);
    	return $query;
    }

    public function  deleteuser($u_id)
    {
    	$this->db->where('u_id',$u_id);
    	$query=$this->db->delete('user');
    	return $query;
    }


  }