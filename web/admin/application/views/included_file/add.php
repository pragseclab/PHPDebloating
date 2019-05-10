<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Covered File Add</h3>
            </div>
            <?php echo form_open('included_file/add'); ?>
          	<div class="box-body">
          		<div class="row clearfix">
					<div class="col-md-6">
						<label for="fk_test_id" class="control-label">Test</label>
						<div class="form-group">
							<select name="fk_test_id" class="form-control">
								<option value="">select test</option>
								<?php
								foreach($all_tests as $test)
								{
									$selected = ($test['id'] == $this->input->post('fk_test_id')) ? ' selected="selected"' : "";

									echo '<option value="'.$test['id'].'" '.$selected.'>'.$test['test_name'].'</option>';
								}
								?>
							</select>
						</div>
					</div>
					<div class="col-md-6">
						<label for="file_name" class="control-label">File Name</label>
						<div class="form-group">
							<input type="text" name="file_name" value="<?php echo $this->input->post('file_name'); ?>" class="form-control" id="file_name" />
						</div>
					</div>
				</div>
			</div>
          	<div class="box-footer">
            	<button type="submit" class="btn btn-success">
            		<i class="fa fa-check"></i> Save
            	</button>
          	</div>
            <?php echo form_close(); ?>
      	</div>
    </div>
</div>
