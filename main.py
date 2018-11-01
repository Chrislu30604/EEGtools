import sys
from scipy.io import loadmat
from ssvepbox import CNNtorch


def main():
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "file")
        sys.exit(1)

    text = loadmat(sys.argv[1])
    datasets = text['Data']['EEG'][0][0]


if __name__ == "__main__":
    main()
