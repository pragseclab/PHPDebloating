<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Vulnerable Functions Listing: <?php echo count($vulnerable_functions) ?> items</h3>
            	<div class="box-tools">
                    <a href="<?php echo site_url('vulnerable_function/add'); ?>" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>ID</th>
						<th>CVE</th>
						<th>Software</th>
						<th>Version</th>
            <th>Function Name</th>
            <th>Line Number</th>
						<th>Actions</th>
                    </tr>
                    <?php foreach($vulnerable_functions as $v){ ?>
                    <tr>
						<td><?php echo $v['id']; ?></td>
						<td><?php echo $v['cve']; ?></td>
						<td><?php echo $v['name']; ?></td>
						<td><?php echo $v['version']; ?></td>
            <td><?php echo $v['function_name']; ?></td>
            <td><?php echo $v['line_number']; ?></td>
						<td>
                            <a href="<?php echo site_url('vulnerable_function/edit/'.$v['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('vulnerable_function/remove/'.$v['id']); ?>" class="btn btn-danger btn-xs" onclick="return confirm('Are you sure you want to delete this entry?')"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
