<?php

class Report_model extends CI_Model
{
    function __construct()
    {
        parent::__construct();
    }

    /*
     * Get all vulnerabilities triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerabilities_id_by_test_group($test_group=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerability_software.id')
             ->from('covered_files')
             ->join('tests', 'tests.id = covered_files.fk_test_id')
             ->where('tests.test_group = "'.$test_group.'"')
             ->join('vulnerable_files', 'INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
             ->join('vulnerability_software', 'vulnerability_software.id = vulnerable_files.fk_vulnerability_software')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             //->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             //->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             //->join('software', 'software.id = software_version.fk_software_id')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerabilities for software being tested
     */
    function get_all_vulnerabilities_by_test_group($test_group=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerability_software.id, vulnerabilities.cve, software.name, software_version.version')
             ->from('tests')
             ->where('tests.test_group = "'.$test_group.'"')
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerabilities triggered by tests filtered by tests.test_groups array
     */
    function get_covered_vulnerabilities_id_by_test_group_array($test_groups=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerability_software.id')
             ->from('covered_files')
             ->join('tests', 'tests.id = covered_files.fk_test_id')
             ->where_in('tests.test_group', $test_groups)
             ->join('vulnerable_files', 'INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
             ->join('vulnerability_software', 'vulnerability_software.id = vulnerable_files.fk_vulnerability_software')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             //->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             //->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             //->join('software', 'software.id = software_version.fk_software_id')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerabilities for software being tested, input is array of test_groups
     */
    function get_all_vulnerabilities_by_test_group_array($test_groups=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerability_software.id, vulnerabilities.cve, software.name, software_version.version')
             ->from('tests')
             ->where_in('tests.test_group', $test_groups)
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable files filtered by tests.test_group
     */
    function get_all_vulnerable_files_by_test_group($test_group=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerable_files.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name')
             ->from('tests')
             ->where('tests.test_group = "'.$test_group.'"')
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable files triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerable_files_id_by_test_group($test_group=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerable_files.id')
             ->from('tests')
             ->where('tests.test_group = "'.$test_group.'"')
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
             ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable files filtered by tests.test_group
     */
    function get_all_vulnerable_files_by_test_group_array($test_groups=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerable_files.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name')
             ->from('tests')
             ->where_in('tests.test_group', $test_groups)
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable files triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerable_files_id_by_test_group_array($test_groups=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerable_files.id')
             ->from('tests')
             ->where_in('tests.test_group', $test_groups)
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
             ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable functions filtered by tests.test_group
     */
    function get_all_vulnerable_functions_by_test_group($test_group=null, $file_id=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            if ($file_id == null)
            {
                $this->db->select('vulnerable_functions.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name, vulnerable_functions.function_name')
                ->from('tests')
                ->where('tests.test_group = "'.$test_group.'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id')
                ->order_by('id', 'desc');
            }
            else
            {
                $this->db->select('vulnerable_functions.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name, vulnerable_functions.function_name')
                ->from('tests')
                ->where('tests.test_group = "'.$test_group.'" AND vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id')
                ->order_by('id', 'desc');
            }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable functions triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerable_function_ids_by_test_group($test_group=null, $file_id=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            if ($file_id == null)
            {
                $this->db->select('vulnerable_functions.id')
                ->from('tests')
                ->where('tests.test_group = "'.$test_group.'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id and covered_lines.run = 1')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id and vulnerable_functions.line_number = covered_lines.line_number')
                ->order_by('id', 'desc');
            }
            else
            {
                $this->db->select('vulnerable_functions.id')
                ->from('tests')
                ->where('tests.test_group = "'.$test_group.'" AND vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id and covered_lines.run = 1')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id and vulnerable_functions.line_number = covered_lines.line_number')
                ->order_by('id', 'desc');
            }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable functions filtered by tests.test_group
     */
    function get_all_vulnerable_functions_by_test_group_array($test_groups=null, $file_id=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
            $this->db->distinct();
            if ($file_id == null)
            {
                $this->db->select('vulnerable_functions.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name, vulnerable_functions.function_name')
                ->from('tests')
                ->where_in('tests.test_group', $test_groups)
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id')
                ->order_by('id', 'desc');
            }
            else
            {
                $this->db->select('vulnerable_functions.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name, vulnerable_functions.function_name')
                ->from('tests')
                ->where('tests.test_group = "'.$test_groups.'" AND vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id')
                ->order_by('id', 'desc');
            }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable functions triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerable_function_ids_by_test_group_array($test_groups=null, $file_id=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
            $this->db->distinct();
            if ($file_id == null)
            {
                $this->db->select('vulnerable_functions.id')
                ->from('tests')
                ->where_in('tests.test_group', $test_groups)
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id and covered_lines.run = 1')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id and vulnerable_functions.line_number = covered_lines.line_number')
                ->order_by('id', 'desc');
            }
            else
            {
                $this->db->select('vulnerable_functions.id')
                ->from('tests')
                ->where('tests.test_group = "'.$test_groups.'" AND vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id and covered_lines.run = 1')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id and vulnerable_functions.line_number = covered_lines.line_number')
                ->order_by('id', 'desc');
            }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable files triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerable_line_ids_by_test_group($test_group=null, $file_id=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            if ($file_id == null)
            {
                $this->db->select('vulnerable_lines.id')
                 ->from('tests')
                 ->where('tests.test_group = "'.$test_group.'"')
                 ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                 //->where('covered_lines.run = 1')
                 ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                 ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                 ->join('software', 'software.id = software_version.fk_software_id')
                 ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                 ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                 ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                 ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id and covered_lines.line_number = vulnerable_lines.line_number')
                 ->order_by('id', 'desc');
           }
           else
           {
               $this->db->select('vulnerable_lines.id')
                ->from('tests')
                ->where('tests.test_group = "'.$test_group.'" and vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                //->where('covered_lines.run = 1')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id and covered_lines.line_number = vulnerable_lines.line_number')
                ->order_by('id', 'desc');
           }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable lines filtered by tests.test_group
     */
    function get_all_vulnerable_lines_by_test_group($test_group=null, $file_id=null)
    {
        if ($test_group == null)
          return null;
        else
        {
          $this->db->distinct();
          if ($file_id == null)
          {
              $this->db->select('vulnerable_lines.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name, vulnerable_lines.line_number')
               ->from('tests')
               ->where('tests.test_group = "'.$test_group.'"')
               ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
               //->where('covered_lines.run = 1')
               ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
               ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
               ->join('software', 'software.id = software_version.fk_software_id')
               ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
               ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
               ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id')
               ->order_by('id', 'desc');
         }
         else
         {
             $this->db->select('vulnerable_lines.id')
              ->from('tests')
              ->where('tests.test_group = "'.$test_group.'" and vulnerable_files.id = "'.intval($file_id).'"')
              ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
              //->where('covered_lines.run = 1')
              ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
              ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
              ->join('software', 'software.id = software_version.fk_software_id')
              ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
              ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
              ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id')
              ->order_by('id', 'desc');
         }
         return $this->db->get()->result_array();
       }
    }

    /*
     * Get all vulnerable files triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerable_line_ids_by_test_group_array($test_groups=null, $file_id=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
            $this->db->distinct();
            if ($file_id == null)
            {
                $this->db->select('vulnerable_lines.id')
                 ->from('tests')
                 ->where_in('tests.test_group', $test_groups)
                 ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                 //->where('covered_lines.run = 1')
                 ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                 ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                 ->join('software', 'software.id = software_version.fk_software_id')
                 ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                 ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                 ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                 ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id and covered_lines.line_number = vulnerable_lines.line_number')
                 ->order_by('id', 'desc');
           }
           else
           {
               $this->db->select('vulnerable_lines.id')
                ->from('tests')
                ->where('tests.test_group = "'.$test_groups.'" and vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                //->where('covered_lines.run = 1')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
                ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
                ->join('covered_lines', 'covered_lines.fk_file_id = covered_files.id')
                ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id and covered_lines.line_number = vulnerable_lines.line_number')
                ->order_by('id', 'desc');
           }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable lines filtered by tests.test_group
     */
    function get_all_vulnerable_lines_by_test_group_array($test_groups=null, $file_id=null)
    {
        if ($test_groups == null)
          return null;
        else
        {
          $this->db->distinct();
          if ($file_id == null)
          {
              $this->db->select('vulnerable_lines.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name, vulnerable_lines.line_number')
               ->from('tests')
               ->where_in('tests.test_group', $test_groups)
               ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
               //->where('covered_lines.run = 1')
               ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
               ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
               ->join('software', 'software.id = software_version.fk_software_id')
               ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
               ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
               ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id')
               ->order_by('id', 'desc');
         }
         else
         {
             $this->db->select('vulnerable_lines.id')
              ->from('tests')
              ->where('tests.test_group = "'.$test_groups.'" and vulnerable_files.id = "'.intval($file_id).'"')
              ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
              //->where('covered_lines.run = 1')
              ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
              ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
              ->join('software', 'software.id = software_version.fk_software_id')
              ->join('vulnerable_files', 'vulnerable_files.fk_vulnerability_software = vulnerability_software.id')
              ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_files.file_name, vulnerable_files.file_name) > 0')
              ->join('vulnerable_lines', 'vulnerable_lines.fk_vulnerable_file = vulnerable_files.id')
              ->order_by('id', 'desc');
         }
         return $this->db->get()->result_array();
       }
    }

}
