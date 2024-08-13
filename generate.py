from transformers import GPT2Tokenizer,GPT2LMHeadModel

def load_tokenizer(model_path):
    tokenizer=GPT2Tokenizer.from_pretrained(model_path)
    return tokenizer

def load_model(model_path):
    model=GPT2LMHeadModel.from_pretrained(model_path)
    return model

def generate_text(model_path,text):
    tokenizer=load_tokenizer(model_path)
    model=load_model(model_path)
    IDs=tokenizer.encode(text,return_tensors='pt')
    outputs=model.generate(IDs,max_length=100,pad_token_id=model.config.eos_token_id,top_k=50,top_p=0.97)
    response=tokenizer.decode(outputs[0],skip_special_tokens=True)
    for i in range(0,len(response)):
        if response[i]=='.':
           response=response[i+1:]
           break
    response=response[::-1]
    for i in range(0,len(response)):
       if response[i]=='.':
           response=response[i:]
           break
    response=response[::-1]
    return response
    