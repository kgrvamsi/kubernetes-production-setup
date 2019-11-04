# kubernetes-production-setup
Ansible Playbooks to install Kubernetes + Vault + Etcd + Falco

```
Things to Complete
1. Etcd  - Cluster
2. K8 Cluster with Flannel
3. K8 Cluster with Calico
3. K8 Fed
4. Vault
5. Etcd Backup and Restore

```

```
Things Completed

1. Etcd - Standalone (With SSL)
2. K8 Cluster with Flannel  -- Not Completed
    a. Control Plane - Completed

```

```
ETCD Cheatsheet

root@instance:/opt/certs# ETCDCTL_API=3 etcdctl --endpoints 127.0.0.1:2379 --cacert /opt/certs/ca.pem  --cert /opt/certs/kubernetes.pem  --key /opt/certs/kubernetes-key.pem put  /example/key new
OK
root@instance:/opt/certs# ETCDCTL_API=3 etcdctl --endpoints 127.0.0.1:2379 --cacert /opt/certs/ca.pem  --cert /opt/certs/kubernetes.pem  --key /opt/certs/kubernetes-key.pem get /example/key
/example/key
new
root@instance:/opt/certs# ETCDCTL_API=3 etcdctl --endpoints 127.0.0.1:2379 --cacert /opt/certs/ca.pem  --cert /opt/certs/kubernetes.pem  --key /opt/certs/kubernetes-key.pem get / --prefix --keys-only
/example/key


etcdctl --endpoints 127.0.0.1:2379 --cacert /opt/certs/ca.pem  --cert /opt/certs/kubernetes.pem  --key /opt/certs/kubernetes-key.pem endpoint health
127.0.0.1:2379 is healthy: successfully committed proposal: took = 8.446026ms
```

```
Kube-API Server Cheatsheet

root@instance:/home/vagrant# kubectl cluster-info
Kubernetes master is running at http://localhost:8080

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

root@instance:/opt/configs# kubectl get cs


root@instance:/home/vagrant# kubectl api-resources -o name

```

```
To Run the test cases:

molecule test

```

```
Known Issues:

1. kubectl get cs have issues to show the component health table
GitHub Issue: https://github.com/kubernetes/kubernetes/issues/83024

root@instance:/opt/configs# kubectl get cs -v=8 --kubeconfig=admin.kubeconfig
I1104 06:33:10.467900   24052 loader.go:375] Config loaded from file:  admin.kubeconfig
I1104 06:33:10.474798   24052 round_trippers.go:420] GET https://172.28.128.37:6443/api/v1/componentstatuses?limit=500
I1104 06:33:10.475082   24052 round_trippers.go:427] Request Headers:
I1104 06:33:10.475303   24052 round_trippers.go:431]     Accept: application/json;as=Table;v=v1beta1;g=meta.k8s.io, application/json
I1104 06:33:10.475585   24052 round_trippers.go:431]     User-Agent: kubectl/v1.16.2 (linux/amd64) kubernetes/c97fe50
I1104 06:33:10.493607   24052 round_trippers.go:446] Response Status: 200 OK in 17 milliseconds
I1104 06:33:10.493623   24052 round_trippers.go:449] Response Headers:
I1104 06:33:10.493627   24052 round_trippers.go:452]     Cache-Control: no-cache, private
I1104 06:33:10.493630   24052 round_trippers.go:452]     Content-Type: application/json
I1104 06:33:10.493633   24052 round_trippers.go:452]     Content-Length: 661
I1104 06:33:10.493636   24052 round_trippers.go:452]     Date: Mon, 04 Nov 2019 06:33:10 GMT
I1104 06:33:10.494115   24052 request.go:968] Response Body: {"kind":"ComponentStatusList","apiVersion":"v1","metadata":{"selfLink":"/api/v1/componentstatuses"},"items":[{"metadata":{"name":"etcd-0","selfLink":"/api/v1/componentstatuses/etcd-0","creationTimestamp":null},"conditions":[{"type":"Healthy","status":"True","message":"{\"health\":\"true\"}"}]},{"metadata":{"name":"controller-manager","selfLink":"/api/v1/componentstatuses/controller-manager","creationTimestamp":null},"conditions":[{"type":"Healthy","status":"True","message":"ok"}]},{"metadata":{"name":"scheduler","selfLink":"/api/v1/componentstatuses/scheduler","creationTimestamp":null},"conditions":[{"type":"Healthy","status":"True","message":"ok"}]}]}
I1104 06:33:10.494660   24052 table_printer.go:44] Unable to decode server response into a Table. Falling back to hardcoded types: attempt to decode non-Table object into a v1beta1.Table
I1104 06:33:10.494685   24052 table_printer.go:44] Unable to decode server response into a Table. Falling back to hardcoded types: attempt to decode non-Table object into a v1beta1.Table
I1104 06:33:10.494694   24052 table_printer.go:44] Unable to decode server response into a Table. Falling back to hardcoded types: attempt to decode non-Table object into a v1beta1.Table
NAME                 AGE
etcd-0               <unknown>
controller-manager   <unknown>
scheduler            <unknown>
root@instance:/opt/configs# kubectl version
Client Version: version.Info{Major:"1", Minor:"16", GitVersion:"v1.16.2", GitCommit:"c97fe5036ef3df2967d086711e6c0c405941e14b", GitTreeState:"clean", BuildDate:"2019-10-15T19:18:23Z", GoVersion:"go1.12.10", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"16", GitVersion:"v1.16.2", GitCommit:"c97fe5036ef3df2967d086711e6c0c405941e14b", GitTreeState:"clean", BuildDate:"2019-10-15T19:09:08Z", GoVersion:"go1.12.10", Compiler:"gc", Platform:"linux/amd64"}
```

