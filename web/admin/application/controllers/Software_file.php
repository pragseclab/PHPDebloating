<?php
/*
 * Generated by CRUDigniter v3.2
 * www.crudigniter.com
 */

require 'vendor/autoload.php';
use PhpParser\Error;
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;
use PhpParser\BuilderFactory;
use PhpParser\Node;
use PhpParser\NodeTraverser;
use PhpParser\NodeVisitorAbstract;
use PhpParser\PrettyPrinter;

class software_file extends CI_Controller{
    function __construct()
    {
        parent::__construct();
        $this->load->model('Software_model');
        $this->load->model('Software_file_model');
        $this->load->model('Software_version_model');
    }

    /*
     * Listing of software_files filtered by fk_software_version_id
     */
    function index($id=null)
    {
        if($id==null) {
            $data['software_files'] = $this->Software_file_model->get_all_software_files();
            $data['software'] = null;
            $data['software_version'] = null;
        }
        else
        {
            $data['software_files'] = $this->Software_file_model->get_all_software_files($id);
            $data['software'] = null;
            $data['software_version'] = null;
        }
        $data['_view'] = 'software_file/index';
        $this->load->view('layouts/main',$data);
    }

    /*
     * Adding a new software_file
     */
    function add()
    {
        if(isset($_POST) && count($_POST) > 0)
        {
            $directory_index = $this->input->post('webapp_directory');
            $params = array(
      				'fk_software_version_id' => $this->input->post('software_version'),
              'description' => $this->input->post('description'),
            );
            $files = $this->getDirs('/var/www/html/');
            $dirname = $files[$directory_index];
            $files = $this->getDirContents($dirname);
            $software_file_id = $this->Software_file_model->add_software_file($params, $files);
            redirect('software_file/description');
        }
        else
        {
            $webapps = $this->getDirs('/var/www/html/');
            $data['webapps'] = $webapps;

      			$this->load->model('Software_model');
      			$data['all_software'] = $this->Software_model->get_all_software();

            $this->load->model('Software_version_model');
      			$data['all_software_versions'] = $this->Software_version_model->get_all_software_version();

            $data['_view'] = 'software_file/add';
            $this->load->view('layouts/main',$data);
        }
    }

    /*
     * Editing a software_file
     */
    function edit($id)
    {
        // check if the software_file exists before trying to edit it
        $data['software_file'] = $this->Software_file_model->get_software_file($id);

        if(isset($data['software_file']['id']))
        {
            if(isset($_POST) && count($_POST) > 0)
            {
                $params = array(
        					'fk_test_id' => $this->input->post('fk_test_id'),
        					'file_name' => $this->input->post('file_name'),
                );

                $this->Software_file_model->update_software_file($id,$params);
                redirect('software_file/index');
            }
            else
            {
        				$this->load->model('Test_model');
        				$data['all_tests'] = $this->Test_model->get_all_tests();

                $data['_view'] = 'software_file/edit';
                $this->load->view('layouts/main',$data);
            }
        }
        else
            show_error('The software_file you are trying to edit does not exist.');
    }

    /*
     * Deleting software_file
     */
    function remove($id)
    {
        $software_file = $this->Software_file_model->get_software_file($id);

        // check if the software_file exists before trying to delete it
        if(isset($software_file['id']))
        {
            $this->Software_file_model->delete_software_file($id);
            redirect('software_file/index');
        }
        else
            show_error('The software_file you are trying to delete does not exist.');
    }

    /*
    * Helper functions to get local www directories
    */
    function getDirContents($dir, &$results = array()){
        $files = scandir($dir);

        foreach($files as $key => $value){
            $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
            if(!is_dir($path)) {
                $results[] = $path;
            } else if($value != "." && $value != "..") {
                $this->getDirContents($path, $results);
                //$results[] = $path;
            }
        }

        return $results;
    }
    function getDirs($dir, &$results = array()){
        $files = scandir($dir);

        foreach($files as $key => $value){
            $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
            if(is_dir($path) && $value != "." && $value != "..") {
                $results[] = $path;
            }
        }

        return $results;
    }

    /*
     * Listing of software_files_description
     */
    function description()
    {
        $data['software_files_description'] = $this->Software_file_model->get_all_software_files_descriptions();
        $data['_view'] = 'software_file/description';
        $this->load->view('layouts/main',$data);
    }

