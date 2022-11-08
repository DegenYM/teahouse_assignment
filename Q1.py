import statistics as s
import json

def sampling(mean: float, std_dev: float, arr_len: int):
    return s.NormalDist(mu=mean, sigma=std_dev).samples(arr_len)

if __name__ == '__main__':
    mean = 10
    std_dev = 10
    arr_len = 10

    try:
        output =  sampling(mean, std_dev, arr_len)
        print(json.dumps({'elements':output, 'mean':s.mean(output), 'standard deviation': s.stdev(output)}, indent=4))
    except Exception as e:
        print(e)
        