INDEX=r'''

{% extends "__APP_NAME___base.html" %}

{% block content %}

 <div  style="width: 50%; margin: 0 auto; clear: both;">
    <h2 class="sub-header" title="{{ processing_count }}">__APP_NAME__</h2>
    </br>

    {% if is_full %}

        <h3>Too many visitors! Please try again later.</h3>

    {% else %}
    <div class='col-md-6'>    
        <form id="form" action="/__APP_NAME__/handler/start/" method="POST"  enctype="multipart/form-data">
             {% csrf_token %}  

              <div class="control-group">
                  <!-- Select Basic -->
                  <label class="control-label"><big>Conditions:</big></label>
                        <div class="controls">
                              <select id="id_conditions" name="conditions"  class="input-xlarge">
                              <option value="A">A</option>
                              <option value="B">B</option></select>
                        </div>
              </div> </br>
                  




            <div class="form-group" style="height=800px">
                <label  style='width=50%' ><big>Input Data:</big></label>
                <textarea rows=10 type="text" class="form-control"  name="input_text" id="id_input_text"></textarea>
                <br>
                <input type="file" class="form-control"  name="input_file" >
            </div>

            <div class="form-group">
                <button type="submit" class="btn btn-primary"  >Submit</button>
            </div>
        </form>
     </div>
    <div class='col-md-4 col-md-offset-1' > 
              <button  class="btn btn-success" id='use-exp'>Demo</button>
              <big><b>
              </br></br>Introduction:</br></br>
              XXXXXXXXXXXXXXXXXXXXXXX</br>      
              XXXXXXXXXXXXXXXXXXXXXXX</br>      
              XXXXXXXXXXXXXXXXXXXXXXX</br>      
              XXXXXXXXXXXXXXXXXXXXXXX</br>      
              XXXXXXXXXXXXXXXXXXXXXXX</br>      
              XXXXXXXXXXXXXXXXXXXXXXX</br>      
              XXXXXXXXXXXXXXXXXXXXXXX</br>      



              </b></big></br></br></br>
     </div>
    {% endif %}

 </div>
<script>
exp = function()
{
 
 da = "A\nB\nC\n";
 
 $('#id_input_text').val(da);

}
$('#use-exp').click(exp);
</script>





{% endblock %}


{% block script %}
    <script>
        $('#table').bootstrapTable()


    </script>
{% endblock %}
'''
