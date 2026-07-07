import json

def format_example(example):
    messages = [
        {"role": "system", "content": "You are a helpful customer support assistant."},
        {"role": "user", "content": example["instruction"]},
        {"role": "assistant", "content": example["response"]}
    ]
    return {"messages": messages}


def convert_file(input_path, output_path):
    with open(input_path, "r") as f:
        data = json.load(f)

    with open(output_path, "w") as out:
        for example in data:
            formatted = format_example(example)
            out.write(json.dumps(formatted) + "\n")

    print(f"Wrote {len(data)} examples to {output_path}")


if __name__ == "__main__":
    convert_file("dataset/train.json", "dataset/train_formatted.jsonl")
    convert_file("dataset/test.json", "dataset/test_formatted.jsonl")