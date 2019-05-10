<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Add Vulnerable Function</h3>
            </div>
            <?php echo form_open('vulnerable_function/add'); ?>
          	<div class="box-body">
          		<div class="row clearfix">
					<div class="col-md-6">
						<label for="fk_vulnerability_software" class="control-label">Software Vulnerability</label>
						<div class="form-group">
							<select name="fk_vulnerability_software" id="fk_vulnerability_software" class="form-control">
								<option value="">select Software Vulnerability</option>
								<?php
								foreach($all_vulnerability_software as $vulnerability_software)
								{
									$selected = ($vulnerability_software['id'] == $this->input->post('fk_vulnerability_software')) ? ' selected="selected"' : "";

									echo '<option value="'.$vulnerability_software['id'].'" '.$selected.'>'.$vulnerability_software['cve'].' : '.$vulnerability_software['name'].' '.$vulnerability_software['version'].'</option>';
								}
								?>
							</select>
						</div>
					</div>
					<div class="col-md-6">
						<label for="fk_vulnerable_file" class="control-label">Vulnerable File</label>
						<div class="form-group">
							<select name="fk_vulnerable_file" id="fk_vulnerable_file" class="form-control">
								<option value="">select Vulnerable File</option>
								<?php
								foreach($all_vulnerable_files as $vulnerable_file)
								{
									$selected = ($vulnerable_file['id'] == $this->input->post('fk_vulnerable_file')) ? ' selected="selected"' : "";

									echo '<option value="'.$vulnerable_file['id'].'" '.$selected.' fk_vulnerability_software="'.$vulnerable_file['fk_vulnerability_software'].'">'.$vulnerable_file['file_name'].'</option>';
								}
								?>
							</select>
						</div>
					</div>
          <div class="col-md-6">
            <label for="line_number" class="control-label">Function Name</label>
            <div class="form-group">
              <input type="text" name="function_name" value="<?php echo $this->input->post('function_name'); ?>" class="form-control" id="function_name" />
            </div>
          </div>
          <div class="col-md-6">
						<label for="line_number" class="control-label">Line Number</label>
						<div class="form-group">
							<input type="text" name="line_number" value="<?php echo $this->input->post('line_number'); ?>" class="form-control" id="line_number" />
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
<script type="application/javascript">
$(document).ready(function() {
    let current_id = $("#fk_vulnerability_software option:selected").val() === "" ? -1 : $("#fk_vulnerability_software option:selected").val();
    $("#fk_vulnerable_file option[fk_vulnerability_software !=" + current_id + "]").hide();
    $('#fk_vulnerability_software').change(function(){
    let current_id = $("#fk_vulnerability_software option:selected").val() === "" ? -1 : $("#fk_vulnerability_software option:selected").val();
  	$("#fk_vulnerable_file option").show();
  	$("#fk_vulnerable_file option[fk_vulnerability_software !=" + current_id + "]").hide();
  });
});
</script>
