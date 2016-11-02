HANDLER='''
{% extends "__APP_NAME___base.html" %}

{% block meta %}
    <meta http-equiv="refresh" content="5">
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



    {% if h.status == 'Processing' %}
        <img src="http://app.tianlab.cn/static/img/waiting.gif">
    {% elif h.status == 'Finish' %}
     </br>
        <a class="btn btn-xs btn-primary" href="/__APP_NAME__/handler/download/{{ h.id }}/">Download</a>
    {% endif %}

</div>
{% endblock %}


{% block script %}
    <script>
        $('#table').bootstrapTable()


    </script>
{% endblock %}
'''