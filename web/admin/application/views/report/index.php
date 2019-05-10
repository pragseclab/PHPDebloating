<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Tests Listing: <?php echo count($tests) ?> items</h3>
            	<div class="box-tools">
                    <a href="<?php echo site_url('test/removeall'); ?>" onclick="return confirm('Are you sure you want to delete all the data related to tests?')" class="btn btn-danger btn-sm">Remove All</a>
                    <a href="<?php echo site_url('test/add'); ?>" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>ID</th>
						<th>Test Name</th>
            <th>Test Group</th>
            <th>Target Software</th>
            <th>Software Version</th>
						<th>Test Date</th>
						<th>Actions</th>
                    </tr>
                    <?php foreach($tests as $t){ ?>
                    <tr>
						<td><a href="<?php echo site_url('covered_file/index/'.$t['id']); ?>"><?php echo $t['id']; ?></a></td>
						<td><a href="<?php echo site_url('covered_file/index/'.$t['id']); ?>"><?php echo $t['test_name']; ?></a></td>
            <td><a href="<?php echo site_url('covered_file/index/'.$t['id']); ?>"><?php echo $t['test_group']; ?></a></td>
            <td><a href="<?php echo site_url('covered_file/index/'.$t['id']); ?>"><?php echo $t['name']; ?></a></td>
            <td><a href="<?php echo site_url('covered_file/index/'.$t['id']); ?>"><?php echo $t['version']; ?></a></td>
						<td><a href="<?php echo site_url('covered_file/index/'.$t['id']); ?>"><?php echo $t['test_date']; ?></a></td>
						<td>
                            <a href="<?php echo site_url('test/edit/'.$t['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('test/remove/'.$t['id']); ?>" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
