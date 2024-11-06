# OPEA ChatQnA resource management example

## Install NRI plugins helm repo

```bash
helm repo add nri-plugins https://containers.github.io/nri-plugins
```

## Install the balloons policy from NRI plugins

NRI plugins require containerd v1.17+ or crio
v1.26+.

Setting nri.runtime.patchConfig is not needed if NRI is already
enabled. This is the default in containerd v2.0.

```bash
helm install balloons nri-plugins/nri-resource-policy-balloons -n kube-system --set nri.runtime.patchConfig=true
```

## Apply new balloonspolicy configuration

```bash
kubectl apply -n kube-system -f cpu-inference.balloonspolicy.yaml
```

## Observe the status

```bash
kubectl describe -n kube-system balloonspolicy default
```

## Install OPEA ChatQnA for CPU

Follow the OPEA project ChatQnA example [instructions](https://github.com/opea-project/GenAIInfra/blob/main/helm-charts/chatqna/README.md).

## Verify CPUs allowed for containers

Verifying allowed CPUs of inference containers (tgi, tei, and
teirerank), and the vectordb containers for comparison.

```bash
kubectl exec -it chatqna-tgi-646dc474fb-s5rsr -- grep Cpus_allowed_list /proc/self/status
Cpus_allowed_list:      0-7
kubectl exec -it chatqna-tei-854b5bdb74-bqfh9 -- grep Cpus_allowed_list /proc/self/status
Cpus_allowed_list:      16-19
kubectl exec -it chatqna-teirerank-b5cff67f4-vfglg -- grep Cpus_allowed_list /proc/self/status
Cpus_allowed_list:      48-51
kubectl exec -it chatqna-redis-vector-db-676fb75667-ps4w9 -- grep Cpus_allowed_list /proc/self/status
Cpus_allowed_list:      40-47,52-63,104-111,116-127
```

## Increase the number of tgi replicas and verify CPUs

```bash
kubectl edit deployments.apps chatqna-tgi
# After changing replicas from 1 to 2 verify CPUs

for tgipod in $(kubectl get pod -l 'app.kubernetes.io/name=tgi' -o name); do
    echo $tgipod
    kubectl exec $tgipod -- grep Cpus_allowed_list /proc/self/status
done
pod/chatqna-tgi-646dc474fb-5hh7p
Cpus_allowed_list:      32-39
pod/chatqna-tgi-646dc474fb-s5rsr
Cpus_allowed_list:      0-7
```

## Uninstall chatqna and the balloons policy

```bash
helm uninstall chatqna
helm uninstall -n kube-system balloons
```

## References

- OPEA ChatQnA example [link](https://github.com/opea-project/GenAIExamples/tree/main/ChatQnA)

- Balloons policy options [link](https://containers.github.io/nri-plugins/stable/docs/resource-policy/policy/balloons.html)

- This example is part of the KubeCon NA 2024 talk:
  Platform Performance Optimization for AI
  by Dixita Narang and Antti Kervinen.
  [talk](https://sched.co/1i7m0)
  [slides](https://docs.google.com/presentation/d/1lqjjpbUAsCf3muFf9YWN5HGwwHB3XxBJmX2-C7JP41k/)
