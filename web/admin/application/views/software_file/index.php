<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Software Files Listing: <?php echo count($software_files) ?> items <b><?php echo $software.' '.$software_version; ?></b></h3>

            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
          						<th>ID</th>
          						<th>Software</th>
                      <th>Software Version</th>
                      <th>Description</th>
          						<th>File Name</th>
                      <th>Line Count</th>
                      <th>Removed</th>
          						<th>Actions</th>
                  </tr>
                  <?php foreach($software_files as $c){ ?>
                  <tr>
            						<td><?php echo $c['id']; ?></td>
            						<td><?php echo $c['name']; ?></td>
                        <td><?php echo $c['version']; ?></td>
                        <td><?php echo $c['description']; ?></td>
            						<td style="max-width: 200px; word-wrap: break-word"><?php echo $c['file_name']; ?></td>
                        <td><?php echo $c['line_count']; ?></td>
                        <td><?php echo $c['removed']; ?></td>
            						<td>
                            <a href="<?php echo site_url('software_file/edit/'.$c['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('software_file/remove/'.$c['id']); ?>" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
