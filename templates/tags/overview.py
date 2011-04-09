{% extends 'base.html' %}
{% load thumbnail %}

{%block 'title'%}Taggar{%endblock%}

{%block main%}
    <h1>Taggar</h1>

    <ul>
      {% for tag in keywords %}
        <li>{{tag.name}} ({{tag.n}})</li>
      {% endfor %}
    </ul>
{%endblock%}
