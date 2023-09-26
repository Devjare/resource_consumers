res=$1
docker image build --tag devjare/${res}-consumer:latest ./${res}
docker push devjare/${res}-consumer:latest

# docker image build --tag devjare/mem-consumer:latest ./MEM
# docker push devjare/mem-consumer:latest
# 
# docker image build --tag devjare/net-consumer:latest ./NET
# docker push devjare/net-consumer:latest
# 
# docker image build --tag devjare/fs-consumer:latest ./FS
# docker push devjare/fs-consumer:latest
