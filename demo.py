
import os
import mlflow
import argparse
import time


def evaluate(param1,param2):
    metrics =  param1*2 + param2*2
    return metrics

def main(p1,p2):
    with mlflow.start_run():
        mlflow.log_param("param1",p1)
        mlflow.log_param("param2",p2)

        metrics = evaluate(p1,p2)
        mlflow.log_metric("someMetric",metrics)

        os.makedirs("temp",exist_ok=True)
        with open("temp/sample.txt","w") as f:
            f.write(time.asctime())
        mlflow.log_artifact("temp")

if __name__=="__main__":
    args= argparse.ArgumentParser()
    args.add_argument("--param1","-p1",type=int,default=2)
    args.add_argument("--param2","-p2",type=int,default=5)
    parsed_args = args.parse_args()

    main(parsed_args.param1,parsed_args.param2)
    print("done.")
