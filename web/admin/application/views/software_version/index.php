<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Software Version Listing: <?php echo count($software_version) ?> items</h3>
            	<div class="box-tools">
                    <a href="<?php echo site_url('software_version/add'); ?>" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>ID</th>
						<th>Software</th>
						<th>Version</th>
						<th>Actions</th>
                    </tr>
                    <?php foreach($software_version as $s){ ?>
                    <tr>
						<td><?php echo $s['id']; ?></td>
						<td><?php echo $s['name']; ?></td>
						<td><?php echo $s['version']; ?></td>
						<td>
                            <a href="<?php echo site_url('software_version/edit/'.$s['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('software_version/remove/'.$s['id']); ?>" class="btn btn-danger btn-xs" onclick="return confirm('Are you sure you want to delete this entry?')"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
