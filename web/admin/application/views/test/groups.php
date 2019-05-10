<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Test Groups Listing: <?php echo count($tests) ?> items</h3>
            	<div class="box-tools">
                    <a disabled href="#" onclick="return confirm('Are you sure you want to delete all the data related to tests?')" class="btn btn-danger btn-sm">Remove All</a>
                    <a disabled href="#" class="btn btn-success btn-sm">Add</a>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
						<th>#</th>
            <th>Test Group</th>
						<th>Actions</th>
                    </tr>
                    <?php $row_num = 1; ?>
                    <?php foreach($tests as $t){ ?>
                    <tr>
						<td><a href="<?php echo site_url('test/groups/'.$t['test_group']); ?>"><?php echo $row_num; $row_num++; ?></a></td>
						<td><a href="<?php echo site_url('test/groups/'.$t['test_group']); ?>"><?php echo $t['test_group']; ?></a></td>
						<td>
                            <!--<a href="#" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>-->
                            <a href="<?php echo site_url('test/covered_vulnerabilities/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-refresh"></span> Analyse Covered Vulnerabilities</a>
                            <a href="<?php echo site_url('test/remove_group/'.$t['test_group']); ?>" onclick="return confirm('Are you sure you want to delete all the data related to <?php echo $t['test_group']; ?> test group?');" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Delete All</a>
                        </td>
                    </tr>
                    <?php } ?>
                </table>

            </div>
        </div>
    </div>
</div>