    /*
     * Debloating files in software_files for selected description
     */
    function debloat_files($id)
    {
        $software_files = $this->Software_file_model->get_all_software_files_descriptions_to_be_removed($id);
        echo 'Removing '.sizeof($software_files).' Files<br />';
        foreach ($software_files as $software_file) {
            $file_name = $software_file['file_name'];
            if (isset(pathinfo($file_name)['extension']) && pathinfo($file_name)['extension'] == 'php') {
              //Backup the file
              echo $file_name."<br />";
              //copy($file_name, $file_name.'.xsrbackup');
              //$file2 = file_get_contents($path2);
              //if ($file1 !== $file2)
              //    file_put_contents($path2, $file1);
              $handle = fopen($file_name, 'w') or die('Cannot open file:  '.$file_name);
              $data = "<html><head>    <meta charset=\"utf-8\">    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no\">    <title>Error: Target File Has Been Removed</title>    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\" integrity=\"sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u\" crossorigin=\"anonymous\">    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css\" integrity=\"sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp\" crossorigin=\"anonymous\">    <style>        * {            font-family: tahoma;        }        div.container .panel {            position: relative !important;        }        div.container {            width: 50% !important;            height: 50% !important;            overflow: auto !important;            margin: auto !important;            position: absolute !important;            top: 0 !important;            left: 0 !important;            bottom: 0 !important;            right: 0 !important;        }    </style></head><body>    <div class=\"container\">        <div class=\"panel panel-danger center\">            <div class=\"panel-heading\" style=\"text-align: left;\"> Error </div>            <div class=\"panel-body\">                <p class=\"text-center\">                  <?php echo 'This file has been removed (\"'.__FILE__.'\")'; error_log('Removed file called ('.__FILE__.')'); ?>                </p>            </div>        </div>    </div></body></html><?php die(); ?>";
              fwrite($handle, $data);
              fclose($handle);
            }
        }
        echo 'Done';
    }

    /*
     * Debloating functions in software_files for selected description
     */
    function debloat_functions($fk_software_files_description)
    {
        $this->load->model('Covered_line_model');
        $this->load->model('Software_function_model');
        $files = $this->Software_file_model->get_all_software_file_names($fk_software_files_description);
        foreach ($files as $file) {
            $file_name = $file['file_name'];
            if (isset(pathinfo($file_name)['extension']) && pathinfo($file_name)['extension'] == 'php') {
                $covered_lines = $this->Covered_line_model->get_covered_lines_by_filename($file_name);
                $covered_lines = array_map('intval', array_column($covered_lines, 'line_number'));
                $code = file_get_contents($file_name);
                $traverser = new NodeTraverser;
                echo '<hr />' . $file_name . ':<br />';
                $traverser->addVisitor(new DebloatFunctionVisitor($file_name, $file['id'], $covered_lines, $this->Software_function_model));
                $parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP5);
                try {
                    $ast = $parser->parse($code);
                } catch (Error $error) {
                    echo "Parse error at ({$file_name}): {$error->getMessage()}\n";
                    //Continue debloating rest of the files and skip the file with parsing errors
                    continue;
                    //return;
                }
                $debloated_ast = $traverser->traverse($ast);
                $prettyPrinter = new PrettyPrinter\Standard();
                $debloated_code = $prettyPrinter->prettyPrintFile($debloated_ast);
                try {
                  $handle = fopen($file_name, 'w');
                  fwrite($handle, $debloated_code);
                  fclose($handle);
                } catch (Exception $e) {
                    echo 'File doesnt exist<br />';
                }
            }
        }
        echo 'Done<br />';
        $this->debloat_files($fk_software_files_description);
    }

    /*
     * Wraps destructors with code coverage calls to make sure we record correct code coverage
     */
    function rewrite_destructors($fk_software_files_description)
    {
        $files = $this->Software_file_model->get_all_software_file_names($fk_software_files_description);
        foreach ($files as $file) {
            $file_name = $file['file_name'];
            if (isset(pathinfo($file_name)['extension']) && pathinfo($file_name)['extension'] == 'php') {
                $code = file_get_contents($file_name);
                $traverser = new NodeTraverser;
                $traverser->addVisitor(new RewriteDestructorsVisitor($file_name));
                $parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP5);
                try {
                    $ast = $parser->parse($code);
                } catch (Error $error) {
                    echo "Parse error at ({$file_name}): {$error->getMessage()}\n";
                    //Continue debloating rest of the files and skip the file with parsing errors
                    continue;
                    //return;
                }
                $new_ast = $traverser->traverse($ast);
                $prettyPrinter = new PrettyPrinter\Standard();
                $new_code = $prettyPrinter->prettyPrintFile($new_ast);
                try {
                  $handle = fopen($file_name, 'w');
                  fwrite($handle, $new_code);
                  fclose($handle);
                } catch (Exception $e) {
                    echo 'File doesnt exist<br />';
                }
            }
        }
    }
}

