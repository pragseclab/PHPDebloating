<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Edit Vulnerable File</h3>
            </div>
			<?php echo form_open('vulnerable_file/edit/'.$vulnerable_file['id']); ?>
			<div class="box-body">
				<div class="row clearfix">
					<div class="col-md-6">
						<label for="fk_vulnerability_software" class="control-label">Software Vulnerability</label>
						<div class="form-group">
							<select name="fk_vulnerability_software" class="form-control">
								<option value="">select Software Vulnerability</option>
								<?php
								foreach($all_vulnerability_software as $vulnerability_software)
								{
									$selected = ($vulnerability_software['id'] == $vulnerable_file['fk_vulnerability_software']) ? ' selected="selected"' : "";
									echo '<option value="'.$vulnerability_software['id'].'" '.$selected.'>'.$vulnerability_software['cve'].' : '.$vulnerability_software['name'].' '.$vulnerability_software['version'].'</option>';
								}
								?>
							</select>
						</div>
					</div>
					<div class="col-md-6">
						<label for="file_name" class="control-label">File Name</label>
						<div class="form-group">
							<input type="text" name="file_name" value="<?php echo ($this->input->post('file_name') ? $this->input->post('file_name') : $vulnerable_file['file_name']); ?>" class="form-control" id="file_name" />
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
