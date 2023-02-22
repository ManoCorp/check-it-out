# Project Scan by dependency-check

## Image Information

| Property | Value | Property | Value |
| ----------- | ------------- | -------- | ----------------- |
| Project Name: | {{ data['projectInfo']['name'] }} | Created on: |  {{ data['projectInfo']['reportDate'] }} | 

## Summary

| Library/App | Vulnerability | Severity | Installed Version | Fixed Version |
| ----------- | ------------- | -------- | ----------------- | ------------- |
{% for result in data['dependencies'] %}
    {{ result['fileName'] }}
    {% if result['vulnerabilityIds'] %}
        {% for vuln in result['vulnerabilityIds'] %}
            | {{ result['fileName'].split(':')[0] }} | [{{ result['fileName'] }}]({{ vuln['references'][0]['url'] }}) | {{ vuln['severity'] }} {% if vuln['severity'].upper() in ['CRITICAL', 'HIGH'] %} :warning: :fire: {% endif %}| {{ result['fileName'].split(':')[-1] }} |  |
        {% endfor %}
    {% endif %}
{% endfor %}
