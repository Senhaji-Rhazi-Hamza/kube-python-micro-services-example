from diagrams import Diagram, Cluster
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.network import Service

with Diagram("Exposed Pod with 3 Replicas", show=False):
    with Cluster("Simple service"):
        svc = Service("svc")
        pods = [Pod("pod1"),
                Pod("pod2"),
                Pod("pod3")]
        #svc >> pods
        
        dp = Deployment("deploy")
        dp >> pods
        svc >> dp
    # net = Ingress("domain.com") >> Service("svc")
    # net >> [Pod("pod1"),
    #         Pod("pod2"),
    #         Pod("pod3")] << ReplicaSet("rs") << Deployment("dp") << HPA("hpa")
