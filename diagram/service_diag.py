from diagrams import Diagram, Cluster
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.network import Service

with Diagram("Exposed Deployment with 3 Replicas", filename="data/mon.png", show=False):
    with Cluster("Monolithic architecture"):
        svc = Service("svc")
        pods = [Pod("pod1"),
                Pod("pod2"),
                Pod("pod3")]
        
        dp = Deployment("deploy")
        dp >> pods
        svc >> dp