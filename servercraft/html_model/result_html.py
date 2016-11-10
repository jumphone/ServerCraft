RESULT='''
{% extends "__APP_NAME___base.html" %}

{% block meta %}
    
{% endblock %}

{% block content %}
 <div style="width: 50%; margin: 0 auto; clear: both;">

    <h2 class="sub-header">{{ h.name }}</h2>

    <p>
        ID: {{ h.id }}
    </p>

    <p>
        Status: {{ h.get_status_display }}
    </p>



    
     </br>
        <a class="btn btn-xs btn-primary" href="/__APP_NAME__/handler/download/{{ h.id }}/">Download</a>
    

</div>
{% endblock %}


{% block script %}
    <script>
        $('#table').bootstrapTable()


    </script>
{% endblock %}
'''
