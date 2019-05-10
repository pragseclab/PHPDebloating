<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Software Files Listing: <?php echo count($software_files_description) ?> items</h3>
                <div class="box-tools">
                      <a href="<?php echo site_url('software_file/add'); ?>" class="btn btn-success btn-sm">Add</a>
                  </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
          						<th>ID</th>
          						<th>Software</th>
                      <th>Software Version</th>
                      <th>Description</th>
                      <th>Actions</th>
                    </tr>
                    <?php foreach($software_files_description as $c){ ?>
                    <tr>
            						<td><a href="<?php echo site_url('software_file/index/'.$c['id']); ?>"><?php echo $c['id']; ?></a></td>
            						<td><a href="<?php echo site_url('software_file/index/'.$c['id']); ?>"><?php echo $c['name']; ?></a></td>
                        <td><a href="<?php echo site_url('software_file/index/'.$c['id']); ?>"><?php echo $c['version']; ?></a></td>
                        <td><a href="<?php echo site_url('software_file/index/'.$c['id']); ?>"><?php echo $c['description']; ?></a></td>
            						<td>
                            <a href="<?php echo site_url('software_file/debloat_files/'.$c['id']); ?>" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Debloat Files</a>
                            <a href="<?php echo site_url('software_file/debloat_functions/'.$c['id']); ?>" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Debloat Functions</a>
                            &nbsp;
                            <a href="<?php echo site_url('software_file/rewrite_destructors/'.$c['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-refresh"></span> Rewrite Destructors</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
