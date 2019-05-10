

<!DOCTYPE html>
<html>
   <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <title>Less is More: PHP Debloating</title>
      <!-- Tell the browser to be responsive to screen width -->
      <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
      <!-- Bootstrap 3.3.6 -->
      <link rel="stylesheet" href="<?php echo site_url('resources/css/bootstrap.min.css');?>">
      <!-- Font Awesome -->
      <link rel="stylesheet" href="<?php echo site_url('resources/css/font-awesome.min.css');?>">
      <!-- Ionicons -->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
      <!-- Datetimepicker -->
      <link rel="stylesheet" href="<?php echo site_url('resources/css/bootstrap-datetimepicker.min.css');?>">
      <!-- Theme style -->
      <link rel="stylesheet" href="<?php echo site_url('resources/css/AdminLTE.min.css');?>">
      <!-- AdminLTE Skins. Choose a skin from the css/skins
         folder instead of downloading all of them to reduce the load. -->
      <link rel="stylesheet" href="<?php echo site_url('resources/css/_all-skins.min.css');?>">
      <!-- jQuery 2.2.3 -->
      <script src="<?php echo site_url('resources/js/jquery-2.2.3.min.js');?>"></script>
      <!-- Bootstrap 3.3.6 -->
      <script src="<?php echo site_url('resources/js/bootstrap.min.js');?>"></script>
      <!-- FastClick -->
      <script src="<?php echo site_url('resources/js/fastclick.js');?>"></script>
      <!-- AdminLTE App -->
      <script src="<?php echo site_url('resources/js/app.min.js');?>"></script>
      <!-- AdminLTE for demo purposes -->
      <script src="<?php echo site_url('resources/js/demo.js');?>"></script>
      <!-- DatePicker -->
      <script src="<?php echo site_url('resources/js/moment.js');?>"></script>
      <script src="<?php echo site_url('resources/js/bootstrap-datetimepicker.min.js');?>"></script>
      <script src="<?php echo site_url('resources/js/global.js');?>"></script>
   </head>
   <body class="hold-transition skin-blue sidebar-mini">
      <div class="wrapper">
         <header class="main-header">
            <!-- Logo -->
            <a href="" class="logo">
               <!-- mini logo for sidebar mini 50x50 pixels -->
               <span class="logo-mini">Less is More</span>
               <!-- logo for regular state and mobile devices -->
               <span class="logo-lg">Less is More</span>
            </a>
            <!-- Header Navbar: style can be found in header.less -->
            <nav class="navbar navbar-static-top">
               <!-- Sidebar toggle button-->
               <a href="#" class="sidebar-toggle" data-toggle="offcanvas" role="button">
               <span class="sr-only">Toggle navigation</span>
               <span class="icon-bar"></span>
               <span class="icon-bar"></span>
               <span class="icon-bar"></span>
               </a>
               <div class="navbar-custom-menu">
                  <ul class="nav navbar-nav">
                     <!-- User Account: style can be found in dropdown.less -->
                     <!--<li class="dropdown user user-menu">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                           <img src="<?php echo site_url('resources/img/user2-160x160.jpg');?>" class="user-image" alt="User Image">
                           <span class="hidden-xs">XS-Shredder</span>
                        </a>
                        <ul class="dropdown-menu">
                           <li class="user-header">
                              <img src="<?php echo site_url('resources/img/user2-160x160.jpg');?>" class="img-circle" alt="User Image">
                              <p>
                                 XS-Shredder
                                 <small>Member since Nov. 2012</small>
                              </p>
                           </li>
                           <li class="user-footer">
                              <div class="pull-left">
                                 <a href="#" class="btn btn-default btn-flat">Profile</a>
                              </div>
                              <div class="pull-right">
                                 <a href="#" class="btn btn-default btn-flat">Sign out</a>
                              </div>
                           </li>
                        </ul>
                     </li>-->
                  </ul>
               </div>
            </nav>
         </header>
         <!-- Left side column. contains the logo and sidebar -->
         <aside class="main-sidebar">
            <!-- sidebar: style can be found in sidebar.less -->
            <section class="sidebar">
               <!-- Sidebar user panel -->
               <div class="user-panel" style="height:40px">
                  <div class="pull-left image">
                     <!--<img src="<?php echo site_url('resources/img/user2-160x160.jpg');?>" class="img-circle" alt="User Image">-->
                  </div>
                  <div class="pull-left info">
                     <p>PHP Debloating</p>
                     <!--<a href="#"><i class="fa fa-circle text-success"></i> Online</a>-->
                  </div>
               </div>
               <!-- sidebar menu: : style can be found in sidebar.less -->
               <ul class="sidebar-menu">
                  <!--<li class="header">MAIN NAVIGATION</li>
                  <li>
                     <a href="<?php echo site_url();?>">
                     <i class="fa fa-dashboard"></i> <span>Dashboard</span>
                     </a>
                  </li>-->
                  <!--<li>
                     <a href="#">
                     <i class="fa fa-file-o"></i> <span>Included File</span>
                     </a>
                     <ul class="treeview-menu">
                        <li class="active">
                           <a href="<?php echo site_url('included_file/add');?>"><i class="fa fa-plus"></i> Add</a>
                        </li>
                        <li>
                           <a href="<?php echo site_url('included_file/index');?>"><i class="fa fa-list-ul"></i> Listing</a>
                        </li>
                     </ul>
                  </li>-->
                  <li class="header">
                    <i class="fa fa-window-maximize"></i><span style="padding-left: 5px">WEB APPLICATIONS</span>
                  </li>
                  <li>
                     <a href="<?php echo site_url('software/index');?>">
                     <i class="fa fa-angle-double-right"></i> <span>Software</span>
                     </a>
                  </li>
                  <li>
                     <a href="<?php echo site_url('software_version/index');?>">
                     <i class="fa fa-angle-double-right"></i> <span>Software Version</span>
                     </a>
                  </li>
                  <li class="header">
                    <i class="fa fa-bar-chart"></i><span style="padding-left: 5px">DYNAMIC ANALYSIS</span>
                  </li>
                  <li>
                    <a href="<?php echo site_url('software_file/description');?>">
                      <i class="fa fa-angle-double-right"></i> <span>Debloating</span>
                    </a>
                  </li>
                  <li>
                    <a href="<?php echo site_url('report');?>">
                      <i class="fa fa-angle-double-right"></i> <span>Report</span>
                    </a>
                  </li>
                  <li class="header">
                    <i class="fa fa-flag"></i><span style="padding-left: 5px">VULNERABILITIES</span>
                  </li>
                  <li>
                     <a href="<?php echo site_url('vulnerability/index');?>">
                     <i class="fa fa-angle-double-right"></i> <span>CVE</span>
                     </a>
                  </li>
                  <li>
                     <a href="<?php echo site_url('vulnerability_software/index');?>">
                     <i class="fa fa-angle-double-right"></i> <span>Software Vulnerabilities</span>
                     </a>
                  </li>
                  <li>
                     <a href="<?php echo site_url('vulnerable_file/index');?>">
                     <i class="fa fa-angle-double-right"></i> <span>Vulnerable Files Mapping</span>
                     </a>
                  </li>
                  <li>
                     <a href="<?php echo site_url('vulnerable_line/index');?>">
                     <i class="fa fa-angle-double-right"></i> <span>Vulnerable Lines Mapping</span>
                     </a>
                  </li>
                  <li>
                     <a href="<?php echo site_url('vulnerable_function/index');?>">
                     <i class="fa fa-angle-double-right"></i> <span>Vulnerable Functions Mapping</span>
                     </a>
                  </li>

                  <!--<li>
                     <a href="#">
                     <i class="fa fa-file"></i> <span>Covered File</span>
                     </a>
                     <ul class="treeview-menu">
                        <li class="active">
                           <a href="<?php echo site_url('covered_file/add');?>"><i class="fa fa-plus"></i> Add</a>
                        </li>
                        <li>
                           <a href="<?php echo site_url('covered_file/index');?>"><i class="fa fa-list-ul"></i> Listing</a>
                        </li>
                     </ul>
                  </li>
                  <li>
                     <a href="#">
                     <i class="fa fa-file-text"></i> <span>Covered Line</span>
                     </a>
                     <ul class="treeview-menu">
                        <li class="active">
                           <a href="<?php echo site_url('covered_line/add');?>"><i class="fa fa-plus"></i> Add</a>
                        </li>
                        <li>
                           <a href="<?php echo site_url('covered_line/index');?>"><i class="fa fa-list-ul"></i> Listing</a>
                        </li>
                     </ul>
                  </li>

                  <li>
                     <a href="#">
                     <i class="fa fa-check-square"></i> <span>Test</span>
                     </a>
                     <ul class="treeview-menu">
                        <li class="active">
                           <a href="<?php echo site_url('test/add');?>"><i class="fa fa-plus"></i> Add</a>
                        </li>
                        <li>
                           <a href="<?php echo site_url('test/index');?>"><i class="fa fa-list-ul"></i> Listing</a>
                        </li>
                        <li>
                           <a href="<?php echo site_url('test/groups');?>"><i class="fa fa-list-ul"></i> Groups</a>
                        </li>
                     </ul>
                  </li>-->
               </ul>
            </section>
            <!-- /.sidebar -->
         </aside>
         <!-- Content Wrapper. Contains page content -->
         <div class="content-wrapper">
            <!-- Main content -->
            <section class="content">
               <?php
                  if(isset($_view) && $_view)
                      $this->load->view($_view);
                  ?>
            </section>
            <!-- /.content -->
         </div>
         <!-- /.content-wrapper -->
         <footer class="main-footer">
            <strong>Generated By <a href="http://www.crudigniter.com/">CRUDigniter</a> 3.2</strong>
         </footer>
         <!-- Control Sidebar -->
         <aside class="control-sidebar control-sidebar-dark">
            <!-- Create the tabs -->
            <ul class="nav nav-tabs nav-justified control-sidebar-tabs">
            </ul>
            <!-- Tab panes -->
            <div class="tab-content">
               <!-- Home tab content -->
               <div class="tab-pane" id="control-sidebar-home-tab">
               </div>
               <!-- /.tab-pane -->
               <!-- Stats tab content -->
               <div class="tab-pane" id="control-sidebar-stats-tab">Stats Tab Content</div>
               <!-- /.tab-pane -->
            </div>
         </aside>
         <!-- /.control-sidebar -->
         <!-- Add the sidebar's background. This div must be placed
            immediately after the control sidebar -->
         <div class="control-sidebar-bg"></div>
      </div>
      <!-- ./wrapper -->
   </body>
</html>
