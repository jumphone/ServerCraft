BASE='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    {% block meta %}
    {% endblock %}

    <title>__APP_NAME__</title>

    <link href="http://app.tianlab.cn/static/css/bootstrap.css" rel="stylesheet">
    <link href="http://app.tianlab.cn/static/css/bootstrap-table.css" rel="stylesheet"/>
    <link href="http://app.tianlab.cn/static/css/dashboard.css" rel="stylesheet">

    <script src="http://app.tianlab.cn/static/js/jquery-1.10.2.js"></script>
    <script src="http://app.tianlab.cn/static/js/bootstrap.js"></script>
    <script src="http://app.tianlab.cn/static/js/bootstrap-table.js"></script>

</head>

<body >
<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/__APP_NAME__/">__APP_NAME__</a>
		
        </div>
        <div class="navbar-collapse collapse">
        </div>
    </div>
</div>

<div class="container-fluid">
    <div class="row">
	</br>
	</br>
	</br>

	  {% block content %}
            {% endblock %}

    </div>
</div>


{% block script %}
{% endblock %}

</body>
</html>
'''