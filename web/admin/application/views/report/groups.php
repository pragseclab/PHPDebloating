<div class="row">
    <div class="col-md-12">
        <div class="box">
            <div class="box-header">
                <h3 class="box-title">Test Groups Listing: <?php echo count($tests) ?> items</h3>
            	<div class="box-tools">
                    <a disabled href="#" onclick="return confirm('Are you sure you want to delete all the data related to tests?')" class="btn btn-danger btn-sm">Remove All</a>
                    <a disabled href="#" class="btn btn-success btn-sm">Add</a>
                    <div class="btn-group" role="group" aria-label="Action button group">
                      <button id="output_html" class="btn btn-success btn-sm">HTML</button>
                      <button id="output_csv" class="btn btn-sm">CSV</button>
                    </div>
                    <div class="btn-group" role="group" aria-label="Action button group">
                      <a href="#" style="cursor: default; background-color:#3c8dbc !important; border-color:#367fa9 !important;" class="btn btn-primary btn-sm">Multi Select</a>
                      <a disabled id="cover_union_a" href="#" class="btn btn-info btn-sm"><span class="fa fa-refresh"></span> Covered Vulnerabilities</a>
                      <a disabled id="file_union_a" href="#" class="btn btn-info btn-sm"><span class="fa fa-file-code-o"></span> File Coverage</a>
                      <a disabled id="function_union_a" href="#" class="btn btn-info btn-sm"><span class="fa fa-code"></span> Function Coverage</a>
                      <a disabled id="line_union_a" href="#" class="btn btn-info btn-sm"><span class="fa fa-bars"></span> Line Coverage</a>
                    </div>
                </div>
            </div>
            <div class="box-body">
                <table class="table table-striped">
                    <tr>
          						<th>#</th>
                      <th>Test Group</th>
                      <th style="width: 90px">Multi Select</th>
          						<th>Actions</th>
                    </tr>
                    <?php $row_num = 1; ?>
                    <?php foreach($tests as $t){ ?>
                    <tr>
          						<td><a href="<?php echo site_url('test/groups/'.$t['test_group']); ?>"><?php echo $row_num; $row_num++; ?></a></td>
          						<td><a href="<?php echo site_url('test/groups/'.$t['test_group']); ?>"><?php echo $t['test_group']; ?></a></td>
                      <td style="text-align: center;">
                        <input type="checkbox" id="<?php echo "chk_".$t['test_group']; ?>" value="<?php echo $t['test_group']; ?>" name="multiselect_chk" />
                      </td>
          						<td>
                        <div class="btn-group html_btn_group" role="group" aria-label="Action button group">
                          <!--<a href="#" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>-->
                          <a href="<?php echo site_url('report/covered_vulnerabilities/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-refresh"></span> Covered Vulnerabilities</a>
                          <a href="<?php echo site_url('report/covered_vulnerable_files/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-file-code-o"></span> File Coverage</a>
                          <a href="<?php echo site_url('report/covered_vulnerable_functions/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-code"></span> Function Coverage</a>
                          <a href="<?php echo site_url('report/covered_vulnerable_lines/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-bars"></span> Line Coverage</a>
                        </div>
                        <div class="btn-group csv_btn_group" role="group" aria-label="Action button group" style="display: none">
                          <!--<a href="#" class="btn btn-info btn-xs"><span class="fa fa-pencil"></span> Edit</a>-->
                          <a href="<?php echo site_url('report/covered_vulnerabilities_csv/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-refresh"></span> Covered Vulnerabilities</a>
                          <a href="<?php echo site_url('report/covered_vulnerable_files_csv/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-file-code-o"></span> File Coverage</a>
                          <a href="<?php echo site_url('report/covered_vulnerable_functions_csv/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-code"></span> Function Coverage</a>
                          <a href="<?php echo site_url('report/covered_vulnerable_lines_csv/'.$t['test_group']); ?>" class="btn btn-info btn-xs"><span class="fa fa-bars"></span> Line Coverage</a>
                        </div>
                          <a disabled href="#" onclick="return confirm('Are you sure you want to delete all the data related to this test group?')" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span> Delete All</a>
                      </td>
                    </tr>
                    <?php } ?>
                  </table>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
$(document).ready(function(){
    var output_format = 'html';
    $('input[name="multiselect_chk"]').change(function() {
          checked_items = [];
          $('input[name="multiselect_chk"]').each(function(){
              if($(this).is(":checked")) {
                checked_items.push($(this).val());
              }
          });
          if (checked_items.length <= 0) {
            $('#cover_union_a').attr('disabled', 'disabled');
            $('#file_union_a').attr('disabled', 'disabled');
            $('#function_union_a').attr('disabled', 'disabled');
            $('#line_union_a').attr('disabled', 'disabled');
            $('#cover_union_a').attr('href', '#');
            $('#file_union_a').attr('href', '#');
            $('#function_union_a').attr('href', '#');
            $('#line_union_a').attr('href', '#');
          }
          else {
            $('#cover_union_a').removeAttr("disabled");
            $('#file_union_a').removeAttr("disabled");
            $('#function_union_a').removeAttr("disabled");
            $('#line_union_a').removeAttr("disabled");
            update_union_hrefs(output_format);
          }
      });
      $('#output_html').click(function(){
        $('#output_html').addClass('btn-success');
        $('#output_csv').removeClass('btn-success');
        $('.html_btn_group').show();
        $('.csv_btn_group').hide();
        output_format = 'html';
        update_union_hrefs(output_format);
      });
      $('#output_csv').click(function(){
        $('#output_html').removeClass('btn-success');
        $('#output_csv').addClass('btn-success');
        $('.html_btn_group').hide();
        $('.csv_btn_group').show();
        output_format = 'csv';
        update_union_hrefs(output_format);
      });
      function update_union_hrefs(output_format)
      {
        if (output_format === 'html') {
          base_href = '<?php echo site_url("report/covered_vulnerabilities/"); ?>';
          $('#cover_union_a').attr('href', base_href + checked_items.join('/'));
          base_href = '<?php echo site_url("report/covered_vulnerable_files/"); ?>';
          $('#file_union_a').attr('href', base_href + checked_items.join('/'));
          base_href = '<?php echo site_url("report/covered_vulnerable_functions/"); ?>';
          $('#function_union_a').attr('href', base_href + checked_items.join('/'));
          base_href = '<?php echo site_url("report/covered_vulnerable_lines/"); ?>';
          $('#line_union_a').attr('href', base_href + checked_items.join('/'));
        } else {
          base_href = '<?php echo site_url("report/covered_vulnerabilities_csv/"); ?>';
          $('#cover_union_a').attr('href', base_href + checked_items.join('/'));
          base_href = '<?php echo site_url("report/covered_vulnerable_files_csv/"); ?>';
          $('#file_union_a').attr('href', base_href + checked_items.join('/'));
          base_href = '<?php echo site_url("report/covered_vulnerable_functions_csv/"); ?>';
          $('#function_union_a').attr('href', base_href + checked_items.join('/'));
          base_href = '<?php echo site_url("report/covered_vulnerable_lines_csv/"); ?>';
          $('#line_union_a').attr('href', base_href + checked_items.join('/'));
        }
      }
});
</script>
