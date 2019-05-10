<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Test Edit</h3>
            </div>
			<?php echo form_open('test/edit/'.$test['id']); ?>
			<div class="box-body">
				<div class="row clearfix">
					<div class="col-md-6">
						<label for="test_name" class="control-label">Test Name</label>
						<div class="form-group">
							<input type="text" name="test_name" value="<?php echo ($this->input->post('test_name') ? $this->input->post('test_name') : $test['test_name']); ?>" class="form-control" id="test_name" />
						</div>
					</div>
					<div class="col-md-6">
						<label for="test_date" class="control-label">Test Date</label>
						<div class="form-group">
							<input type="text" name="test_date" value="<?php echo ($this->input->post('test_date') ? $this->input->post('test_date') : $test['test_date']); ?>" class="has-datetimepicker form-control" id="test_date" />
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