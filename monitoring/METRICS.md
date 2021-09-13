### Metrics lab 8


    1. I added Prometheus image to docker-compose
    2. I added Prometheus as data source to Grafana [Screen 1](screens/prometheus_datasource.png)
    3. I run some metrics to see that it works [Screen 2](screens/prometheus_metrics.png)
    4. I created dashboard by importing ready dashboard Prometheus 2.0 Overview by id 3662 [Screen 3](screens/prometheus_dashboard.png)
    5. I checked that it works performing some actions on my web app as reloading, writing paths that are not existing
    6. I added mem_limit 256 to docker-compose according to lab 8
    
    
### Best practices 

    1. You can import ready dashboard that suits your needs to safe time
    2. Use labels to differentiate the characteristics of the thing that is being measured
    3. Prometheus does not have any units hard coded. For better compatibility, base units should be used
 