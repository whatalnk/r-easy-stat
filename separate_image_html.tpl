{%- extends 'full.tpl' -%}

{% block data_svg scoped -%}
<div class="output_svg output_subarea {{extra_class}}">
<img src="{{ output.metadata.filenames['image/svg+xml'] | path2url }}"
</div>
{%- endblock data_svg %}
