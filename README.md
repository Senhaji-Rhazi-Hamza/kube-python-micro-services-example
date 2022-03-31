# kube-python-micro-services-example

### What is about
This project aims to serve as a didactic example, on how to deploy python micro services inside a kubernetes

### Pre-requisite
```
# as a pre-requisite you should have poetry installed, otherwise check poetry installation --> https://python-poetry.org/docs/#installation

# install dependencies with 

poetry install
```
### Usage

#### List available commands:

```
sh bin/cli.sh --help
```

#### Use sum functionality :

```
sh bin/cli.sh sum_cmd -e 3 -e 4
# result 
>>the result sum of elements : (3.0, 4.0) is 7.0
```

#### Use mul functionality :

```
sh bin/cli.sh mul_cmd -e 3 -e 4
# result 
>>the result mul of elements : (3.0, 4.0) is 12.0
```


#### Start monolithic architecture service :
```
sh bin/cli.sh service_monolithic
# result 
>>...
>>2022-03-31 15:58:54,011 - (werkzeug) - INFO -  * Running on http://10.0.2.15:8000/ (Press CTRL+C to quit)
>>...
```
