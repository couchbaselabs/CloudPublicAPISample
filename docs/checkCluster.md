 #  checkCluster
Creates a 3 node cluster , all running the data service.  

createCluster requires one parameters  

-cid ID of the Cluster 
  
You can see the help for the parameters just running checkCluster by itself e.g

```
$ python checkCluster.py                                          
usage: checkCluster.py [-h] -cid CLUSTERID
checkCluster.py: error: the following arguments are required: -cid/--clusterID
$
```
Cluster ID can be found by first running listClusters

Output from checkCluster is formatted JSON

Examples

Cluster in a draft state, not yet deployed

```
$ python checkCluster.py -cid c33522b2-50f1-49fd-8cc6-b59995fee696
Cluster information found
{
  "cloudId": "32cf63e0-b65f-46c0-b936-41542e5ac768",
  "createdAt": "2021-04-21T12:48:41.685114922Z",
  "id": "c33522b2-50f1-49fd-8cc6-b59995fee696",
  "name": "ACluster03",
  "projectId": "89f4459c-85af-438a-a509-d3999c3fb763",
  "resourceIdentifier": "couchbase-fred-acluster03-ee696",
  "status": "draft",
  "tenantId": "aeb0e100-c511-404d-a025-1bc84b47d5b2",
  "updatedAt": "2021-04-21T12:48:41.685114922Z",
  "version": {
    "components": {
      "cbServerVersion": "enterprise-6.6.0",
      "componentVersion": "877efe98",
      "operatorVersion": "2.1.0"
    },
    "name": "enterprise-6.6.0"
  }
}

```

A running Cluster

 ```
$ python checkCluster.py -cid 47f4e4ac-6819-4243-936b-9b9996a44041 
{
  "cloudId": "b0bb69c0-c52f-4294-a022-c505fe5641f2",
  "createdAt": "2021-04-21T14:40:49.469962453Z",
  "deployedAt": "2021-04-21T14:41:03.407460514Z",
  "endpointsSrv": "47f4e4ac-6819-4243-936b-9b9996a44041.dp.cloud.couchbase.com",
  "endpointsURL": [
    "cb-0000.47f4e4ac-6819-4243-936b-9b9996a44041.dp.cloud.couchbase.com",
    "cb-0001.47f4e4ac-6819-4243-936b-9b9996a44041.dp.cloud.couchbase.com",
    "cb-0002.47f4e4ac-6819-4243-936b-9b9996a44041.dp.cloud.couchbase.com"
  ],
  "id": "47f4e4ac-6819-4243-936b-9b9996a44041",
  "name": "ACluster02",
  "privateEndpointURL": [
    "cb-0000.47f4e4ac-6819-4243-936b-9b9996a44041.internal.dp.cloud.couchbase.com",
    "cb-0001.47f4e4ac-6819-4243-936b-9b9996a44041.internal.dp.cloud.couchbase.com",
    "cb-0002.47f4e4ac-6819-4243-936b-9b9996a44041.internal.dp.cloud.couchbase.com"
  ],
  "projectId": "a41a1553-839c-4bed-b855-9a4c80cf0640",
  "resourceIdentifier": "couchbase-prod-acluster02-44041",
  "status": "ready",
  "tenantId": "aeb0e100-c511-404d-a025-1bc84b47d5b2",
  "updatedAt": "2021-04-21T14:54:17.535600368Z",
  "version": {
    "components": {
      "cbServerVersion": "enterprise-6.6.0",
      "componentVersion": "877efe98",
      "nodeImageVersion": "amazon-eks-node-1.16-v20200904",
      "operatorVersion": "2.0.3"
    },
    "name": "enterprise-6.6.0"
  }
}

```
