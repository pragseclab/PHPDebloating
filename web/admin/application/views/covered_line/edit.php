<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Covered Line Edit</h3>
            </div>
			<?php echo form_open('covered_line/edit/'.$covered_line['id']); ?>
			<div class="box-body">
				<div class="row clearfix">
					<div class="col-md-6">
						<label for="fk_file_id" class="control-label">Vulnerable File</label>
						<div class="form-group">
							<select name="fk_file_id" class="form-control">
								<option value="">select vulnerable_file</option>
								<?php 
								foreach($all_vulnerable_files as $vulnerable_file)
								{
									$selected = ($vulnerable_file['id'] == $covered_line['fk_file_id']) ? ' selected="selected"' : "";

									echo '<option value="'.$vulnerable_file['id'].'" '.$selected.'>'.$vulnerable_file['file_name'].'</option>';
								} 
								?>
							</select>
						</div>
					</div>
					<div class="col-md-6">
						<label for="line_number" class="control-label">Line Number</label>
						<div class="form-group">
							<input type="text" name="line_number" value="<?php echo ($this->input->post('line_number') ? $this->input->post('line_number') : $covered_line['line_number']); ?>" class="form-control" id="line_number" />
						</div>
					</div>
					<div class="col-md-6">
						<label for="run" class="control-label">Run</label>
						<div class="form-group">
							<input type="text" name="run" value="<?php echo ($this->input->post('run') ? $this->input->post('run') : $covered_line['run']); ?>" class="form-control" id="run" />
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