class DebloatFunctionVisitor extends NodeVisitorAbstract {

    public $file_name = '';
    public $debloat_function_lines = array();

    public function __construct($file_name, $file_id, $debloat_function_lines, $software_function_model) {
        $this->file_name = $file_name;
        $this->file_id = $file_id;
        $this->debloat_function_lines = $debloat_function_lines;
        $this->software_function_model = $software_function_model;
    }

    public function enterNode(Node $node) {
        if (($node instanceof Node\Stmt\Function_ || $node instanceof Node\Stmt\ClassMethod) // If node is function or method definition And ...
            && sizeof($node->stmts) > 0) { // If function has some executable lines And ...
            // Create function signature e.g., func(a, b, c)
            $params_csv = '';
            for ($i=0; $i < sizeof($node->params); $i++) {
              $params_csv = $params_csv . $node->params[$i]->var->name . ($i < sizeof($node->params) - 1 ? ',' : '');
            }
            $functions_signature = $node->name . '(' . $params_csv . ')';
            // If function is covered, skip
            echo 'Testing coverage ' . $functions_signature . ' for ' . $node->stmts[0]->getType() . ' at ' . $node->stmts[0]->getStartLine() . '-' . $node->getEndLine() . ' in ' . implode(',', $this->debloat_function_lines) . '<br />';
            // debloat_function_lines is of type string, getStartLine() returns int, mind the conversion
            // Testing if first statement inside a function was executed and then deciding the coverage status of the function leads to the following issue:
            /*
             * 197. function PMA_langDetails($lang)
             * 198. {
             * 199.   switch ($lang) {
             * 200.    case 'af':
             * 201.    return array('af|afrikaans', 'af', '');
             * 202.    ...
             */
             // Line 199 is not executed
             // First executed line inside PMA_langDetails is line 200
             // So have to check if any line within the function was executed and not only the first one
             $firstStatementLines = range($node->stmts[0]->getStartLine(), $node->getEndLine());
             if (count(array_intersect($firstStatementLines, $this->debloat_function_lines)) > 0) {
               // Update Database
               echo 'Function is covered ' . $this->file_name . ':' . $node->stmts[0]->getStartLine() . ':' . $functions_signature . '<br />';
               $this->software_function_model->add_software_function($this->file_id, $functions_signature, $node->stmts[0]->getStartLine(), 0, -1);
             }
             else {
               echo 'Removing ' . $this->file_name . ':' . $node->stmts[0]->getStartLine() . ':' . $functions_signature . '<br />';
               // Build replacement structure
               /*
               * echo('This function has been removed ("function_foo") from ("file_bar at line 29")');
               * error_log('Removed function called functionfoo:29@file_bar');
               * die();
               */
               $factory = new BuilderFactory;
               $func_call_echo = $factory->funcCall('echo', ["<html><head>    <meta charset=\"utf-8\">    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no\">    <title>Error, Target Function Has Been Removed</title>    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\" integrity=\"sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u\" crossorigin=\"anonymous\">    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css\" integrity=\"sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp\" crossorigin=\"anonymous\">    <style>        * {            font-family: tahoma;        }        div.container .panel {            position: relative !important;        }        div.container {            width: 50% !important;            height: 50% !important;            overflow: auto !important;            margin: auto !important;            position: absolute !important;            top: 0 !important;            left: 0 !important;            bottom: 0 !important;            right: 0 !important;        }    </style></head><body>    <div class=\"container\">        <div class=\"panel panel-danger center\">            <div class=\"panel-heading\" style=\"text-align: left;\"> Error </div>            <div class=\"panel-body\">                <p class=\"text-center\">                  This function has been removed (\"" . $node->name . "\") from (\"" . $this->file_name . " at line " . $node->stmts[0]->getLine() . "\")                </p>            </div>        </div>    </div></body></html>"]);
               $echo_stmt = new Node\Stmt\Expression($func_call_echo);
               $func_call_error_log = $factory->funcCall('error_log', ['Removed function called ' . $node->name . ':' . $node->stmts[0]->getStartLine() . '@' . $this->file_name ]);
               $error_log_stmt = new Node\Stmt\Expression($func_call_error_log);
               $func_call_die = $factory->funcCall('die');
               $die_stmt = new Node\Stmt\Expression($func_call_die);
               $node->stmts = array($echo_stmt, $error_log_stmt, $die_stmt);
               // dont die
               //$node->stmts = array($echo_stmt, $error_log_stmt);

               // Update Database
               $this->software_function_model->add_software_function($this->file_id, $functions_signature, $node->stmts[0]->getStartLine(), 0, 1);

               //return $node;
               // We can skip traversal of function at enterNode by:
               // return NodeTraverser::DONT_TRAVERSE_CHILDREN;
               // We can try to maintain the same line numbers,
               // writing stuff at the same line or putting empty lines
             }
        }
    }
}

