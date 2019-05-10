<?php

class Report extends CI_Controller{
    function __construct()
    {
        parent::__construct();
        $this->load->model('Report_model');
    }

    /*
     * Listing of tests
     */
    function index($id=null)
    {
      $this->load->model('Test_model');
      if($id==null) {
        // return test groups
        $data['tests'] = $this->Test_model->get_all_test_groups();
        $data['_view'] = 'report/groups';
      }
      else {
        // return all tests within a category
        $data['tests'] = $this->Test_model->get_all_tests_by_group($id);
        $data['_view'] = 'report/index';
      }
      $this->load->view('layouts/main',$data);
    }

    /*
     * Listing of covered vulnerabilities by a test group
     */
     function covered_vulnerabilities($id=null)
     {
       $test_groups = $this->_get_test_groups_from_url();
       $this->load->model('Vulnerability_software_model');
       if($id==null) {
         $data['vulnerability_software'] = array();
       }
       elseif (sizeof($test_groups) > 1) {
         $data['vulnerability_software'] = $this->Report_model->get_all_vulnerabilities_by_test_group_array($test_groups);
         $data['trigerred_vulnerability_ids'] = $this->Report_model->get_covered_vulnerabilities_id_by_test_group_array($test_groups);;
       }
       else {
         $data['vulnerability_software'] = $this->Report_model->get_all_vulnerabilities_by_test_group($id);
         $data['trigerred_vulnerability_ids'] = $this->Report_model->get_covered_vulnerabilities_id_by_test_group($id);;
       }
       $data['_view'] = 'report/covered_vulnerabilities';
       $this->load->view('layouts/main',$data);
     }

     /*
      * Listing of covered vulnerabilities by a test group as CSV
      */
      function covered_vulnerabilities_csv($id=null)
      {
        $test_groups = $this->_get_test_groups_from_url();
        $this->load->model('Vulnerability_software_model');
        if($id==null) {
          $data['vulnerability_software'] = array();
        }
        elseif (sizeof($test_groups) > 1) {
          $data['vulnerability_software'] = $this->Report_model->get_all_vulnerabilities_by_test_group_array($test_groups);
          $data['trigerred_vulnerability_ids'] = $this->Report_model->get_covered_vulnerabilities_id_by_test_group_array($test_groups);;
        }
        else {
          $data['vulnerability_software'] = $this->Report_model->get_all_vulnerabilities_by_test_group($id);
          $data['trigerred_vulnerability_ids'] = $this->Report_model->get_covered_vulnerabilities_id_by_test_group($id);;
        }
        $data['test_groups'] = $test_groups;
        //$data['_view'] = 'report/covered_vulnerabilities';
        header('Content-Type: text/csv');
        header('Content-Disposition: inline; filename="covered_vulns_'.implode("_",$test_groups).'.csv"');
        $this->load->view('report/covered_vulnerabilities_csv',$data);
      }

      /*
       * Listing of covered vulnerable files by a test group
       */
      function covered_vulnerable_files($id=null)
      {
        $test_groups = $this->_get_test_groups_from_url();
        if($id==null) {
          $data['vulnerable_files'] = array();
        }
        elseif (sizeof($test_groups) > 1) {
          $data['vulnerable_files'] = $this->Report_model->get_all_vulnerable_files_by_test_group_array($test_groups);
          $data['trigerred_vulnerable_file_ids'] = $this->Report_model->get_covered_vulnerable_files_id_by_test_group_array($test_groups);;
        }
        else {
           $data['vulnerable_files'] = $this->Report_model->get_all_vulnerable_files_by_test_group($id);
           $data['trigerred_vulnerable_file_ids'] = $this->Report_model->get_covered_vulnerable_files_id_by_test_group($id);;
        }
        $data['_view'] = 'report/covered_vulnerable_files';
        $this->load->view('layouts/main',$data);
      }

      /*
       * Listing of covered vulnerable files by a test group as CSV
       */
      function covered_vulnerable_files_csv($id=null)
      {
        $test_groups = $this->_get_test_groups_from_url();
        if($id==null) {
          $data['vulnerable_files'] = array();
        }
        elseif (sizeof($test_groups) > 1) {
          $data['vulnerable_files'] = $this->Report_model->get_all_vulnerable_files_by_test_group_array($test_groups);
          $data['trigerred_vulnerable_file_ids'] = $this->Report_model->get_covered_vulnerable_files_id_by_test_group_array($test_groups);;
        }
        else {
           $data['vulnerable_files'] = $this->Report_model->get_all_vulnerable_files_by_test_group($id);
           $data['trigerred_vulnerable_file_ids'] = $this->Report_model->get_covered_vulnerable_files_id_by_test_group($id);;
        }
        $data['test_groups'] = $test_groups;
        header('Content-Type: text/csv');
        header('Content-Disposition: inline; filename="covered_vuln_files_'.implode("_",$test_groups).'.csv"');
        $this->load->view('report/covered_vulnerable_files_csv',$data);
      }

