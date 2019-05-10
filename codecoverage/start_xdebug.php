<?php
    //xdebug_start_code_coverage(XDEBUG_CC_UNUSED | XDEBUG_CC_DEAD_CODE);
    xdebug_start_code_coverage();
    //error_log('starting coverage (main)' . $_SERVER["SCRIPT_FILENAME"]);
    function shutdown_ashd9va()
    {
        // Registering shutdown function inside shutdown function
        // is a trick to make this function be called last!
        register_shutdown_function('shutdown_kdnw92j');
        //error_log('registering second shutdown function' . $_SERVER["SCRIPT_FILENAME"]);
    }

    function shutdown_kdnw92j()
    {
        //error_log('calling end coverage (shutdown)' . $_SERVER["SCRIPT_FILENAME"]);
        end_coverage_cav39s8hca(True);
    }
    function end_coverage_cav39s8hca($caller_shutdown_func=False)
    {
        //error_log(implode(',',$_COOKIE));
        //error_log('stopping coverage (' . xdebug_code_coverage_started() . ') ' . $_SERVER["SCRIPT_FILENAME"]);
        $current_dir = __DIR__;
        $test_name = (isset($_COOKIE['test_name']) && !empty($_COOKIE['test_name'])) ? htmlspecialchars($_COOKIE['test_name'],ENT_QUOTES, 'UTF-8') : 'unknown_test_' . time();
        $fk_software_id = (isset($_COOKIE['software_id']) && !empty($_COOKIE['software_id'])) ? intval($_COOKIE['software_id']) : -1;
        $fk_software_version_id = (isset($_COOKIE['software_version_id']) && !empty($_COOKIE['software_version_id'])) ? intval($_COOKIE['software_version_id']) : -1;
        $test_group = (isset($_COOKIE['test_group']) && !empty($_COOKIE['test_group'])) ? htmlspecialchars($_COOKIE['test_group'],ENT_QUOTES, 'UTF-8') : 'default';
        if ($test_group == 'default') {
            // Try to read values from .htaccess
            $cfg_test_group = getenv('lim_test_group');
            $cfg_test_name = getenv('lim_test_name');
            $cfg_fk_software_id = getenv('lim_software_id');
            $cfg_fk_software_version_id = getenv('lim_software_version_id');
            if (isset($cfg_test_group)) {
                $test_group = $cfg_test_group;
            }
            if (isset($cfg_test_name)) {
                $test_name = $cfg_test_name;
            }
            if (isset($cfg_fk_software_id)) {
                $fk_software_id = $cfg_fk_software_id;
            }
            if (isset($cfg_fk_software_version_id)) {
                $fk_software_version_id = $cfg_fk_software_version_id;
            }
        }
        $dt = new DateTime("now", new DateTimeZone('US/Eastern'));
        $coverageName = $current_dir . '/coverages/coverage-' . $test_name . '-' . $dt->format('m-d-Y_Hi');
        try {
            $codecoverageData = json_encode(xdebug_get_code_coverage());
            if ($caller_shutdown_func) {
              //error_log('calling xdebug stop');
              xdebug_stop_code_coverage(); // true to destroy in memory information, not resuming later
            }
            //file_put_contents($coverageName . '.json', $codecoverageData);
            //$included_files = get_included_files();
            $included_files = array();
            write_to_db_vb76bvgbasc($coverageName, $test_group, $codecoverageData, $included_files, $fk_software_id, $fk_software_version_id);
        } catch (Exception $ex) {
            error_log($ex);
            file_put_contents($coverageName . '.ex', $ex);
        }
    }

    function write_to_db_vb76bvgbasc($coverageName, $test_group, $codecoverageData, $included_files, $fk_software_id, $fk_software_version_id)
    {
        $mysqli = new mysqli("db", "root", "root", "code_coverage");
        $mysqli->autocommit(FALSE);
        if (mysqli_connect_errno())
        {
          error_log(sprintf("Connect failed: %s", mysqli_connect_error()));
          exit();
        }
        // Create test entry
        $test_id = 0;
        if ($stmt = $mysqli->prepare('INSERT INTO tests (test_name, test_group, test_date, fk_software_id, fk_software_version_id) VALUES (?,?,?,?,?) ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id)')) {
      	  $date = date("Y-m-d H:i:s");
      	  $stmt->bind_param("sssii", $coverageName, $test_group, $date, $fk_software_id, $fk_software_version_id);
      	  $res = $stmt->execute();
      	  $test_id = mysqli_insert_id($mysqli);
        }
        else
          error_log($mysqli->error);
        $file_id = 0;
        // bulk insert all
        $str_line_coverage = '';
        foreach (json_decode($codecoverageData) as $filename => $values) { // Iterate over each covered file
          if ($stmt = $mysqli->prepare('INSERT INTO covered_files (file_name, fk_test_id) VALUES (?,?) ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id)')) {
              $stmt->bind_param("si", $filename, $test_id);
              $stmt->execute(); // Insert covered files into the database
  	          $file_id = mysqli_insert_id($mysqli);
          }
          else
            error_log($mysqli->error);
          foreach($values as $line_no => $status) { // Iterate over each covered line
            if ($str_line_coverage !== '') {
              $str_line_coverage = $str_line_coverage . ', ';
            }
            $str_line_coverage = $str_line_coverage . sprintf('(%s,%s,%s)', $line_no, $status, $file_id);
          }
        }
        // Bulk insert covered lines into the database
        if ($stmt = $mysqli->prepare('INSERT IGNORE INTO covered_lines (line_number, run, fk_file_id) VALUES ' . $str_line_coverage)) {
          $stmt->execute();
        }
        else
          error_log($mysqli->error);
        // foreach ($included_files as $filename) {
        //   if ($stmt = $mysqli->prepare('INSERT INTO included_files (file_name, fk_test_id) VALUES (?,?)')) {
        //       $stmt->bind_param("si", $filename, $test_id);
        //       $stmt->execute();
        //   }
        //   else
        //     error_log($mysqli->error);
        // }
        $mysqli->commit();
    }

    register_shutdown_function('shutdown_ashd9va');
    //error_log('registered shutdown_ashd9va as shutdown function');
