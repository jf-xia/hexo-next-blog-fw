{%
  set boot_scripts = [
    'src/bootstrap.js'
  ]
%}

{% for bs in boot_scripts %}
  <script type="text/javascript" src="{{ url_for(theme.js) }}/{{ bs }}?v={{ theme.version }}"></script>
{% endfor %}
<script type="text/javascript" src="//cdn.bootcss.com/mermaid/6.0.0/mermaid.min.js"></script>