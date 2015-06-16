{%- extends 'html_basic.tpl' -%}


<!DOCTYPE html>
<html>
<head>
{%- block header -%}
<meta charset="utf-8" />
<title>{{resources['metadata']['name']}}</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

{% for css in resources.inlining.css -%}
    <style type="text/css">
    {{ css }}
    </style>
{% endfor %}

<!-- Can put analytics code here, if desired -->

<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<link rel="stylesheet" href="/css/ipynb.css">

{%- endblock header -%}
</head>


<body>
{% block body %}

  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">
      {{ super() }}
      <div class="cell border-box-sizing text_cell rendered">
        <div class="prompt input_prompt">
	</div>
	<div class="inner_cell">
	  <div class="text_cell_render border-box-sizing rendered_html">
	    <h3 style="margin-top:0px">Back to main site: <a href="http://www.frankcleary.com">www.frankcleary.com</a></h3>
	  </div>
	</div>
      </div>
    </div>
  </div>
 
{%- endblock body %}
</body>


{% block footer %}
</html>
{% endblock footer %}
