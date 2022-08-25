## Argocd
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. 

## Argocd Python Client

For Install Argocd Python Client using following command:

```
$ pip install argo-workflows
```

## Resubmit Workflow using Argocd Python Client:
For resubmiting the same workflow using this python client we need to give our configurations in resubmit_workflow.py file:

```
configuration = argo_workflows.Configuration(host="<YOUR_ARGOCD_SERVER_ENDPOINT>")

```

And you have to give the name and namespace of that workflow which you want to delete:

```
namespace = "<NAMESPACE_OF_ARGOWORKFLOW>"
name= "<NAME_OF_WORKFLOW"
```

```
namespace = "argo"  
name= "hello-yami-resubmitbgpk7"
```


## Run the python file:

```
$ python3 create_workflow.py
```

```
$ python3 resubmit_workflow.py
```

It is successfully resubmitted!!