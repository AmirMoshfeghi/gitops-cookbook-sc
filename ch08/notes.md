No deployment is created, argocd will take care of the deployments
What if there is a deployment we want argo to take care of?


kubectl argo rollouts list rollouts

kubectl argo rollouts get rollout bgd-rollouts --watch


kubectl argo rollouts promote rollouts-demo


kubectl get ro

When a Rollout has not yet reached its desired state (e.g. it was aborted, or in the middle of an update), and the stable manifest were re-applied, the Rollout detects this as a rollback and not a update, and will fast-track the deployment of the stable ReplicaSet by skipping analysis, and the steps.



