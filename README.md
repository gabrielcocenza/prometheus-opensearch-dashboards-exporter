# Prometheus Opensearch Dashboards Exporter
An exporter for OpenSearch Dashboards


## Installing
With [poetry](https://python-poetry.org/) installed, clone this repo and run:

```shell
poetry init
```

```shell
poetry build
```

Builds will be located at `dist`. Access the virtual environment and install the build package.

```shell
poetry shell

pip install ./dist/prometheus_opensearch_dashboards_exporter-0.1.0.tar.gz
```


## Running
Identify the url of the `opensearch-dashboards` that you want to monitor, set the `OPENSEARCH_DASHBOARDS_USER` and `OPENSEARCH_DASHBOARDS_PASSWORD` and start the Prometheus exporter:

```shell
export OPENSEARCH_DASHBOARDS_USER="my-user"
export OPENSEARCH_DASHBOARDS_PASSWORD="my-pass"
prometheus-opensearch-dashboards-exporter  http(s)://<IP>:5601
```

After that, it's possible to check the metrics:
```
 curl http://localhost:9684
```

![Example of output](images/opensearch_dashboards_prometheus.png)


By default the server will start at localhost on port `9684`, but it's possible to choose a different one using the `--port` flag. E.g:

```shell
prometheus-opensearch-dashboards-exporter  http(s)://<IP>:5601 -p 9685
```


## Metrics

The metrics exposed by this Exporter are the following.

| Metric                                         | Description                                                                                                                                | Type  |
| -----------------------------------------------| ------------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| `opensearch_dashboards_status`                 | Dashboards overall status. Values `0`, `1`, `2`, `-1` are for Green, Yellow, Red and Unknown, respectively                                 | Gauge |
| `opensearch_dashboards_statuses`               | Dashboards granular status of plugins and core components. Values `0`, `1`, `2`, `-1` are for Green, Yellow, Red and Unknown, respectively | Gauge |
| `opensearch_dashboards_concurrent_connections` | Dashboards Concurrent Connections                                                                                                          | Gauge |
| `opensearch_dashboards_up_time`                | Dashboards uptime in milliseconds                                                                                                          | Gauge |
| `opensearch_dashboards_event_loop_delay`       | Dashboards NodeJS Event Loop Delay in Milli Seconds                                                                                        | Gauge |
| `opensearch_dashboards_heap_total`             | Dashboards Heap total used in bytes                                                                                                        | Gauge |
| `opensearch_dashboards_heap_used`              | Dashboards Heap used in bytes                                                                                                              | Gauge |
| `opensearch_dashboards_heap_size`              | Dashboards Heap size limit in bytes                                                                                                        | Gauge |
| `opensearch_dashboards_re_set_size`            | Dashboards Resident Set Size in bytes                                                                                                      | Gauge |
| `opensearch_dashboards_load_1m`                | Dashboards load average 1m                                                                                                                 | Gauge |
| `opensearch_dashboards_load_5m`                | Dashboards load average 5m                                                                                                                 | Gauge |
| `opensearch_dashboards_load_15m`               | Dashboards load average 15m                                                                                                                | Gauge |
| `opensearch_dashboards_os_mem_total`           | Dashboards OS memory total in bytes                                                                                                        | Gauge |
| `opensearch_dashboards_os_mem_free`            | Dashboards OS memory free in bytes                                                                                                         | Gauge |
| `opensearch_dashboards_os_mem_used`            | Dashboards OS memory used in bytes                                                                                                         | Gauge |
| `opensearch_dashboards_resp_time_avg`          | Dashboards average response time in milliseconds                                                                                           | Gauge |
| `opensearch_dashboards_resp_time_max`          | Dashboards maximum response time in milliseconds                                                                                           | Gauge |
| `opensearch_dashboards_req_disconnects`        | Dashboards request disconnections count                                                                                                    | Gauge |
| `opensearch_dashboards_req_total`              | Dashboards total request count                                                                                                             | Gauge |
