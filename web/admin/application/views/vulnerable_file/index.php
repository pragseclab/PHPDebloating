<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Vulnerable Files Listing: <?php echo count($vulnerable_files) ?> items</h3>
            	<div class="box-tools">
                    <a href="<?php echo site_url('vulnerable_file/add'); ?>" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>ID</th>
						<th>CVE</th>
						<th>Software</th>
            <th>Version</th>
            <th>File Name</th>
						<th>Actions</th>
                    </tr>
                    <?php foreach($vulnerable_files as $v){ ?>
						<td><a href="<?php echo site_url('vulnerable_line/index/'.$v['id']); ?>"><?php echo $v['id']; ?></td>
						<td><a href="<?php echo site_url('vulnerable_line/index/'.$v['id']); ?>"><?php echo $v['cve']; ?></td>
						<td><a href="<?php echo site_url('vulnerable_line/index/'.$v['id']); ?>"><?php echo $v['name']; ?></td>
            <td><a href="<?php echo site_url('vulnerable_line/index/'.$v['id']); ?>"><?php echo $v['version']; ?></td>
            <td><a href="<?php echo site_url('vulnerable_line/index/'.$v['id']); ?>"><?php echo $v['file_name']; ?></td>
						<td>
                            <a href="<?php echo site_url('vulnerable_file/edit/'.$v['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('vulnerable_file/remove/'.$v['id']); ?>" class="btn btn-danger btn-xs" onclick="return confirm('Are you sure you want to delete this entry?')"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
