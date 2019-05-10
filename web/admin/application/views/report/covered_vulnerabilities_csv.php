Test_Groups,CVE,Software,Version,Triggered
<?php foreach($vulnerability_software as $v){ ?>
<?php echo implode("_",$test_groups); ?>,<?php echo $v['cve']; ?>,<?php echo $v['name']; ?>,<?php echo $v['version']; ?>,<?php
         if (in_array((string)$v['id'], array_column($trigerred_vulnerability_ids, 'id'))) {
           echo "1";
         }
         else {
           echo "0";
         }
    ?>
    
<?php } ?>
