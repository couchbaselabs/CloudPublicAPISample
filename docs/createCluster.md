 #  createCluster
Creates a 3 node cluster , all running the data service.  

createCluster requires three parameters to be provided

-cid <ID of the Cloud connection to use with the cluster>
-pid <ID of the Project to use with the cluster>
-cn <Name for the cluster>
  
You can see the help for the parameters just running createCluster by itself e.g

```
$ python createCluster.py
usage: createCluster.py [-h] -cid CLOUDID -pid PROJECTID -cn CLUSTERNAME
createCluster.py: error: the following arguments are required: -cid/--cloudID, -pid/--projectID, -cn/--clusterName
$
```
Cloud ID and Project ID to use with createCluster can be found by using listClouds and listProjects


It will take several minutes for a cluster to be created. createCluster returns an endpoint to find out the status of the cluster which you can poll to see how the deployment is going.  Once the cluster reports as 'Healthy' it is ready for use.

checkCluster can be used for this purpose



Example
```
$ python createCluster.py -cid b0bb69c0-c52f-4294-a022-c505fe5641f2  -pid 22c71ef9-caf2-4dcd-aeea-61563eb64b88 -cn newCluster
Success. Resource status can be checked here:- /v2/clusters/0887f5d9-f7ca-4a4d-9486-727ae95ca88d

```


 
