import json


def main():
    with open("data/train.jsonl", "r") as f:
        train = [json.loads(line) for line in f]
    with open("data/test.jsonl", "r") as f:
        test = [json.loads(line) for line in f]


if __name__ == "__main__":
    main()
