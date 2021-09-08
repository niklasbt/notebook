---
layout: default
title: Home
---
# Most recent entries

<ul>
	{% for post in site.posts limit: 5 %}
		<li>
			<h2><a href="{{ post.url }}">[{{ post.date | date_to_string }}] {{ post.title }}</a></h2>
			{{ post.excerpt }}
		</li>
	{% endfor %}
</ul>
