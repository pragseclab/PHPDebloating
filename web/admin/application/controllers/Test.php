<?php
/*
 * Generated by CRUDigniter v3.2
 * www.crudigniter.com
 */

class Test extends CI_Controller{
    function __construct()
    {
        parent::__construct();
        $this->load->model('Test_model');
    }

    /*
     * Listing of tests
     */
    function index()
    {
        $data['tests'] = $this->Test_model->get_all_tests();

        $data['_view'] = 'test/index';
        $this->load->view('layouts/main',$data);
    }

    /*
     * Adding a new test
     */
    function add()
    {
        if(isset($_POST) && count($_POST) > 0)
        {
            $params = array(
      				'test_name' => $this->input->post('test_name'),
      				'test_date' => $this->input->post('test_date'),
            );

            $test_id = $this->Test_model->add_test($params);
            redirect('test/index');
        }
        else
        {
            $data['_view'] = 'test/add';
            $this->load->view('layouts/main',$data);
        }
    }

    /*
     * Editing a test
     */
    function edit($id)
    {
        // check if the test exists before trying to edit it
        $data['test'] = $this->Test_model->get_test($id);

        if(isset($data['test']['id']))
        {
            if(isset($_POST) && count($_POST) > 0)
            {
                $params = array(
					'test_name' => $this->input->post('test_name'),
					'test_date' => $this->input->post('test_date'),
                );

                $this->Test_model->update_test($id,$params);
                redirect('test/index');
            }
            else
            {
                $data['_view'] = 'test/edit';
                $this->load->view('layouts/main',$data);
            }
        }
        else
            show_error('The test you are trying to edit does not exist.');
    }

    /*
     * Deleting test
     */
    function remove($id)
    {
        $test = $this->Test_model->get_test($id);

        // check if the test exists before trying to delete it
        if(isset($test['id']))
        {
            $this->Test_model->delete_test($id);
            redirect('test/index');
        }
        else
            show_error('The test you are trying to delete does not exist.');
    }

    function remove_group($group_name)
    {
        if(isset($group_name))
        {
            $this->Test_model->delete_all_tests_by_group($group_name);
            redirect('test/groups');
        }
        else
            show_error('The test group you are trying to delete does not exist.');
    }

    /*
     * Deleting all tests and its related covered and included files and lines
     */
    function removeall()
    {
        $this->Test_model->delete_all_tests();
        redirect('test/index');
    }

    /*
     * Listing of test groups
     */
    function groups($id=null)
    {
        if($id==null) {
          // return test groups
          $data['tests'] = $this->Test_model->get_all_test_groups();
          $data['_view'] = 'test/groups';
        }
        else {
          // return all tests within a category
          $data['tests'] = $this->Test_model->get_all_tests_by_group($id);
          $data['_view'] = 'test/index';
        }
        $this->load->view('layouts/main',$data);
    }

    /*
     * Listing of covered vulnerabilities by a test group
     */
     function covered_vulnerabilities($id=null)
     {
       $this->load->model('Vulnerability_software_model');
       if($id==null) {
         $data['vulnerability_software'] = null;
       }
       else {
          $data['vulnerability_software'] = $this->Vulnerability_software_model->get_covered_vulnerabilities_by_test_group($id);
          $data['trigerred_vulnerability_ids'] = $this->Vulnerability_software_model->get_covered_vulnerabilities_id_by_test_group($id);;
       }
       $data['_view'] = 'vulnerability_software/index';
       $this->load->view('layouts/main',$data);
     }
}
