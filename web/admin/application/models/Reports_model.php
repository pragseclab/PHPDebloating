<?php

class Reports_model extends CI_Model
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
             ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
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
             ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
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
             ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
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
             ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
             ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_file.file_name, vulnerable_files.file_name) > 0')
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
                ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id')
                ->order_by('id', 'desc');
            }
            else
            {
                $this->db->select('vulnerable_functions.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name, vulnerable_functions.function_name')
                ->from('tests')
                ->where('INSTR(tests.test_group, "'.$test_group.'") > 0 AND vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
                ->join('vulnerable_functions', 'vulnerable_functions.fk_vulnerable_file = vulnerable_files.id')
                ->order_by('id', 'desc');
            }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable files triggered by tests filtered by tests.test_group
     */
    function get_covered_vulnerable_functions_id_by_test_group($test_group=null, $file_id=null)
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
                 ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
                 ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                 ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                 ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                 ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                 ->join('software', 'software.id = software_version.fk_software_id')
                 ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
                 ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_file.file_name, vulnerable_files.file_name) > 0')
                 ->order_by('id', 'desc');
           }
           else
           {
               $this->db->select('vulnerable_functions.id')
                ->from('tests')
                ->where('INSTR(tests.test_group, "'.$test_group.'") > 0 AND vulnerable_files.id = "'.intval($file_id).'"')
                ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
                ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
                ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
                ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
                ->join('software', 'software.id = software_version.fk_software_id')
                ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
                ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_file.file_name, vulnerable_files.file_name) > 0')
                ->order_by('id', 'desc');
           }
           return $this->db->get()->result_array();
        }
    }

    /*
     * Get all vulnerable files filtered by tests.test_group
     */
    function get_all_vulnerable_files_by_test_group($test_group=null, $function_id=null)
    {
        if ($test_group == null)
          return null;
        else
        {
            $this->db->distinct();
            $this->db->select('vulnerable_files.id, vulnerabilities.cve, software.name, software_version.version, vulnerable_files.file_name')
             ->from('tests')
             ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
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
             ->where('INSTR(tests.test_group, "'.$test_group.'") > 0')
             ->join('vulnerability_software', 'vulnerability_software.fk_version_id = tests.fk_software_version_id')
             ->where('tests.fk_software_version_id = vulnerability_software.fk_version_id')
             ->join('vulnerabilities', 'vulnerabilities.id = vulnerability_software.fk_vulnerability_id')
             ->join('software_version', 'software_version.id = vulnerability_software.fk_version_id')
             ->join('software', 'software.id = software_version.fk_software_id')
             ->join('vulnerable_files', 'vulnerable_file.fk_vulnerability_software = vulnerability_software.id')
             ->join('covered_files', 'covered_files.fk_test_id = tests.id and INSTR(covered_file.file_name, vulnerable_files.file_name) > 0')
             ->order_by('id', 'desc');
           return $this->db->get()->result_array();
        }
    }
}
