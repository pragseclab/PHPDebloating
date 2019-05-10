Test_Group,CVE,Software,Version,File Name,Function Name,Triggered
<?php foreach($vulnerable_functions as $v){ ?>
<?php echo implode("_",$test_groups); ?>,<?php echo $v['cve']; ?>,<?php echo $v['name']; ?>,<?php echo $v['version']; ?>,<?php echo $v['file_name']; ?>,<?php echo $v['function_name']; ?>,<?php
 if (in_array((string)$v['id'], array_column($trigerred_vulnerable_function_ids, 'id'))) {
   echo "1";
 }
 else {
   echo "0";
 }
?>

<?php } ?>
