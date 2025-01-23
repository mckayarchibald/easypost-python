# EasyPost Python Test Scripts
How to get started:
<ol>
  <li>Create a virtual environment for your scripts. If you do not have `venv` installed run the following:</li>
  
      pip<version> install virtualenv
        
<li>Afterwards create a new virtual environment for your scripts:</li>

      python<version> -m venv <virtual-environment-name>
     
<li>Activate the virtual environment by running this command:</li>

      source <virtual-environment-name>/bin/activate
<li>Install EasyPost</li>

      pip install easypost
</ol>

When writing a new script add the following to the top to set up the evironment:
```python
import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)
```

>
> The current scripts are tested to work with easypost-9.5.0
>