class RewriteDestructorsVisitor extends NodeVisitorAbstract {
    public $file_name = '';

    public function __construct($file_name) {
        $this->file_name = $file_name;
    }

    public function enterNode(Node $node) {
        if (($node instanceof Node\Stmt\Function_ || $node instanceof Node\Stmt\ClassMethod)
            && sizeof($node->stmts) > 0) { // If function has some executable lines And ...
            // Create function signature e.g., func(a, b, c)
            $params_csv = '';
            if (strtolower($node->name) == '__destruct') {
              echo 'Destructor found in ' . $this->file_name . ' at line ' . $node->stmts[0]->getStartLine() . '-' . $node->getEndLine() . '<br />';
              for ($i=0; $i < sizeof($node->params); $i++) {
                $params_csv = $params_csv . $node->params[$i]->var->name . ($i < sizeof($node->params) - 1 ? ',' : '');
              }
              $functions_signature = $node->name . '(' . $params_csv . ')';

              $factory = new BuilderFactory;
              // Prepend calls to exit within destructors

              // $stop_coverage = false;
              $var_stop_coverage = $factory->var('stop_coverage');
              $val_false = $factory->val(False);
              $expr[] = new Node\Stmt\Expression(new Node\Expr\Assign($var_stop_coverage, $val_false));

              /*
               * Pre destructor code
               */
              // function_exists("end_coverage_cav39s8hca")
              $func_exists_end_coverage = $factory->funcCall('function_exists', ['end_coverage_cav39s8hca']);
              // $stop_coverage = !xdebug_code_coverage_started();
              $func_xdebug_cc_started = $factory->funcCall('xdebug_code_coverage_started');
              $not_func_xdebug_cc_started = new Node\Expr\BooleanNot($func_xdebug_cc_started);
              $assign_stop_code_coverage = new Node\Stmt\Expression(new Node\Expr\Assign($var_stop_coverage, $not_func_xdebug_cc_started));
              // xdebug_start_code_coverage();
              $func_xdebug_start_cc = $factory->funcCall('xdebug_start_code_coverage');
              // if (!xdebug_code_coverage_started()) { ... }
              $if_not_xdebug_cc_started = new Node\Stmt\If_($not_func_xdebug_cc_started, ['stmts' => [new Node\Stmt\Expression($func_xdebug_start_cc)]]);
              // if (function_exists("end_coverage_cav39s8hca")) { ... }
              $if_function_exists_1 = new Node\Stmt\If_($func_exists_end_coverage, ['stmts' => [$assign_stop_code_coverage, $if_not_xdebug_cc_started]]);
              $expr[] = $if_function_exists_1;

              // Original destructor code
              foreach ($node->stmts as $key => $value) {
                $expr[] = $value;
              }

              /*
               * Post destructor code
               */
              // end_coverage_cav39s8hca($stop_coverage);
              $func_end_coverage = $factory->funcCall('end_coverage_cav39s8hca', [$var_stop_coverage]);
              // if ($stop_coverage) { ... }
              $if_stop_coverage = new Node\Stmt\If_($var_stop_coverage, ['stmts' => [new Node\Stmt\Expression($func_end_coverage)]]);
              // if (function_exists("end_coverage_cav39s8hca")) { ... }
              $if_function_exists_2 = new Node\Stmt\If_($func_exists_end_coverage, ['stmts' => [$if_stop_coverage]]);
              $expr[] = $if_function_exists_2;

              $node->stmts = $expr;
           }
        }
    }
}
