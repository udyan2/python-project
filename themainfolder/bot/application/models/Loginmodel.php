<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Loginmodel extends CI_Model {
 
    public function adminLogin($email,$password) {
         $this->db->select('*');
        $this->db->where("email = '$email' AND password = '$password'");
        $query=$this->db->get('user');
    
    return $query;
    } 
}