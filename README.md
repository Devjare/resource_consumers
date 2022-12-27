# Resource random eaters

A collection of configurable containerized docker applications which
consume CPU, DISK, RAM and NET resources in a variable way from
low to hight usage based on specified container limitation.

### Memory consumption

For memory consumption the next endpoints are available:

- To start consuming: ***/start\_consuming*** with *no args*
- To change utilization: ***/change_utilization?utilization_level=n***, 
where $n=\{1, 2, 3\}$ for LOW, MED or HIGH utilization. Considering that:
    - $utilization\_percentage=random(start, end)$ where
        - $start, end=0, 0.3$ for **LOW** Consumption
        - $start, end=0.3, 0.6$ for **MED** Consumption
        - $start, end=0.6, 0.9$ for **HIGH** Consumption
    - LOW Utilization consumes $utilization\_percentage \times TOTAL\_SYSTEM\_MEMORY$ RAM
    - MED Utilization consumes $utilization\_percentage \times TOTAL\_SYSTEM\_MEMORY$ RAM
    - HIGH Utilization consumes $utilization\_percentage \times TOTAL\_SYSTEM\_MEMORY$ RAM
- To stop consuming: ***/stop\_consuming***  with *no args*

### Network consumption
### CPU consumption
