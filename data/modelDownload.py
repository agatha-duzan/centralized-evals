from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    models_list = ["mistralai/Mistral-7B-Instruct-v0.2", "ai21labs/Jamba-v0.1", "CohereForAI/c4ai-command-r-plus"]

    for model_id in models_list:
        print(f"Downloading {model_id}...")
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        print(f"Model: {model_id} has been downloaded!")

    print(f"Finished downloading: \n {models_list}")

if __name__ == '__main__':
    main()
