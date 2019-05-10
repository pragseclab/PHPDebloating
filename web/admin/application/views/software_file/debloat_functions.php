<div class="row">
    <div class="col-md-12">
      	<div class="box box-info">
            <div class="box-header with-border">
              	<h3 class="box-title">Software File Add</h3>
            </div>
            <?php echo form_open('software_file/add'); ?>
          	<div class="box-body">
          		<div class="row clearfix">
                <div class="col-md-3">
      						<label for="software" class="control-label">Software</label>
      						<div class="form-group">
      							<span name="software" class="form-control">
                      PMA4.4.0
                    </span>
      						</div>
      					</div>
                <div class="col-md-3">
                  <label for="description" class="control-label">Description</label>
                  <div class="form-group">
                    <span name="description" class="form-control">
                      pma_400_original
                    </span>
                  </div>
                </div>
                <div class="col-md-6">
                  <label for="webapp_directory" class="control-label">Web Application Directory</label>
                  <div class="form-group">
                    <span name="webapp_directory" class="form-control">
                      /var/www/...
                    </span>
                  </div>
                </div>
                <div class="col-md-12">
                  <label for="test_groups" class="control-label">Test Groups</label>
                  <div class="form-group">
                    <div class="form-check col-lg-2 col-md-3">
                      <input type="checkbox" class="form-check-input" id="exampleCheck1">
                      <label class="form-check-label" for="exampleCheck1">Test Group 1</label>
                    </div>
                    <div class="form-check col-lg-2 col-md-3">
                      <input type="checkbox" class="form-check-input" id="exampleCheck1">
                      <label class="form-check-label" for="exampleCheck1">Test Group 2</label>
                    </div>
                    <div class="form-check col-lg-2 col-md-3">
                      <input type="checkbox" class="form-check-input" id="exampleCheck1">
                      <label class="form-check-label" for="exampleCheck1">Test Group 3</label>
                    </div>
                    <div class="form-check col-lg-2 col-md-3">
                      <input type="checkbox" class="form-check-input" id="exampleCheck1">
                      <label class="form-check-label" for="exampleCheck1">Test Group 4</label>
                    </div>
                  </div>
                </div>
				</div>
			</div>
          	<div class="box-footer">
            	<button type="submit" class="btn btn-success">
            		<i class="fa fa-refresh"></i>&nbsp;&nbsp;Debloat Functions
            	</button>
          	</div>
            <?php echo form_close(); ?>
      	</div>
    </div>
</div>
