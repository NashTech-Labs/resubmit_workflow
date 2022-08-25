from pprint import pprint
import requests
import yaml
import argo_workflows
from argo_workflows.api import workflow_service_api

from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_resubmit_request import IoArgoprojWorkflowV1alpha1WorkflowResubmitRequest

configuration = argo_workflows.Configuration(host="https://127.0.0.1:2746")
configuration.verify_ssl = False

resp = requests.get('https://raw.githubusercontent.com/yamikarajput546/argocd-update/master/hello-world.yaml')
manifest = yaml.safe_load(resp.text)

api_client = argo_workflows.ApiClient(configuration)
api_instance = workflow_service_api.WorkflowServiceApi(api_client)
api_response = api_instance.resubmit_workflow(
    namespace="<namespace>",
    name = "<existing_workflow>",
    body=IoArgoprojWorkflowV1alpha1WorkflowResubmitRequest(workflow=manifest, _check_type=False),
    _check_return_type=False)
pprint(api_response)
