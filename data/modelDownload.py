from transformers import AutoTokenizer, AutoModelForCausalLM

def tryRunningModel(model, tokenizer):
    text = input()
    model = AutoModelForCausalLM.from_pretrained("ai21labs/Jamba-v0.1", trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained("ai21labs/Jamba-v0.1")
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs, max_new_tokens=500)

    print(tokenizer.decode(outputs[0]))


def main():
    #models_list = ["mistralai/Mixtral-8x7B-v0.1"]#, "ai21labs/Jamba-v0.1", "CohereForAI/c4ai-command-r-plus"]

    tokenizer = None
    model = None

    #for model_id in models_list:
    #    print(f"Downloading {model_id}...")
    #    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    #    tokenizer = AutoTokenizer.from_pretrained(model_id)

    #    print(f"Model: {model_id} has been downloaded!")

    #print(f"Finished downloading: \n {models_list}")

    tryRunningModel(model, tokenizer)

if __name__ == '__main__':
    main()
