import audit_helper

cs = audit_helper.cs

head = '''<!DOCTYPE html>
<html>
<head>
    <title>蹭课查询</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap-4.0.0.css')}}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css')}}">

    <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="{{ url_for('static', filename='js/jquery-3.2.1.min.js')}}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap-4.0.0.js')}}"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body class="container" style="width: 320px;">
    {% include '_flash.html' %}
    <br>

    {% include '_search.html' %}
    <br>
'''

