<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Covered Files Listing: <?php echo count($covered_files) ?> items <b><?php echo $test_name; ?></b></h3>
            	<div class="box-tools">
                    <a href="<?php echo site_url('covered_file/add'); ?>" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>ID</th>
						<th>Fk Test Id</th>
						<th>File Name</th>
						<th>Actions</th>
                    </tr>
                    <?php foreach($covered_files as $c){ ?>
                    <tr>
						<td><a href="<?php echo site_url('covered_line/index/'.$c['id']); ?>"><?php echo $c['id']; ?></td>
						<td><a href="<?php echo site_url('covered_line/index/'.$c['id']); ?>"><?php echo $c['fk_test_id']; ?></td>
						<td><a href="<?php echo site_url('covered_line/index/'.$c['id']); ?>"><?php echo $c['file_name']; ?></td>
						<td>
                            <a href="<?php echo site_url('covered_file/edit/'.$c['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('covered_file/remove/'.$c['id']); ?>" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
