hdfs dfs -r /output
hdfs dfs -put input/ /
mapred streaming -input input/train*/tweets.csv -output /output -file Hadoop/base_naivebayes/mapper.py -file Hadoop/base_naivebayes/reducer.py -mapper "python3 mapper.py" -reducer "python3 reducer.py"