      /*
       * Listing of covered vulnerable functions by a test group
       */
      function covered_vulnerable_functions($id=null)
      {
        $test_groups = $this->_get_test_groups_from_url();
        if($id==null) {
          $data['vulnerable_functions'] = array();
        }
        elseif (sizeof($test_groups) > 1) {
          $data['vulnerable_functions'] = $this->Report_model->get_all_vulnerable_functions_by_test_group_array($test_groups);
          $data['trigerred_vulnerable_function_ids'] = $this->Report_model->get_covered_vulnerable_function_ids_by_test_group_array($test_groups);;
        }
        else {
           $data['vulnerable_functions'] = $this->Report_model->get_all_vulnerable_functions_by_test_group($id);
           $data['trigerred_vulnerable_function_ids'] = $this->Report_model->get_covered_vulnerable_function_ids_by_test_group($id);
        }
        $data['_view'] = 'report/covered_vulnerable_functions';
        $this->load->view('layouts/main',$data);
      }

      /*
       * Listing of covered vulnerable functions by a test group as CSV
       */
      function covered_vulnerable_functions_csv($id=null)
      {
        $test_groups = $this->_get_test_groups_from_url();
        if($id==null) {
          $data['vulnerable_functions'] = array();
        }
        elseif (sizeof($test_groups) > 1) {
          $data['vulnerable_functions'] = $this->Report_model->get_all_vulnerable_functions_by_test_group_array($test_groups);
          $data['trigerred_vulnerable_function_ids'] = $this->Report_model->get_covered_vulnerable_function_ids_by_test_group_array($test_groups);;
        }
        else {
           $data['vulnerable_functions'] = $this->Report_model->get_all_vulnerable_functions_by_test_group($id);
           $data['trigerred_vulnerable_function_ids'] = $this->Report_model->get_covered_vulnerable_function_ids_by_test_group($id);
        }
        $data['test_groups'] = $test_groups;
        header('Content-Type: text/csv');
        header('Content-Disposition: inline; filename="covered_vuln_functions_'.implode("_",$test_groups).'.csv"');
        $this->load->view('report/covered_vulnerable_functions_csv',$data);
      }

      /*
       * Listing of covered vulnerable functions by a test group
       */
      function covered_vulnerable_lines($id=null)
      {
        $test_groups = $this->_get_test_groups_from_url();
        if($id==null) {
          $data['vulnerable_functions'] = array();
        }
        elseif (sizeof($test_groups) > 1) {
          $data['vulnerable_lines'] = $this->Report_model->get_all_vulnerable_lines_by_test_group_array($test_groups);
          $data['trigerred_vulnerable_line_ids'] = $this->Report_model->get_covered_vulnerable_line_ids_by_test_group_array($test_groups);;
        }
        else {
           $data['vulnerable_lines'] = $this->Report_model->get_all_vulnerable_lines_by_test_group($id);
           $data['trigerred_vulnerable_line_ids'] = $this->Report_model->get_covered_vulnerable_line_ids_by_test_group($id);
        }
        $data['_view'] = 'report/covered_vulnerable_lines';
        $this->load->view('layouts/main',$data);
      }

      /*
       * Listing of covered vulnerable functions by a test group as CSV
       */
      function covered_vulnerable_lines_csv($id=null)
      {
        $test_groups = $this->_get_test_groups_from_url();
        if($id==null) {
          $data['vulnerable_functions'] = array();
        }
        elseif (sizeof($test_groups) > 1) {
          $data['vulnerable_lines'] = $this->Report_model->get_all_vulnerable_lines_by_test_group_array($test_groups);
          $data['trigerred_vulnerable_line_ids'] = $this->Report_model->get_covered_vulnerable_line_ids_by_test_group_array($test_groups);;
        }
        else {
           $data['vulnerable_lines'] = $this->Report_model->get_all_vulnerable_lines_by_test_group($id);
           $data['trigerred_vulnerable_line_ids'] = $this->Report_model->get_covered_vulnerable_line_ids_by_test_group($id);
        }
        $data['test_groups'] = $test_groups;
        header('Content-Type: text/csv');
        header('Content-Disposition: inline; filename="covered_vuln_lines_'.implode("_",$test_groups).'.csv"');
        $this->load->view('report/covered_vulnerable_lines_csv',$data);
      }

     /*
     * Used to parse multiple parameters passed in url separated by / and return an array
     */
     function _get_test_groups_from_url()
     {
       $segments = $this->uri->total_segments();
       $test_groups = array();
       for ($i=3; $i <= $segments; $i++) {
         array_push($test_groups, $this->uri->segment($i));
       }
       return $test_groups;
     }
}
