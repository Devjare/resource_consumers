# Resource random eaters

A collection of configurable containerized docker applications which
consume CPU, DISK, RAM and NET resources in a variable way from
low to hight usage based on specified container limitation.

### Memory consumption

For memory consumption the next endpoints are available:

- To start consuming: ***/start\_consumption*** with *no args*
- To change utilization: ***/change_utilization?utilization_level=n***, 
where $n=\{1, 2, 3\}$ for LOW, MED or HIGH utilization. Considering that:
    - $utilization\_percentage=random(start, end)$ where
        - $start, end=0, 0.3$ for **LOW** Consumption
        - $start, end=0.3, 0.6$ for **MED** Consumption
        - $start, end=0.6, 0.9$ for **HIGH** Consumption
    - LOW Utilization consumes $utilization\_percentage \times TOTAL\_SYSTEM\_MEMORY$ RAM
    - MED Utilization consumes $utilization\_percentage \times TOTAL\_SYSTEM\_MEMORY$ RAM
    - HIGH Utilization consumes $utilization\_percentage \times TOTAL\_SYSTEM\_MEMORY$ RAM
- To stop consuming: ***/stop\_consumption***  with *no args*

### CPU consumption
For cpu consumption the next endpoints are available:

- Add process: ***/add\_process*** with *no args*.
- Remove process: ***/remove\_process*** with *no args*.
- Show processes ***/current\_processes*** with *no args*.
- Stop all processes: ***/stop\_consumption*** with *no args*.

The process is a simple bubble sort to an array of size 10000 in an infinite loop, until
***/stop_consumption*** is called, or all processes were stopped by calling enough 
***/remove\_process***.

### Network consumption
