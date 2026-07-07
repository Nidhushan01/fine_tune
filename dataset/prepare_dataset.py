from datasets import load_dataset
import json

ds = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset")["train"]

data = []
for row in ds:
    data.append({
        "instruction": row["instruction"],
        "response": row["response"]
    })

split = int(len(data) * 0.9)
train, test = data[:split], data[split:]

with open("dataset/train.json", "w") as f:
    json.dump(train, f, indent=2)
with open("dataset/test.json", "w") as f:
    json.dump(test, f, indent=2)

print(f"Train: {len(train)}, Test: {len(test)}")