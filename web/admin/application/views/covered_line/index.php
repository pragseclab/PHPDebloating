<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Covered Lines Listing: <?php echo count($covered_lines) ?> items <b><?php echo $file_name; ?></b></h3>
            	<div class="box-tools">
                    <a href="<?php echo site_url('covered_line/add'); ?>" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>ID</th>
						<th>Fk File Id</th>
						<th>Line Number</th>
						<th>Run</th>
						<th>Actions</th>
                    </tr>
                    <?php foreach($covered_lines as $c){ ?>
                    <tr>
						<td><?php echo $c['id']; ?></td>
						<td><?php echo $c['fk_file_id']; ?></td>
						<td><?php echo $c['line_number']; ?></td>
						<td><?php echo $c['run']; ?></td>
						<td>
                            <a href="<?php echo site_url('covered_line/edit/'.$c['id']); ?>" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>
                            <a href="<?php echo site_url('covered_line/remove/'.$c['id']); ?>" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
