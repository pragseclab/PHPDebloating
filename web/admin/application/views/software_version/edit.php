<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Edit Software Version</h3>
            </div>
			<?php echo form_open('software_version/edit/'.$software_version['id']); ?>
			<div class="box-body">
				<div class="row clearfix">
					<div class="col-md-6">
						<label for="fk_software_id" class="control-label">Software</label>
						<div class="form-group">
							<select name="fk_software_id" class="form-control">
								<option value="">select software</option>
								<?php
								foreach($all_software as $software)
								{
									$selected = ($software['id'] == $software_version['fk_software_id']) ? ' selected="selected"' : "";

									echo '<option value="'.$software['id'].'" '.$selected.'>'.$software['name'].'</option>';
								}
								?>
							</select>
						</div>
					</div>
					<div class="col-md-6">
						<label for="version" class="control-label">Version</label>
						<div class="form-group">
							<input type="text" name="version" value="<?php echo ($this->input->post('version') ? $this->input->post('version') : $software_version['version']); ?>" class="form-control" id="version" />
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
