import statistics as s
import json
import argparse


# Use the following command to run the script:
# python3 -mean {float} -std_dev {float} -arr_len {int}
# For example: python3 -mean 10 -std_dev 10 -arr_len 10

def sampling(mean: float, std_dev: float, arr_len: int):
    return s.NormalDist(mu=mean, sigma=std_dev).samples(arr_len)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-mean", type=float)
    parser.add_argument("-std_dev", type=float)
    parser.add_argument("-arr_len", type=int)
    args = parser.parse_args()

    try:
        output =  sampling(args.mean, args.std_dev, args.arr_len)
        print(json.dumps({'elements':output, 'mean':s.mean(output), 'standard deviation': s.stdev(output)}, indent=4))
    except Exception as e:
        print(e)
    