from diagrams import Diagram, Cluster
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.network import Service

with Diagram("Exposed Pod with 3 Replicas", show=False):
    with Cluster("multi-service"):
        svc_master = Service("svc_master")
        # pods = [Pod("pod1"),
        #         Pod("pod2"),
        #         Pod("pod3")]
        master_pod = Pod("master_pod")
        svc_master << master_pod

    # net = Ingress("domain.com") >> Service("svc")
    # net >> [Pod("pod1"),
    #         Pod("pod2"),
    #         Pod("pod3")] << ReplicaSet("rs") << Deployment("dp") << HPA("hpa")
