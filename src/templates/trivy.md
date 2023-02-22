# Docker Image Scan by trivy

{% set labels =data['Metadata']['ImageConfig']['config']['Labels'] %}

## Image Information

| Property | Value | Property | Value |
| ----------- | ------------- | -------- | ----------------- |
| Artifact Name: | {{ data['ArtifactName'] }} | Artifact Id |  {{ data['ArtifactName'] }} |
| Artifact Type: | {{ data['ArtifactType'] }} | OS Family | </strong> {{ data['Metadata']['OS']['Family'] }} {{ data['Metadata']['OS']['Name'] }} |
| Image ID: | {{ data['Metadata']['ImageID'][:13] }}...{{ data['Metadata']['ImageID'][-6:] }} | Labels | {% for label in labels.items() %} `{{ label[0] }}: {{ label[1] }}` {% endfor %} |
| Exposed Ports: | {{ ", ".join(data['Metadata']['ImageConfig']['config']['ExposedPorts'].keys()) }} | Architecture: | {{ data['Metadata']['ImageConfig']['architecture'] }} |
| Created on: |  {{ data['Metadata']['ImageConfig']['created'] }} | Stop Signal: | {{ data['Metadata']['ImageConfig']['config']['StopSignal'] }} | 

## Summary

| Library/App | Vulnerability | Severity | Installed Version | Fixed Version |
| ----------- | ------------- | -------- | ----------------- | ------------- |
{% for result in data['Results'] %}{% for vuln in result['Vulnerabilities'] %}| {{ vuln['PkgName'] }} | [{{ vuln[ 'VulnerabilityID'] }}]({{ vuln['PrimaryURL'] }}) | {{ vuln['Severity'] }} {% if vuln['Severity'] in ['CRITICAL', 'HIGH'] %}> :warning : {% endif %}| {{ vuln['InstalledVersion'] }} | {{ vuln['FixedVersion'] }} |
{% endfor %}
{% endfor %}
