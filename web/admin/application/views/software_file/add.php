<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Add Software Files</h3>
            </div>
            <?php echo form_open('software_file/add'); ?>
          	<div class="box-body">
          		<div class="row clearfix">
                <div class="col-md-6">
      						<label for="software" class="control-label">Software</label>
      						<div class="form-group">
      							<select name="software" id="software" class="form-control">
      								<option value="">select Software</option>
      								<?php
      								foreach($all_software as $software)
      								{
      									//$selected = ($webapp['id'] == $this->input->post('fk_test_id')) ? ' selected="selected"' : "";
      									echo '<option value="'.$software['id'].'">'.$software['name'].'</option>';
      								}
      								?>
      							</select>
      						</div>
      					</div>
                <div class="col-md-6">
                  <label for="software_version" class="control-label">Version</label>
                  <div class="form-group">
                    <select name="software_version" id="software_version" class="form-control">
                      <option value="">select Software Version</option>
                      <?php
                      foreach($all_software_versions as $software_version)
                      {
                        //$selected = ($webapp['id'] == $this->input->post('fk_test_id')) ? ' selected="selected"' : "";
                        echo '<option value="'.$software_version['id'].'" fk_software_id="'.$software_version['fk_software_id'].'">'.$software_version['version'].'</option>';
                      }
                      ?>
                    </select>
                  </div>
                </div>
                <div class="col-md-6">
                  <label for="webapp_directory" class="control-label">Web Application Directory</label>
                  <div class="form-group">
                    <select name="webapp_directory" class="form-control">
                      <option value="">select Web Application Directory</option>
                      <?php
                      $counter = 0;
                      foreach($webapps as $webapp)
                      {
                        //$selected = ($webapp['id'] == $this->input->post('fk_test_id')) ? ' selected="selected"' : "";
                        echo '<option value="'.$counter.'">'.$webapp.'</option>';
                        $counter++;
                      }
                      ?>
                    </select>
                  </div>
                </div>
                <div class="col-md-6">
      						<label for="description" class="control-label">Description</label>
      						<div class="form-group">
      							<input type="text" name="description" value="" class="form-control" id="description" />
      						</div>
      					</div>
				</div>
			</div>
          	<div class="box-footer">
            	<button type="submit" class="btn btn-success">
            		<i class="fa fa-refresh"></i>&nbsp;&nbsp;Populate Database
            	</button>
          	</div>
            <?php echo form_close(); ?>
      	</div>
    </div>
</div>
<script type="application/javascript">
$(document).ready(function() {
    let current_id = $("#software option:selected").val() === "" ? -1 : $("#software option:selected").val();
    $("#software_version option[fk_software_id != " + current_id + "]").hide();
    $('#software').change(function(){
    let current_id = $("#software option:selected").val() === "" ? -1 : $("#software option:selected").val();
  	$("#software_version option").show();
    $("#software_version option[fk_software_id != " + current_id + "]").hide();
  });
});
</script>
