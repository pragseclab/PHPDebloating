<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Vulnerabilities Listing:
                  <?php echo count($vulnerability_software) ?> items
                  <?php
                  if (isset($trigerred_vulnerability_ids)) {
                    echo '('.count($trigerred_vulnerability_ids).'/'.count($vulnerability_software).' triggered)';
                  } ?></h3>

            	<div class="box-tools">
                    <a href="<?php echo site_url('vulnerability_software/add'); ?>" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>ID</th>
						<th>CVE</th>
            <th>Software</th>
						<th>Version</th>
            <?php if (isset($trigerred_vulnerability_ids)) echo "<th>Triggered</th>" ?>
						<th>Actions</th>
                </tr>
                <?php foreach($vulnerability_software as $v){ ?>
                <tr>
        						<td><?php echo $v['id']; ?></td>
        						<td><?php echo $v['cve']; ?></td>
                    <td><?php echo $v['name']; ?></td>
        						<td><?php echo $v['version']; ?></td>
                    <?php
                      if (isset($trigerred_vulnerability_ids)) {
                         echo "<td>";
                         if (in_array((string)$v['id'], array_column($trigerred_vulnerability_ids, 'id'))) {
                           echo "<i style='color: green' class='fa fa-check' />";
                         }
                         else {
                           echo "<i style='color: red' class='fa fa-close' />";
                         }
                         echo "</td>";
                       }
                    ?>
        						<td>
                            <a href="<?php echo site_url('vulnerability_software/edit/'.$v['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('vulnerability_software/remove/'.$v['id']); ?>" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
