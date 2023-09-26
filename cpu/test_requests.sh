#!/bin/bash
# curl http://192.168.100.7:9010/sort\?size\=500 &  # "tt": 0.04026508331298828
# sleep 5s
# curl http://192.168.100.7:9010/sort\?size\=1000 & # "tt": 0.17967820167541504
# sleep 5s
# curl http://192.168.100.7:9010/sort\?size\=5000 & # "tt": 7.703182935714722
# sleep 5s
# curl http://192.168.100.7:9010/sort\?size\=10000 & # "tt": 159.49358367919922
# sleep 5s
# curl http://192.168.100.7:9010/sort\?size\=10000 & # "tt": 173.5354962348938
# sleep 5s
curl http://192.168.100.7:9010/sort\?size\=15000 & # "tt": 333.56565141677856
# sleep 5s
# curl http://192.168.100.7:9010/sort\?size\=15000 &
# sleep 5s
# curl http://192.168.100.7:9010/sort\?size\=20000 &
# sleep 5s
# curl http://192.168.100.7:9010/sort\?size\=20000
# sleep 5s

# "tt": 336.886869430542
# "tt": 426.40787959098816
# "tt": 422.9974808692932
