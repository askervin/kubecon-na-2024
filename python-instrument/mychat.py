from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=False)

inputs = tokenizer("What happens at KubeCon?", return_tensors="pt")

model.generate(input_ids=inputs['input_ids'], streamer=streamer, max_length=23)
