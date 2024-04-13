from transformers import AutoTokenizer, AutoModelForCausalLM

def tryRunningModel(model, tokenizer):
    output = ""
    while True:
        output += input(f"Enter text: ")
        inputs = tokenizer(output, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_length=500)
        output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(output)

def main():
    models_list = "CobraMamba/mamba-gpt-3b-v4" #["mistralai/Mixtral-8x7B-v0.1"]#, "ai21labs/Jamba-v0.1", "CohereForAI/c4ai-command-r-plus"]

    model = AutoModelForCausalLM.from_pretrained(models_list, trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained(models_list)

    #for model_id in models_list:
    #    print(f"Downloading {model_id}...")
    #    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    #    tokenizer = AutoTokenizer.from_pretrained(model_id)

    #    print(f"Model: {model_id} has been downloaded!")

    #print(f"Finished downloading: \n {models_list}")

    tryRunningModel(model, tokenizer)

if __name__ == '__main__':
    main()
