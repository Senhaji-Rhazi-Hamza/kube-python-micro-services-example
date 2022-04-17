from diagrams import Diagram, Cluster
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.network import Service

with Diagram("Microservices", show=False):
    with Cluster("microservices"):
        svc_master = Service("svc_master")
        # pods = [Pod("pod1"),
        #         Pod("pod2"),
        #         Pod("pod3")]
        master_pod = Pod("master_pod")
        master_deploy = Deployment("master_deploy")
        svc_master >>   master_deploy >> master_pod

    

        svc_sum = Service("svc_sum")
        sum_pod = Pod("sum_pod")
        sum_deploy = Deployment("sum_deploy")

        

        svc_mul = Service("svc_mul")
        mul_pod = Pod("mul_pod")
        mul_deploy = Deployment("mul_deploy")


        master_pod  >> svc_sum
        master_pod >> svc_mul
        svc_mul >> mul_deploy >> mul_pod
        svc_sum >> sum_deploy >> sum_pod